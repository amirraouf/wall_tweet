from django.db.models import Q
from rest_framework.generics import (
        ListAPIView,
        CreateAPIView,
        UpdateAPIView,
        DestroyAPIView,
        RetrieveAPIView
    )
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from ..models import Posts
from .serializers import PostModelDetailSerializer, PostModelListSerializer


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostModelDetailSerializer


class PostUpdateAPIView(UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostModelDetailSerializer


class PostDeleteAPIView(DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostModelDetailSerializer


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostModelDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.user = self.request.user

    def get_queryset(self):
        return Posts.objects.all()


class PostListAPIView(ListAPIView):
    serializer_class = PostModelListSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        qs = Posts.objects.filter(privacy='pb')
        if self.request.user.is_authenticated:
            qs = Posts.objects.all()

        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs