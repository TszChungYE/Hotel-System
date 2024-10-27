import datetime

from rest_framework.decorators import api_view, authentication_classes

from hotel import utils
from hotel.auth.authentication import TokenAuthtication
from hotel.handler import APIResponse
from hotel.models import Order, Thing, User
from hotel.serializers import OrderSerializer, ThingSerializer


# 获取订单列表
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        userId = request.GET.get('userId', -1)
        orderStatus = request.GET.get('orderStatus', '')  # 订单状态
        orders = Order.objects.all().filter(user=userId).filter(status__contains=orderStatus).order_by('-order_time')
        serializer = OrderSerializer(orders, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


# 创建订单
@api_view(['POST'])
@authentication_classes([TokenAuthtication])  # 用户token验证
def create(request):
    data = request.data.copy()
    # print(data['user'])
    user = User.objects.get(id=data['user'])
    # print(user.mobile)
    if data['user'] is None or data['thing'] is None or data['count'] is None:
        return APIResponse(code=1, msg='创建订单参数错误')
    thing = Thing.objects.get(pk=data['thing'])
    create_time = datetime.datetime.now()
    data['create_time'] = create_time
    data['order_number'] = str(utils.get_timestamp())  # 用当前的时间戳生成订单号
    data['status'] = '1'
    data['receiver_phone'] = user.mobile
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, msg='创建失败')


# 取消订单
@api_view(['POST'])
@authentication_classes([TokenAuthtication])
def cancel_order(request):
    print("取消订单")
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
        # thing = Thing.objects.get(id=order.thing_id)
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='订单不存在')
    data = {
        'status': 7
    }
    serializer = OrderSerializer(order, data=data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='取消成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, msg='更新失败')


# 支付订单
@api_view(['POST'])
@authentication_classes([TokenAuthtication])
def pay_order(request):
    print("支付订单")
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
        thing = Thing.objects.get(id=order.thing_id)
    except Order.DoesNotExist or Thing.DoesNotExist:
        return APIResponse(code=1, msg='订单不存在')
    data = {
        'status': 2
    }
    data1 = {
        'status': 1
    }
    serializer = OrderSerializer(order, data=data)
    serializer1 = ThingSerializer(thing, data=data1)

    if serializer.is_valid() and serializer1.is_valid():
        serializer.save()
        serializer1.save()
        return APIResponse(code=0, msg='支付成功', data=serializer.data)
    else:
        print(serializer.errors,serializer1.errors)
        return APIResponse(code=1, msg='支付失败')
