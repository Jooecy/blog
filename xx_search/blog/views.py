import datetime
from django.shortcuts import render, get_object_or_404 # render 载入模板并返回字典或其他响应对象
from django.utils import timezone
from django.db.models import Count, Sum # 求和
from django.conf import settings
from django.core.paginator import Paginator # 分页器
from .models import Blog, Categorys
# from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse


# from comment.forms import CommentForm


# 编写视图别忘了import模型models


# def get_7days_hot_blogs():
#     '''获取7天热门文章'''
#     today = timezone.now().date()
#     days = today - datetime.timedelta(days=7)

#     # 在模型Blog中，read_details反向关联了应用read_stats中的模型ReadDetail
#     # values将筛选（查询）结果按('id', 'title')条件分组，使用 注解 annotate进行注释统计。
#     # order_by 排序方法
#     blogs = Blog.objects.filter(read_details__date__lt=today, read_details__date__gte=days) \
#                 .values('id', 'title').annotate(read_num_sum=Sum('read_details__read_num')) \
#                 .order_by('-read_num_sum')[:7]
#     return blogs


def get_blog_list_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.BLOGS_NUM_OF_PAGE)
    page_num = request.GET.get('page', 1) # 获取链接里面的get参数。(?=page=1)，1为默认值
    page_of_blogs = paginator.get_page(page_num) # 对应页码的blogs

    current_page_num = page_of_blogs.number # 获取当前页码

    # page_range：页码显示的范围为当前页面的前2页和后2页
    # paginator.num_pages 为总页数。
    page_range = list(range(max(current_page_num-2, 1), current_page_num))+ \
                 list(range(current_page_num,min (current_page_num+2, paginator.num_pages)+1))
    
    # 如果页码范围page_range的第一个值与第一页(1)差值>=2，则在页码范围page_range的第一个值前面+'...'
    if page_range[0] - 1 >= 2:
        page_range.insert(0,'...')

    # 如果页码范围page_range的最后一个值与最大页paginator.num_pages差值>=2，则在页码范围page_range的最后一个值后面+'...'
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 如果页码范围page_range第一个值不是1，则将1添加在页码范围page_range的第一个位置。
    if page_range[0] != 1:
        page_range.insert(0,1)

    # 如果页码范围page_range最后一个值不是最大页码，则将最大页码值添加在页码范围page_range的最后一个位置。
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    
    # 创建一个字典context用于向页面模板返回数据
    context = {}

    # 文章归档数据
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    blogs_date_dict = {}
    for blog_date in blog_dates:
        blogs_count = Blog.objects.filter(created_time__year=blog_date.year, created_time__month=blog_date.month).count()
        blogs_date_dict[blog_date] = blogs_count

    # context里面的键blogs相当于一个存入Blog.bojects.all()的变量
    # 之后可以在模板文件中使用变量blogs
    context['num_pages'] = paginator.num_pages
    context['page_of_blogs'] = page_of_blogs
    context['blogs'] = Blog.objects.all()
    context['page_range'] = page_range
    context['categorys'] = Categorys.objects.annotate(blog_count = Count('blog'))
    context['blog_date'] = blogs_date_dict


    return context

#定义博客文章列表页处理方法
def blog_list(request):

    blogs_all_list = Blog.objects.all()
    context = get_blog_list_data(request, blogs_all_list)

    # 获取7日热门
    # context['get_7days_hot_blogs'] = get_7days_hot_blogs()
    res_blogs = [] 
    for i in context['page_of_blogs']:
        res_blogs.append({'title':i.title, 'content':i.content, 'author':i.author.username, 'category':i.blog_category.category, 'time':i.created_time.strftime("%Y-%m-%d"), 'id':i.pk})
    res_blogs.append(context['num_pages'])
    # print(context['num_pages'])
    print(res_blogs)
    return JsonResponse(res_blogs,safe=False)
    # print(context)
    return render(request, 'blog/blog_list.html', context)


# 定义分类文章处理方法
def category_detail(request, category_pk):
    
    
    # 获取类别的pk(主键) 获取模型Category中主键为category_pk的值（具体的类别）
    category = get_object_or_404(Categorys, pk=category_pk)
    blogs_all_list = Blog.objects.filter(blog_category=category)
    context = get_blog_list_data(request, blogs_all_list)
    context['category_name'] = category
    # context['get_7days_hot_blogs'] = get_7days_hot_blogs()
    return render(request, 'blog/category_detail.html', context)


def author_detail(request, author_pk):

    blogs_all_list = Blog.objects.filter(author=author_pk)
    context = get_blog_list_data(request, blogs_all_list)
    # context['get_7days_hot_blogs'] = get_7days_hot_blogs()
    return render(request, 'blog/author_detail.html', context)



def archives(request, year, month):
    
    blogs_all_list = Blog.objects.filter(created_time__year = year, created_time__month = month)
    context = get_blog_list_data(request, blogs_all_list)
    # context['get_7days_hot_blogs'] = get_7days_hot_blogs()
    return render(request, 'blog/archives.html', context)

# 定义文章详情页处理方法
# 处理方法blog_detail需要一个来之url的变量blog_pk
def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)

    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    blogs_date_dict = {}
    for blog_date in blog_dates:
        blogs_count = Blog.objects.filter(created_time__year=blog_date.year, created_time__month=blog_date.month).count()
        blogs_date_dict[blog_date] = blogs_count

    # 变量blog获取主键(id)值为blog_pk的文章


    # 评论内容获取
    # content_type = ContentType.objects.get_for_model(blog)
    # comments = Comment.objects.filter(content_type=content_type, object_id=blog.pk, parent=None)

    # annotate(blog_count = Count('blog'))是一种高级查询，它可以获取模型的全部记录，并为该模型的Queryset
    # 添加了一个属性 blog_count。Queryset中的每个对象都会有这个属性。
    # 这个属性存储了该模型每个对象的blog数量   
    context = {}
    context['categorys'] = Categorys.objects.annotate(blog_count = Count('blog'))
    context['previous_blog'] = Blog.objects.filter(created_time__gt = blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt = blog.created_time).first()
 
    context['blog'] = blog
    # context['get_7days_hot_blogs'] = get_7days_hot_blogs()
 


    context['blog_date'] = blogs_date_dict
    response = render(request, 'blog/blog_detail.html', context)
    return response


