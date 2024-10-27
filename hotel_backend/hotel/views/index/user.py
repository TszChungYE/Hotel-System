from rest_framework.decorators import api_view

from hotel import utils
from hotel.handler import APIResponse
from hotel.models import User
from hotel.serializers import UserSerializer, LoginLogSerializer
from hotel.utils import md5value


# 创建登录日志
def make_login_log(request):
    try:
        username = request.data['username']
        data = {
            "username": username,
            "ip": utils.get_ip(request),
            "ua": utils.get_ua(request)
        }
        serializer = LoginLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
    except Exception as e:
        print(e)


# 登录
@api_view(['POST'])  # 只接受post请求
def login(request):
    username = request.data['username']
    password = utils.md5value(request.data['password'])
    users = User.objects.filter(username=username, password=password)
    if len(users) > 0:
        user = users[0]
        # 判断是否是管理员账号
        if user.role in ['1']:
            return APIResponse(code=1, msg='该帐号为后台管理员帐号')
        data = {
            'username': username,
            'password': password,
            'token': md5value(username)  # 生成token令牌
        }
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            make_login_log(request)
            return APIResponse(code=0, msg='登录成功', data=serializer.data)
        else:
            print(serializer.errors)

    return APIResponse(code=1, msg='用户名或密码错误')


# 用户信息
@api_view(['GET'])  # 只接受get请求
def info(request):
    if request.method == 'GET':
        pk = request.GET.get('id', -1)
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)



