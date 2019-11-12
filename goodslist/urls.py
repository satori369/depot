from django.conf.urls import url

from . import views

urlpatterns=[
    #http:127.0.0.1:8000/goodslist/addsort/
    url(r'^addsort/$',views.goodslist_addsort),
    url(r'^addsort_server/$',views.goodslist_addsort_server),

    #http:127.0.0.1:8000/goodslist/addinfo/
    url(r'^addinfo/$',views.goodslist_addinfo),
    #http:127.0.0.1:8000/goodslist/all/
    url(r'^all/$',views.goodslist),
    #http:127.0.0.1:8000/goodslist/delete/
    url(r'^delete/(\d+)$',views.goodslist_delete),
]