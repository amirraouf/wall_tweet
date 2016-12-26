from rest_framework import serializers

from ..models import Posts
from users.api.serializers import UserModelSerializer


class PostModelDetailSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only= True)
    class Meta:
        model = Posts
        fields = "__all__"



class PostModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = [
            'content',
            'image',
            'privacy',

        ]
