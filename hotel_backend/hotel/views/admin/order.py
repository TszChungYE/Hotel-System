import datetime

from rest_framework.decorators import api_view, authentication_classes

from hotel import utils
from hotel.auth.authentication import AdminTokenAuthtication
from hotel.handler import APIResponse
from hotel.models import Order, Thing
from hotel.serializers import OrderSerializer, ThingSerializer


# 订单信息列表
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        orders = Order.objects.all().order_by('-order_time')
        serializer = OrderSerializer(orders, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


# 创建订单
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])  # 管理员身份验证
def create(request):
    data = request.data.copy()

    if data['user'] is None or data['thing'] is None or data['count'] is None:
        return APIResponse(code=1, msg='创建订单参数错误')

    thing = Thing.objects.get(pk=data['thing'])
    count = data['count']
    if thing.repertory < int(count):
        return APIResponse(code=1, msg='房间数量不足')

    # 处理时间
    create_time = datetime.datetime.now()
    data['create_time'] = create_time
    data['order_number'] = str(utils.get_timestamp())  # 通过当前的时间戳生成订单号
    data['status'] = '1'
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, msg='创建失败')


# 修改订单
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='订单不存在')

    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, msg='更新失败')


# 取消订单
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def cancel_order(request):
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='订单不存在')

    data = {
        'status': 7  # 修改状态为取消
    }
    serializer = OrderSerializer(order, data=data)
    if serializer.is_valid():
        serializer.save()

        return APIResponse(code=0, msg='取消成功', data=serializer.data)
    else:
        print(serializer.errors)
        return APIResponse(code=1, msg='更新失败')


# 删除订单
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Order.objects.filter(id__in=ids_arr).delete()
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='订单不存在')

    return APIResponse(code=0, msg='删除成功')


# 完成订单
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def ok_order(request):
    try:
        id = request.GET.get('id')
        order = Order.objects.get(id=id)
        thing = Thing.objects.get(id=order.thing_id)
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='订单不存在')
    data = {
        'status': 0  # 修改状态为完成
    }
    data1 = {
        'status': 0  # 修改房间状态为空闲
    }
    serializer = OrderSerializer(order, data=data)
    serializer1 = ThingSerializer(thing, data=data1)
    if serializer.is_valid() and serializer1.is_valid():
        serializer.save()
        serializer1.save()

        return APIResponse(code=0, msg='操作成功', data=serializer.data)
    else:
        print(serializer.errors, serializer1.errors)
        return APIResponse(code=1, msg='操作失败')
