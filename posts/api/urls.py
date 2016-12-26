from django.conf.urls import url

from .views import (
    PostListAPIView,
    PostCreateAPIView,
    PostRetrieveAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView
)

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/$', PostRetrieveAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', PostUpdateAPIView.as_view(), name='update'),
]