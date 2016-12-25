from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import permissions
from ..models import Posts
from .serializers import PostModelSerializer


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = permissions.IsAuthenticated

    def perform_create(self, serializer):
        serializer.user = self.request.user

    def get_queryset(self):
        return Posts.objects.all()


class PostListAPIView(ListAPIView):
    serializer_class = PostModelSerializer

    def get_queryset(self):
        return Posts.objects.all()