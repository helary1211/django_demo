from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import json
# Create your views here.


@api_view(['GET'])
def hello(request):
    # username = request.GET.get('username')
    # pwd = request.GET.get('pwd')
    # if username is not None and pwd is not None:
    #     return render(request, 'mall.html', context={"name":username})
    # else:
    #     return render(request, 'error.html', context={"msg":"缺少必要参数"})

    # try:
    #     data = json.loads(request.body)
    # except:
    #     return render(request, 'error.html', context={"msg":'请求非标准json格式'})

    request.FILES
    return HttpResponse('123')