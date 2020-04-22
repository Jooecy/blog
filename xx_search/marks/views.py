
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Marks
from django.urls import reverse
from django.http import JsonResponse
from rest_framework.decorators import api_view



def SuccessJson():
    data = {}
    data['status'] = 'SUCCESS'
    return JsonResponse(data)

def ErrorJson():
    data = {}
    data['status'] = 'ERROR'
    data['message'] = '出现错误'
    return JsonResponse(data)

@api_view(['POST'])
def mark(request):
    context = {}
    # data = {}
    if request.user.is_authenticated:
        print(request.user.username)
        receive = request.data
        mark_user = request.user.username
        user = User.objects.get(username = mark_user)
        title = receive.get('title')
        description = receive.get('description')
        url = receive.get('url')
        is_mark = receive.get('is_mark')
        print(title)
        print(url)
        print(user)
        print(is_mark)
        if is_mark:
            mark = Marks()
            mark.mark_user = user
            mark.title = title
            mark.describe = description
            mark.url = url
            mark.save()
            print('保存成功')
            return JsonResponse({"username": user.username,"test":1})
         

        else:
            del_mark = Marks.objects.filter(mark_user=user,url=url)
            del_mark.delete()
            
            print(user)
            print('del')
        
            return SuccessJson()
    else:
        
        return ErrorJson()
    return redirect(reverse('index'))

@api_view(['POST'])
def all_marks(request):
    # try:
    mark_user = request.user
    user = User.objects.get(username = mark_user)
    marks = Marks.objects.filter(mark_user=user)
    allmarks = marks.order_by('-id')
    marks_list = []
    for i in allmarks:
        marks_dict = {}
        marks_dict['url'] = i.url
        marks_dict['title'] = i.title
        marks_dict['description'] = i.describe
        marks_list.append(marks_dict)
    print(marks_list)
    # return JsonResponse({"allmarks":allmarks})
        # context['allmarks'] = allmarks
        # context['all_marks_active'] = 1
    # except:
        # context['all_marks_active'] = 0
        # context['not_login'] = '未登录无法查询'
    # return JsonResponse({"error":'not login'})

    return JsonResponse(marks_list,safe=False)
    # return render(request, 'index/index.html', {})

@api_view(['POST'])
def list_del_mark(request):
    context = {}
    receive = request.data
    mark_user = request.user
    user = User.objects.get(username = mark_user)
    url = receive.get('url')
    # pk = request.GET.get('id')
    del_mark = Marks.objects.filter(mark_user=user,url=url)
    print(del_mark)
    del_mark.delete()
    print(url)
    # marks = Marks.objects.filter(mark_user=user)
    # allmarks = marks.order_by('-id')
    # context['allmarks'] = allmarks
    # context['all_marks_active'] = 1
    # return render(request, 'index/index.html',context)
    return JsonResponse(url,safe=False)
