from django.shortcuts import render, redirect
from .utils import search
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import logout
from django.urls import reverse
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from marks.models import Marks
from django.shortcuts import HttpResponse

@api_view(['POST'])
def index(request):
    receive = request.data
    context = {}
    # if request.user.is_authenticated:
    keyword = receive.get('search', '')
    if keyword != '':
        print(keyword)
        # result = {'url':'1','title':'2','description':'3'}
        result = search(keyword)
        # if result:
        #     context['result'] = result
        #     context['keyword'] = keyword
        #     context['status'] = 1
        # # else:
        #     context['status'] = 0

        ## 需要错误处理
        if Marks.objects.filter(mark_user=request.user, url=result['url']):
            # print('已经mark过')
            result['is_marked'] = 1
        # else:
        #     print('没有mark过')

        if result == {}:
            return JsonResponse({'err':'没有数据'},safe=False)
        else:
            return JsonResponse(result,safe=False)
            # print(result)
    # else:
    #     print('输入为空')
    #     context['not_login'] = '未登录无法查询'
    return render(request, 'index/index.html', context)  ##之后注释掉
    


@api_view(['POST'])
def login(request):
    receive = request.data
    username = receive.get('username')
    password = receive.get('password')
    user = auth.authenticate(username=username, password=password)
    if not user:
        return HttpResponse("用户名和密码不匹配")
    # 校验通过
    # 删除原有的Token
    old_token = Token.objects.filter(user=user)
    old_token.delete()
    # 创建新的Token
    token = Token.objects.create(user=user)
    return JsonResponse({"username": user.username, "token": token.key})



# def login(request):
#     print('执行了')
#     username = request.POST.get('username')
#     password = request.POST.get('password')
    
#     user = authenticate(request, username=username, password=password)
#     if user:
#         token = Token.objects.update_or_create(user=user)
#         token = Token.objects.get(user=user)


#         # auth.login(request, user)
#         # # Redirect to a success page.
#         # print('登录成功')
#         # print(request.user.username)
#         return JsonResponse({'token':token.key})
#         # return redirect(reverse('index'))
#     else:
#         return JsonResponse({'code':'no','message':'验证失败'})
#         print('登录失败')
#         # return render(request, 'login.html')
#     # return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

def loginstatus(request):
    if request.user.is_authenticated:
        username = request.user.username
        return JsonResponse({'code':1,'username':username})
    else:
        return JsonResponse({'code':0,'username':'没登陆'})


@api_view(['POST'])
def do_something(request):
    # receive = request.data
    # print(receive)
    if request.user.is_authenticated:   # 验证Token是否正确
        print("Do something...")
        return JsonResponse({"msg": "验证通过"})
    else:
        print("验证失败")
        return JsonResponse({"msg": "验证失败"})