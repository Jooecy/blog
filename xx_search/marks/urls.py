from django.urls import path
from . import views

urlpatterns = [
    path('', views.mark, name='mark'),
    path('all', views.all_marks, name='all_marks'),
    path('list_del_mark', views.list_del_mark, name='list_del_mark'),
]