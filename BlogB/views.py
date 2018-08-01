from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
import time
from . import mongodb
from pymongo import MongoClient
def dbIndex(request):
    user1 = mongodb.User(
            username='aa',
            website='www.google.com',
            tags=['111','121','111']
    )
    user1.save()
    Oid = user1.id
    return HttpResponse(Oid)
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
def getSidebarPopContent(request):
    if request.method == 'POST':
        id = request.POST.get('id','')
        dat = {
            'id': id,
            'content': []
         }
        if id == 'num0':
            dat['content'].append('the first update')
            dat['content'].append('the second update')
            dat['content'].append('the third update')
        else:
            dat['content'].append( 'other')
        dat['content'].reverse()
        return JsonResponse(dat)
def getSidebarPopEditPasswordCheck(request): 
    if request.method == 'POST':
        pwd = request.POST.get('pwd','')
        if pwd == 'root':
            return JsonResponse({'data': 'true'})
        else:
            return JsonResponse({'data': 'false'})