from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
def post(request):
    if request.method == 'GET':
        return render(request,'post.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        return JsonResponse({'username': username, "password": password})
def getRightSidebar(request):
    if request.method == 'GET':
        a = request.GET.get('a',0)
        b = request.GET.get('b',0)
        res = float(a) + float(b)
        response = JsonResponse({'res':res}, safe=False)
        return response
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
                'label': 'file1',
                'img': '',
                'url': ''
            },
            {
                'label': 'file2',
                'img': '',
                'url': ''
            },
            {
                'label': 'file3',
                'img': '',
                'url': ''
            }
        ], safe=False)
        return dat
