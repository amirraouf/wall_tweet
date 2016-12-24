from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import ProfileView

urlpatterns = [
    url(r'login/$', login,{'template_name': 'users/login.html'} ,name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', ProfileView.as_view(), name='profile')
]