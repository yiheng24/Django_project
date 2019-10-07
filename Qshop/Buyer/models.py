from django.db import models
from Seller.models import LoginUser

class PayOrder(models.Model):
    """订单表
       订单状态
       0 未支付
       1 已支付
       2 待发货
       3 待收货
       4/5 完成/拒收
       """
    order_number=models.CharField(max_length=32)
    order_data=models.DateTimeField(auto_now=True)

    order_total=models.FloatField(blank=True,null=True)
    order_user=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)


class OrderInfo(models.Model):
    """订单表
           订单状态
           0 未支付
           1 已支付
           2 待发货
           3 待收货
           4/5 完成/拒收
           """
    order_id=models.ForeignKey(to=PayOrder,on_delete=models.CASCADE)
    goods_id=models.IntegerField()
    goods_picture=models.CharField(max_length=32)
    goods_name=models.CharField(max_length=32)
    goods_count=models.IntegerField()
    order_status = models.IntegerField(default=0)
    goods_price=models.FloatField()
    goods_total_price=models.FloatField()
    store_id=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)



class Cart(models.Model):
    goods_name=models.CharField(max_length=32)
    goods_id=models.IntegerField()
    goods_price=models.FloatField()
    goods_picture=models.CharField(max_length=32)
    goods_total=models.FloatField()
    goods_number=models.IntegerField()
    cart_user=models.IntegerField()

# Create your models here.
