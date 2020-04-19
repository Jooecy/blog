from django.urls import path
from . import views


urlpatterns = [
    # path第一个参数定义访问路径及接收的参数，第二个为实现方法的名称
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name='blog_detail' ),
    path('category/<int:category_pk>', views.category_detail, name='category_detail'),
    path('author/<int:author_pk>', views.author_detail, name='author_detail'),
    path('archives/<int:year>/<int:month>', views.archives, name='archives')
]
