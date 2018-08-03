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
        col = db.desktopIconList
        countArticle = col.find().count()
        dat = JsonResponse({'data': countArticle}, safe=False)
        return dat
def getDesktopIconList(request):
    if request.method == 'POST':
        reqArr = []
        col = db.desktopIconList
        findData = col.find()
        for i in findData:
            i.pop('_id')
            i.pop('content')
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
        col = db.desktopIconList
        findDat = col.find({},{'label':1,'date':1,'id':1})
        # findDat = col.find({}, {"label": 1})
        dat = {
            'id': id,
            'content': []
         }
        if id == 'num0':
            for i in findDat:
                label = i['label']
                date  = i['date']
                id    = i['id']
                dat['content'].append({'label':label,'date':date,'id':id})
        else:
            dat['content'].append({'label': 'other'})
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
        date          = request.POST.get('date')
        contentType = request.POST.get('contentType')
        content     = request.POST.get('content')
        col = db.desktopIconList
        times = time.time()
        dbDat = {
            "label":h1,
            "img": '',
            "url": '',
            "date": date,
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
def getSubmitEditArticle(request):
    if request.method == 'POST':
        id          = request.POST.get('id')
        h1          = request.POST.get('h1')
        date          = request.POST.get('date')
        contentType = request.POST.get('contentType')
        content     = request.POST.get('content')

        col = db.desktopIconList
        col.update({"id":id},{"$set": {
            "label":h1,
            "img": '',
            "url": '',
            "date": date,
            "id": id,
            "content" : {
                "contentType": contentType,
                "data": [{
                    "h1": h1,
                    "content": content
                }]
            }
        }})
        return JsonResponse({'res': 'ok'})
def getDeleteSidebarPopHistory(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        col = db.desktopIconList
        col.remove({'id':id})
        return JsonResponse({'res': 'ok'})