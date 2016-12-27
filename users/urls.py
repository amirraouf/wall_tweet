from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import ProfileView, RegisterFormView, UserActivationView

urlpatterns = [
    # accounts/...
    url(r'login/$', login, kwargs={'template_name': 'users/login.html',
                                   'redirect_authenticated_user': True}, name='login'),

    url(r'^logout/$', logout, name='logout'), # used based logout view
    url(r'^profile/(?P<username>[\w.@+-]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^signup/$', RegisterFormView.as_view(), name='register'),
    url(r'^activate/(?P<key>.+)$', UserActivationView.as_view(), name='activation'),
]