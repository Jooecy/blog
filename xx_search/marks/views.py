from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Marks
from django.urls import reverse
from django.http import JsonResponse

def SuccessJson():
    data = {}
    data['status'] = 'SUCCESS'
    return JsonResponse(data)

def ErrorJson():
    data = {}
    data['status'] = 'ERROR'
    data['message'] = '出现错误'
    return JsonResponse(data)

def mark(request):
    context = {}
    data = {}
    if request.user.is_authenticated:
        mark_user = request.GET.get('user')
        user = User.objects.get(username = mark_user)
        title = request.GET.get('title')
        description = request.GET.get('description')
        url = request.GET.get('url')
        is_mark = request.GET.get('is_mark')
        print(title)
        print(url)
        print(user)
        print(is_mark)
        if is_mark == 'true':

            mark = Marks()
            mark.mark_user = user
            mark.title = title
            mark.describe = description
            mark.url = url
            mark.save()
            return SuccessJson()
         

        else:
            del_mark = Marks.objects.filter(mark_user=user,url=url)
            del_mark.delete()
            print('del')
            return SuccessJson()
    else:
        
        return ErrorJson()
    return redirect(reverse('index'))

def all_marks(request):
    context = {}
    try:
        mark_user = request.user
        user = User.objects.get(username = mark_user)
        
        marks = Marks.objects.filter(mark_user=user)
        allmarks = marks.order_by('-id')
        context['allmarks'] = allmarks
        context['all_marks_active'] = 1
    except:
        context['all_marks_active'] = 0
        context['not_login'] = '未登录无法查询'


    return render(request, 'index/index.html', context)

def list_del_mark(request):
    context = {}
    mark_user = request.GET.get('user')
    user = User.objects.get(username = mark_user)
    pk = request.GET.get('id')
    del_mark = Marks.objects.filter(mark_user=user,pk=pk)
    del_mark.delete()
    marks = Marks.objects.filter(mark_user=user)
    allmarks = marks.order_by('-id')
    context['allmarks'] = allmarks
    context['all_marks_active'] = 1
    return render(request, 'index/index.html',context)