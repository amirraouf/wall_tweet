from rest_framework import serializers

from ..models import Posts
from users.api.serializers import UserModelSerializer


class PostModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only= True)
    class Meta:
        model = Posts
        fields = "__all__"
