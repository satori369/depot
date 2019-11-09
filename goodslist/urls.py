from django.conf.urls import url

from . import views

urlpatterns=[
    #http:127.0.0.1:8000/goodslist/add/
    url(r'^addsort/$',views.goodslist_addsort),
    url(r'^addsort_server/$',views.goodslist_addsort_server),

    #http:127.0.0.1:8000/goodslist/all/
    url(r'^addinfo/$',views.goodslist_addinfo),
]