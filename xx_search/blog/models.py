from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation


# 修改模型时要更新数据库


# 创建类别Categorys模型
class Categorys(models.Model):

    # CharField 是一个字符字段，max_length 限制最大长度为20。
    category = models.CharField('类别',max_length=20)

    def __str__(self):
        """定义模型对象显示的具体信息"""
        return self.category
    
    class Meta:
        # verbose_name_plural复数形式，如果只设置verbose_name，在Admin会显示为“文章分类s”
        verbose_name_plural = "文章分类"
        verbose_name = "文章分类"


# 创建博客Blog模型
class Blog(models.Model):

    title = models.CharField('标题', max_length=50)
    blog_category = models.ForeignKey('Categorys',on_delete=models.CASCADE, verbose_name = '分类')
    
    # RichTextUploadingField 是带上传功能的富文本编辑器
    content = models.TextField('内容',)

    # author外键关联User
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = '作者' )

    # auto_now_add 和 auto_now 的区别在于前者添加的时间修改时不变。
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_update_time = models.DateTimeField('修改时间', auto_now=True)
    

    def __str__(self):
        """定义模型对象显示的具体信息"""
        return '<Blog: %s>' % self.title
    
    
    class Meta:
        # verbose_name_plural复数形式，如果只设置verbose_name，在Admin会显示为“博客文章s”
        verbose_name_plural = "博客文章"
        verbose_name = "博客文章"

        # 排序，依据创建时间倒序排列
        ordering = ['-created_time']
