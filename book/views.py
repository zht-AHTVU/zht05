from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book.models import AreaInfo

# Create your views here.
def index(request):
    return render(request,'book/index.html')


def login(request):
    if request.session.has_key('is_login'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'book/login.html', {'username': username})


@csrf_exempt
def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    remember = request.POST.get('remember')
    if username == 'admin' and password == '123':
        response = redirect('/index')
        request.session['username'] = username
        request.session['password'] = password
        # request.session['is_login'] = True
        if remember == 'on':
            response.set_cookie('username',username, max_age=14*24*3600)
        return response
    else:
        return redirect('/login')

def areas(request):
    return render(request,'book/areas.html')

def prov(request):
    '''获取所有省级地区的信息'''
    area = AreaInfo.objects.filter(area_parent__isnull=True)
    area_list = []
    for a in area:
        area_list.append((a.id,a.area_name))
    # 返回数据
    return JsonResponse({'data':area_list})


def city(request,prov_id):
    area = AreaInfo.objects.filter(area_parent_id=prov_id)
    area_list = []
    for a in area:
        area_list.append((a.id, a.area_name))
    return JsonResponse({'data':area_list})
#
# def dis(request,city_id):
#     area = AreaInfo.objects.filter(area_parent_id=city_id)
#     area_list = []
#     for a in area:
#         area_list.append((a.id, a.area_name))
#     return JsonResponse({'data':area_list})

