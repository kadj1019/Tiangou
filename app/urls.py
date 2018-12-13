from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^homepage/$', views.index, name='homepage'),

    url(r'^login/$', views.login, name='login'),
    url(r'^goods/(\d+)/$', views.goods, name='goods'),
    url(r'^register/$', views.register, name='register'),
    url(r'^loginout', views.loginout, name='loginout')
]
