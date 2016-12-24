from django.conf.urls import url

from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update'),
]