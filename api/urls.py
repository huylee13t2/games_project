from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^api/invite$', views.invite, name='invite'),
    url(r'^api/get-user$', views.get_user, name='get_user'),
    # user
    url(r'^api/register$', views.register, name='register'),
    url(r'^api/login$', views.login, name='login'),
]

