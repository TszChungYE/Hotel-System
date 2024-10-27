from rest_framework import serializers

from hotel.models import Thing, Classification, Tag, User,  LoginLog, Order, OpLog


# 房间信息序列化
class ThingSerializer(serializers.ModelSerializer):
    """
    ReadOnlyField是一个只读字段，它只用于序列化器的输出，不能用于反序列化器的输入。
    当在序列化器中定义ReadOnlyField时，它将只读取模型实例中的相应字段的值，并将其包含在序列化的输出中。
    这意味着这title字段不能被更新或创建。
    """
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        # 序列化的模型
        model = Thing
        # 序列化所有的字段
        fields = '__all__'


# 房间详情序列化
class DetailThingSerializer(serializers.ModelSerializer):
    # 只读字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Thing
        # 排除多对多字段
        exclude = ('wish', 'collect',)


# 修改房间信息序列化
class UpdateThingSerializer(serializers.ModelSerializer):
    # 只读字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Thing
        # 排除多对多字段
        exclude = ('wish', 'collect',)


# 查询所有房间序列化
class ListThingSerializer(serializers.ModelSerializer):
    # 只读字段
    classification_title = serializers.ReadOnlyField(source='classification.title')

    class Meta:
        model = Thing
        # 排除字段
        exclude = ('wish', 'collect', 'description',)


# 房间分类序列化
class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'


# 房间标签序列化
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# 用户序列化
class UserSerializer(serializers.ModelSerializer):
    # 处理时间格式
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = User
        fields = '__all__'




# 登录日志序列化
class LoginLogSerializer(serializers.ModelSerializer):
    log_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = LoginLog
        fields = '__all__'


# 操作日志序列化
class OpLogSerializer(serializers.ModelSerializer):
    re_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = OpLog
        fields = '__all__'



# 订单信息序列化
class OrderSerializer(serializers.ModelSerializer):
    order_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    expect_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    return_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # 只读字段
    username = serializers.ReadOnlyField(source='user.username')
    # receiver_phone = serializers.ReadOnlyField(source='user.mobile')
    title = serializers.ReadOnlyField(source='thing.title')
    price = serializers.ReadOnlyField(source='thing.price')
    # 文件类型序列化
    cover = serializers.FileField(source='thing.cover', required=False)

    class Meta:
        model = Order
        fields = '__all__'


