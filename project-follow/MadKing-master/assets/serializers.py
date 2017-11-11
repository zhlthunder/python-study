#_*_coding:utf-8_*_
__author__ = 'jieli'
from assets.myauth import UserProfile
from assets import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        # fields = ('url', 'name', 'email')
        fields = ('url', 'name', 'email','is_admin')


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asset
        #加上这个，可以同时显示server中的详细的信息；
        depth=2
        fields = ('name', 'sn','server','networkdevice')


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Server
        #fields = ('name', 'sn','server')