from rest_framework import serializers
from .models import Param, SubParam, ServerParam

class ServerParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerParam
        fields = ['title', 'description']

class SubParamSerializer(serializers.ModelSerializer):
    server_params = ServerParamSerializer(many=True, source='serverparam_set')

    class Meta:
        model = SubParam
        fields = ['title', 'description', 'server_params']

class ParamSerializer(serializers.ModelSerializer):
    sub_params = SubParamSerializer(many=True, source='subparam_set')

    class Meta:
        model = Param
        fields = ['title', 'description', 'sub_params']