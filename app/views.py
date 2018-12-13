import hashlib
import random
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.models import Brand, Computer1, Computer_list, Computer_lun, Dress_list, Dress_lun, Gift_lun, Goods, Lunbo, \
    Makeup_list, Makeup_lun, Phone_list, Phone_lun, Vip, Product1, User


def index(request):
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/computer1.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #
    #     lunbo = Computer1()
    #
    #     lunbo.img = dice['img']
    #     # lunbo.price = dice['price']
    #     # lunbo.msg = dice['msg']
    #     lunbo.save()
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/computer_list.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #
    #     lunbo = Computer_list()
    #
    #     lunbo.img = dice['img']
    #     lunbo.price = dice['price']
    #     lunbo.msg = dice['msg']
    #     lunbo.save()
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/computer_lun.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #
    #     lunbo = Computer_lun()
    #
    #     lunbo.img = dice['img']
    #     # lunbo.price = dice['price']
    #     # lunbo.msg = dice['msg']
    #     lunbo.save()
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/dress_list.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #
    #     lunbo = Dress_list()
    #
    #     lunbo.img = dice['img']
    #     lunbo.price = dice['price']
    #     lunbo.msg = dice['msg']
    #     lunbo.save()
    #
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/product1.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #     lunbo = Product1()
    #
    #     lunbo.img = dice['img']
    #     lunbo.price = dice['price']
    #     lunbo.msg = dice['msg']
    #     lunbo.save()
    #
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/goods.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #
    #     lunbo = Goods()
    #
    #     lunbo.img = dice['img']
    #     lunbo.price = dice['price']
    #     # lunbo.msg = dice['msg']
    #     lunbo.bianHao = dice['bianHao']
    #     lunbo.shopPrice = dice['shopPrice']
    #     lunbo.jieShao = dice['jieShao']
    #     lunbo.save()
    #
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/dress_lun.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #
    #     lunbo = Dress_lun()
    #
    #     lunbo.img = dice['img']
    #     # lunbo.price = dice['price']
    #     # lunbo.msg = dice['msg']
    #     lunbo.save()
    #
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/makeup_list.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #
    #     lunbo = Makeup_list()
    #
    #     lunbo.img = dice['img']
    #     lunbo.price = dice['price']
    #     lunbo.msg = dice['msg']
    #     lunbo.save()
    #
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/makeup_lun.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #     lunbo = Makeup_lun()
    #     lunbo.img = dice['img']
    #     # lunbo.price = dice['price']
    #     # lunbo.msg = dice['msg']
    #     lunbo.save()
    #
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/phone_list.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #     lunbo = Phone_list()
    #     lunbo.img = dice['img']
    #     lunbo.price = dice['price']
    #     lunbo.msg = dice['msg']
    #     lunbo.save()
    #
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/phone_lun.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #     lunbo = Phone_lun()
    #     lunbo.img = dice['img']
    #     # lunbo.price = dice['price']
    #     # lunbo.msg = dice['msg']
    #     lunbo.save()
    #
    # with open('/home/kadj/01_Django/Tiangou/Tiangou/json/gift_lun.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #     lunbo = Gift_lun()
    #     lunbo.img = dice['img']
    #     # lunbo.price = dice['price']
    #     # lunbo.msg = dice['msg']
    #     lunbo.save()
    dress = Dress_list.objects.all()
    dress_lun = Dress_lun.objects.all()
    makeup_lun = Makeup_lun.objects.all()
    makeup_list = Makeup_list.objects.all()
    computer_lun = Computer_lun.objects.all()
    computer_list = Computer_list.objects.all()
    computer1 = Computer1.objects.all()
    phone_lun = Phone_lun.objects.all()
    phone_list = Phone_list.objects.all()
    gift_lun = Gift_lun.objects.all()
    pro = Product1.objects.all()
    pro1 = pro[0:4]
    pro2 = pro[4:8]
    pro3 = pro[8:12]
    pro4 = pro[12:16]
    goods = Goods.objects.all()

    token = request.session.get('token')

    data = {
        'dress': dress,
        'dress_lun': dress_lun,
        'makeup_lun': makeup_lun,
        'makeup_list': makeup_list,
        'computer_lun': computer_lun,
        'computer_list': computer_list,
        'computer1': computer1,
        'phone_lun': phone_lun,
        'phone_list': phone_list,
        'gift_lun': gift_lun,
        'pro2': pro2,
        'pro1': pro1,
        'pro3': pro3,
        'pro4': pro4,
        'pro': pro,
        'goods': goods,
    }
    if token:
        user = User.objects.get(token=token)
        data['username'] = user.username
        data['email'] = user.email
    return render(request, 'homepage/homepage.html', context=data)


#
# def generate_password(param):
#     md5 = hashlib.md5()
#     md5.update(param.encode('utf-8'))
#
#     return md5.hexdigest()
#
#
def generate_token():
    md5 = hashlib.md5()
    temp = str(time.time()) + str(random.random())
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()


def goods(request, id):
    goods = Goods.objects.get(pk=id)

    data = {
        "goods": goods
    }

    return render(request, 'goods/goods.html', context=data)


def login(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        if user:
            if password == user.password:
                user.token = generate_token()
                user.save()
                request.session['token'] = user.token
                return redirect('tiangou:homepage')
        else:
            return HttpResponse('账号或者密码错误')

def register(request):
    if request.method == "GET":
        return render(request, 'login/register.html')
    elif request.method == "POST":
        user = User()
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.token = generate_token()
        user.save()
        request.session['token'] = user.token

        return redirect('tiangou:homepage')
