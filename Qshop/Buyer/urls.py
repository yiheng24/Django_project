from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('index/', index),
    path('logout/', logout),
    path('goods_list/', goods_list),
    path('user_info/', user_info),
    re_path('goods_detail/(?P<id>\d+)/', goods_detail),
    path('Alipay/', Alipay),
    path('pay_order/', pay_order),

    path('pay_order_more/', pay_order_more),

    path('pay_result/', pay_result),
    path('add_cart/', add_cart),
    path('cart/', cart),
    path('uco/', user_center_order),
    path('mtv/', middle_test_view),
]
