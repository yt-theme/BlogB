from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
import time
from . import mongodb
############## db ##################
from pymongo import MongoClient
conn = MongoClient('localhost', 27017)
db = conn.blog
############## eb end ##############
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
        reqArr = []
        col = db.desktopIconList
        for i in col.find():
            i.pop('_id')
            reqArr.append(i)
        dat = JsonResponse(reqArr, safe=False)
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
        if id:
            findDat = db.desktopIconList.find_one({"id":id})
            print(id)
            return JsonResponse({
                'id': findDat['id'],
                'contentType': findDat['content']['contentType'],
                'data': [
                    {
                        'h1': findDat['content']['data'][0]['h1'],
                        'content': findDat['content']['data'][0]['content'],
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
def getSubmitNewArticle(request):
    if request.method == 'POST':
        h1          = request.POST.get('h1')
        contentType = request.POST.get('contentType')
        content     = request.POST.get('content')
        col = db.desktopIconList
        times = time.time()
        dbDat = {
            "label":h1,
            "img": '',
            "url": '',
            "id": str(round( times * 1000)),
            "content" : {
                "contentType": contentType,
                "data": [{
                    "h1": h1,
                    "content": content
                }]
            }
        }
        col.save(dbDat)
        return JsonResponse({'res': 'ok'})