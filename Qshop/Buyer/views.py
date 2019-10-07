from django.core.paginator import Paginator
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from Seller.models import *
from Seller.views import setPassword
from Buyer.models import *

def logVaild(fun):
    def inner(request,*args,**kwargs):
        cookie_user=request.COOKIES.get('username')
        session_user=request.session.get('username')
        if cookie_user and session_user and cookie_user==session_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Buyer/login/')
    return inner

def login(request):
    if request.method == "POST":
        password = request.POST.get("pwd")
        email = request.POST.get("email")
        user = LoginUser.objects.filter(email = email).first()
        if user:
            db_password = user.password
            password = setPassword(password)
            if db_password == password:
                response= HttpResponseRedirect("/Buyer/index/")
                response.set_cookie('username',user.username)
                response.set_cookie('user_id',user.id)
                request.session['username']=user.username
                return response
    return render(request, "buyer/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("pwd")
        email = request.POST.get("email")

        user = LoginUser()
        user.username = username
        user.password = setPassword(password)
        user.email = email
        user.save()
        return HttpResponseRedirect("/Buyer/login/")
    return render(request, "buyer/register.html")
def logout(request):
    url=request.META.get('HTTP_REFERER','/Buyer/index/')
    response=HttpResponseRedirect(url)
    for k in request.COOKIES:
        response.delete_cookie(k)
    del request.session['username']
    return response

def index(request):
    goods_type = GoodsType.objects.all() #获取所有类型
    result = []
    for ty in goods_type:
        # 按照生产日期对对应类型的商品进行排序
        goods = ty.goods_set.order_by("-goods_pro_time")
        if len(goods) >= 4: #进行条件判断
            goods = goods[:4]
            result.append({"type":ty,"goods_list":goods})
    return render(request,"buyer/index.html",locals())

def goods_list(request):
    """
    type 代表请求的类型
        t 按照类型查询
            keywords必须是类型id
        k 按照关键字查询
            keywords可以是任何东西
    keywords 代表请求的关键字
    """
    request_type = request.GET.get("type") #获取请求的类型 t 类型查询 k关键字查询
    keyword = request.GET.get("keywords") #查询的内容 t类型 k为类型id  k类型 k为关键字
    goods_list = [] #返回的结果
    if request_type == "t": #t类型查询
        if keyword:
            id = int(keyword)
            goods_type = GoodsType.objects.get(id = id) #先查询类型
            goods_list = goods_type.goods_set.order_by("-goods_pro_time") #再查询类型对应的商品
    elif request_type == "k":
        if keyword:
            goods_list = Goods.objects.filter(goods_name__contains=keyword).order_by("-goods_pro_time") #模糊查询商品名称含有关键字的商品
    if goods_list: #限定推荐的条数
        lenth = len(goods_list) / 5
        if lenth != int(lenth):
            lenth += 1
        lenth = int(lenth)
        recommend = goods_list[:lenth]
    return render(request,"buyer/goods_list.html",locals())


def goods_detail(request,id):
    goods = Goods.objects.get(id = int(id))
    return render(request,"buyer/detail.html",locals())


def user_info(request):
    return render(request,'buyer/user_info.html',locals())


import time
import datetime
@logVaild
def pay_order(request):
    goods_id=request.GET.get('goods_id')
    count=request.GET.get('count')
    if goods_id and count:
        order=PayOrder()
        order.order_number=str(time.time()).replace('.','')
        order.order_data=datetime.datetime.now()
        order.order_status=0
        order.order_user=LoginUser.objects.get(id=int(request.COOKIES.get('user_id')))
        order.save()

        goods=Goods.objects.get(id=int(goods_id))
        order_info=OrderInfo()
        order_info.order_id=order
        order_info.goods_id=goods.id
        order_info.goods_picture=goods.picture
        order_info.goods_name=goods.goods_name
        order_info.goods_count=int(count)
        order_info.goods_price=goods.goods_price
        order_info.goods_total_price=goods.goods_price*int(count)
        order_info.store_id=goods.goods_store
        order_info.save()
        order.order_total=order_info.goods_total_price
        order.save()
    return render(request,'buyer/pay_order.html',locals())
@logVaild
def pay_order_more(request):
    data=request.GET
    data_item=data.items()
    request_data=[]
    for key,value in data_item:
        if key.startswith('check_'):
            goods_id=key.split('_',1)[1]
            count=data.get('count_'+goods_id)
            request_data.append(int(goods_id),int(count))

    if request_data:
        order=PayOrder()
        order.order_number=str(time.time()).replace('.','')
        order.order_data=datetime.datetime.now()
        order.order_status=0
        order.order_user=LoginUser.objects.get(id=int(request.COOKIES.get('user_id')))
        order.save()
        order_total=0
        for goods_id,count in request_data:
            goods=Goods.objects.get(id=int(goods_id))
            order_info=OrderInfo()
            order_info.order_id=order
            order_info.goods_id=goods.id
            order_info.goods_picture=goods.picture
            order_info.goods_name=goods.goods_name
            order_info.goods_count=int(count)
            order_info.goods_price=goods.goods_price
            order_info.goods_total_price=goods.goods_price*int(count)
            order_info.store_id=goods.goods_store
            order_info.save()
            order.order_total+=order_info.goods_total_price
        order_total=order.order_total
        order.save()
    return render(request,'buyer/pay_order.html',locals())

def pay_result(request):
    return render(request,'buyer/AliPay.html',locals())


from alipay import AliPay
from Qshop.settings import alipay_public_key_string,alipay_private_key_string

def Alipay(request):
    # 实例化支付
    order_number=request.GET.get('order_number')
    goods_total=request.GET.get('total')
    alipay = AliPay(
        appid=2016101200667746,
        app_notify_url=None,
        app_private_key_string=alipay_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type='RSA2'
    )
    # 实例化订单

    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_number,  # 订单号，唯一
        total_amount=str(goods_total),  # 支付金额
        subject='快活林',  # 支付主题
        return_url='http://127.0.0.1:8000/Buyer/pay_result/',
        notify_url=None,
    )

    # 拼接收款地址
    result = "https://openapi.alipaydev.com/gateway.do?" + order_string

    return HttpResponseRedirect(result)



def add_cart(request):
    result={
        'code':200,
        'data':''
    }
    if request.method=='POST':

        id = int(request.POST.get('goods_id'))
        count=int(request.POST.get('count',1))

        goods=Goods.objects.get(id=id)
        cart=Cart()
        cart.goods_name=goods.goods_name
        cart.goods_id=id
        cart.goods_number=count
        cart.goods_price=goods.goods_price
        cart.goods_picture=goods.picture
        cart.goods_total=goods.goods_price*count
        cart.cart_user=request.COOKIES.get('user_id')
        cart.save()
        result['data']='加入购物车成功'

    else:
        result['code']=500
        result['data']='请求数据有误'
    return JsonResponse(result)


def cart(request):
    user_id=request.COOKIES.get('user_id')
    goods=Cart.objects.filter(cart_user=int(user_id)).order_by('-id')
    count=goods.count()
    return render(request,'buyer/cart.html',locals())

def user_center_order(request):
    user_id=request.COOKIES.get('user_id')
    user=LoginUser.objects.get(id=int(user_id))
    order_list=user.payorder_set.order_by('-order_data')
    return render(request,'buyer/user_center_order.html',locals())


from django.http import HttpResponse
def middle_test_view(request):
    def hello():
        return HttpResponse('hello world')
    rep=HttpResponse('hello')
    rep.render=hello
    return rep

