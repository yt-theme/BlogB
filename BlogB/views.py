from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
import time
def post(request):
    if request.method == 'GET':
        return render(request,'post.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        return JsonResponse({'username': username, "password": password})
def getMenu(request):
    if request.method == 'GET':
        dat =  JsonResponse([
            {
                'label': 'file',
                'action': ''
            },
            {
                'label': 'edit',
                'action': ''
            },
            {
                'label': 'select',
                'action': ''
            }
        ], safe=False)
        return dat
def getNotifyNumber(request):
    if request.method == 'GET':
        dat = JsonResponse({'data': 11}, safe=False)
        return dat
def getDesktopIconList(request):
    if request.method == 'POST':
        dat = JsonResponse([
            {
                'label': 'The Blog Start',
                'img': '',
                'url': '',
                'id':  'num1'
            },
            {
                'label': 'file2',
                'img': '',
                'url': '',
                'id': 'num2'
            },
            {
                'label': 'file3',
                'img': '',
                'url': '',
                'id': 'num3'
            }
        ], safe=False)
        return dat
def getSidebarIconList(request):
    if request.method == 'POST':
        dat = JsonResponse([
            {
                'label': 'Baidu',
                'img': '',
                'url': 'https://www.baidu.com'
            },
            {
                'label': 'Arch',
                'img': '',
                'url': 'https://www.archlinux.org/'
            },
            {
                'label': 'Github',
                'img': '',
                'url': 'https://github.com/'
            },
            {
                'label': 'Kernel',
                'img': '',
                'url': 'https://www.kernel.org/'
            },
            {
                'label': 'Distrowatch',
                'img': '',
                'url': 'https://distrowatch.org/'
            }
        ], safe=False)
        return dat
def getWindowContent(request):
    if request.method == 'POST':
        id = request.POST.get('id','')
        if id == 'num1':
            return JsonResponse({
                'id': id,
                'contentType': 'web',
                'data': [
                    {
                        'h1': 'The Blog Start',
                        'content': '<div style=line-height:2;margin-top:40px><p>Today is 2018.7.27 17:25:51</p>' +
                            '<p>Good-luck</p></div>',
                    }    
                ]
            })
        else:
            return JsonResponse({
                'id': id,
                'contentType': 'txt',
                'data': [
                    {
                        'h1': 'not file1',
                        'content': '233'
                    }    
                ]
            })
