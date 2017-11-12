#_*_coding:utf-8_*_
__author__ = 'jieli'
from assets import  myauth
from rest_framework import viewsets
from assets.serializers import UserSerializer, AssetSerializer,ServerSerializer
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from assets import models


#下面每个视图的格式是固定的，且queryset 和serializer_class 命名也是固定的。
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = myauth.UserProfile.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Asset to be viewed or edited.
    """
    queryset = models.Asset.objects.all()
    serializer_class = AssetSerializer

class ServerViewSet(viewsets.ModelViewSet):

    queryset = models.Server.objects.all()
    serializer_class = ServerSerializer




@api_view(['GET', 'POST'])  #定义了支持的方法类型，比如如果删除get方法，再执行获取时就会提示 无权限；
@permission_classes((permissions.AllowAny,)) ##定义了用户权限控制
def AssetList(request):
    if request.method == 'GET':
        asset_list = models.Asset.objects.all()
        serializer = AssetSerializer(asset_list,many=True)
        # print serializer.data
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
