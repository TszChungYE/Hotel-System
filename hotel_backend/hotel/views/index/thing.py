from rest_framework.decorators import api_view

from hotel import utils
from hotel.handler import APIResponse
from hotel.models import Thing, Tag, User
from hotel.serializers import ThingSerializer, ListThingSerializer, DetailThingSerializer


# 首页房间数据
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        # print("首页获取数据")
        keyword = request.GET.get("keyword", None)  # 关键词
        c = request.GET.get("c", None)  # 分类
        tag = request.GET.get("tag", None)  # 标签
        sort = request.GET.get("sort", 'recent')  # 排序

        # 排序方式
        order = '-create_time'
        if sort == 'recent':
            order = '-create_time'
        elif sort == 'hot' or sort == 'recommend':
            order = '-pv'

        if keyword:
            things = Thing.objects.filter(title__contains=keyword).order_by(order)

        elif c and int(c) > -1:
            ids = [c]
            things = Thing.objects.filter(classification_id__in=ids).order_by(order)

        elif tag:
            tag = Tag.objects.get(id=tag)
            # print(tag)
            things = tag.thing_set.all().order_by(order)

        else:
            # 延迟加载
            things = Thing.objects.all().defer('wish').order_by(order)

        serializer = ListThingSerializer(things, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


# 房间详情
@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        thing = Thing.objects.get(pk=pk)
    except Thing.DoesNotExist:
        utils.log_error(request, '房间不存在')
        return APIResponse(code=1, msg='房间不存在')

    if request.method == 'GET':
        serializer = ThingSerializer(thing)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)

