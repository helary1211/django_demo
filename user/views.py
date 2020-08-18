from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view
import json
# Create your views here.
source = {
    "business_autoFans_J":[14,15,9],
    "autoAx":[7,32,0],
    "autoAx_admin":[5,13,2]
}
def hello(request):
    # return render(request,'user.html')
    result = {"code":0, "msg":"ok"}
    if request.method == "GET":
        return HttpResponse(content_type="application/json", content=json.dumps(result))
    else:
        return HttpResponse(status=405, reason='method not allowed')

@api_view(['POST'])
def api_login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    is_login = request.POST.get('is_login')
    if username is not None and password is not None:

        if username == 'admin' and password == 'admin':
            res = HttpResponseRedirect('/user/home/')
            res.set_cookie('uid','1',httponly=True)
            res.set_cookie('username', 'admin')
            res.set_signed_cookie('password', 'admin', salt='123')
            return res
        else:
            return render(request, 'error.html', context={"msg":"用户名或密码错误！"})
    else:
        return render(request, 'error.html', context={"msg":'用户名、密码不能为空！'})

def login(request):
    return render(request, 'login.html')

def home(request):
    if request.COOKIES.get('uid') == '1'and request.COOKIES.get('username') == 'admin'\
            and request.get_signed_cookie('password',salt='123') == 'admin':
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/user/login/')


@api_view(['POST'])
def api_buglogs(request):
    total_num = 0
    if request.method == "POST":
        pname = request.GET.get("pname")
        print(pname)
    if pname is not None:
        if pname in source.keys():
            for i in source[pname]:
                total_num += i
            return JsonResponse({"total":total_num, "name":pname})
        else:
            return JsonResponse({"error":10000, "msg":"不存在该项目"})
    else:
        for key in source.keys():
            for i in source[key]:
                total_num += i
        return JsonResponse({"total":total_num, "name":"all"})
