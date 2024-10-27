from django.db import models


# 用户信息表
class User(models.Model):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    ROLE_CHOICES = (
        ('0', '管理员'),
        ('1', '普通用户'),
    )
    STATUS_CHOICES = (
        ('0', '正常'),
        ('1', '封号'),
    )
    id = models.BigAutoField(primary_key=True)  # id
    username = models.CharField(max_length=50, null=True)  # 用户名
    password = models.CharField(max_length=50, null=True)  # 密码
    role = models.CharField(max_length=2, blank=True, null=True)  # 角色
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')  # 状态
    nickname = models.CharField(blank=True, null=True, max_length=20)  # 昵称
    avatar = models.FileField(upload_to='avatar/', null=True)  # 头像
    mobile = models.CharField(max_length=13, blank=True, null=True)  # 手机
    email = models.CharField(max_length=50, blank=True, null=True)  # 邮箱
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)  # 性别
    description = models.TextField(max_length=200, null=True)  # 简介
    create_time = models.DateTimeField(auto_now_add=True, null=True)  # 创建时间
    score = models.IntegerField(default=0, blank=True, null=True)
    push_email = models.CharField(max_length=40, blank=True, null=True)
    push_switch = models.BooleanField(blank=True, null=True, default=False)
    admin_token = models.CharField(max_length=32, blank=True, null=True)  # 管理员token
    token = models.CharField(max_length=32, blank=True, null=True)  # token

    # 设置表名称
    class Meta:
        db_table = "b_user"


# 标签信息表（房间的标签，如：有空调、阳台等）
class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)  # id
    title = models.CharField(max_length=100, blank=True, null=True)  # 标题
    create_time = models.DateTimeField(auto_now_add=True, null=True)  # 创建时间

    class Meta:
        db_table = "b_tag"


# 房间分类表
class Classification(models.Model):
    list_display = ("title", "id")  # 设置后台显示的内容
    id = models.BigAutoField(primary_key=True)  # id
    title = models.CharField(max_length=100, blank=True, null=True)  # 标题
    create_time = models.DateTimeField(auto_now_add=True, null=True)  # 创建时间

    # 当它作为外键的时候，显示标题
    def __str__(self):
        return self.title

    class Meta:
        db_table = "b_classification"


# 房间信息表
class Thing(models.Model):
    STATUS_CHOICES = (
        ('0', '空闲'),
        ('1', '入住'),
    )
    id = models.BigAutoField(primary_key=True)  # id
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='classification_thing')  # 分类
    tag = models.ManyToManyField(Tag, blank=True)  # 标签
    title = models.CharField(max_length=100, blank=True, null=True)  # 房间名称
    cover = models.ImageField(upload_to='cover/', null=True)  # 封面
    description = models.TextField(max_length=1000, blank=True, null=True)  # 描述
    price = models.CharField(max_length=50, blank=True, null=True)  # 价格
    window = models.CharField(max_length=10, blank=True, null=True)  # 是否带窗户
    address = models.CharField(max_length=50, blank=True, null=True)  # 地址
    sheshi = models.CharField(max_length=50, blank=True, null=True)  # 设施
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')  # 房间状态
    create_time = models.DateTimeField(auto_now_add=True, null=True)  # 创建时间
    pv = models.IntegerField(default=0)
    recommend_count = models.IntegerField(default=0)  # 评论数量
    wish = models.ManyToManyField(User, blank=True, related_name="wish_things")  # 想住
    wish_count = models.IntegerField(default=0)  # 想住数量
    collect = models.ManyToManyField(User, blank=True, related_name="collect_things")  # 收藏
    collect_count = models.IntegerField(default=0)  # 收藏数量

    class Meta:
        db_table = "b_thing"


# 登录日志表
class LoginLog(models.Model):
    id = models.BigAutoField(primary_key=True)  # id
    username = models.CharField(max_length=50, blank=True, null=True)  # 用户名
    ip = models.CharField(max_length=100, blank=True, null=True)  # ip地址
    ua = models.CharField(max_length=200, blank=True, null=True)  # ua
    log_time = models.DateTimeField(auto_now_add=True, null=True)  # 时间

    class Meta:
        db_table = "b_login_log"


# 操作日志
class OpLog(models.Model):
    id = models.BigAutoField(primary_key=True)  # id
    re_ip = models.CharField(max_length=100, blank=True, null=True)  # ip地址
    re_time = models.DateTimeField(auto_now_add=True, null=True)  # 时间
    re_url = models.CharField(max_length=200, blank=True, null=True)  # 操作路径
    re_method = models.CharField(max_length=10, blank=True, null=True)  # 请求方法
    re_content = models.CharField(max_length=200, blank=True, null=True)  # 内容
    access_time = models.CharField(max_length=10, blank=True, null=True)  # 访问时间

    class Meta:
        db_table = "b_op_log"




# 订单信息表
class Order(models.Model):
    id = models.BigAutoField(primary_key=True)  # id
    order_number = models.CharField(max_length=13, blank=True, null=True)  # 订单号
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_order')  # 用户
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE, null=True, related_name='thing_order')  # 房间
    count = models.IntegerField(default=0)  # 数量
    status = models.CharField(max_length=2, blank=True, null=True)  # 订单状态： 1未支付 2已支付 7订单取消 0已完成
    order_time = models.DateTimeField(auto_now_add=True, null=True)  # 预定时间
    pay_time = models.DateTimeField(null=True)  # 支付时间
    receiver_name = models.CharField(max_length=20, blank=True, null=True)  # 姓名
    receiver_address = models.CharField(max_length=50, blank=True, null=True)  # 地址
    receiver_phone = models.CharField(max_length=20, blank=True, null=True)  # 电话
    remark = models.CharField(max_length=30, blank=True, null=True)  # 备注

    class Meta:
        db_table = "b_order"
