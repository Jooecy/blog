from django.contrib import admin
from .models import Categorys, Blog



# 将模型加入后台管理



@admin.register(Categorys)
class Categorys_admin(admin.ModelAdmin):

    # list_display 把希望显示的 字段 添加到后台管理页面。
    list_display = ('id', 'category',) 

    
@admin.register(Blog)
class Blog_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_category', 'author', 'created_time', 'last_update_time')
    
    # list_editable 设置可快速编辑的条目
    list_editable = ('blog_category', 'title', )

    # 设置可用于后台搜索的 字段
    search_fields = ('title', 'content', 'blog_category__category')