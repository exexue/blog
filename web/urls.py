
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import *
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name = 'index'),
    url(r'^list/(\d+)$',list,name = 'list'),
    url(r'^show/(\d+)/$',show,name = 'show'),
    url(r'^uedit/(\d+)$',uedit,name = 'uedit'),
    url(r'^send/$',send,name = 'send'),

]
