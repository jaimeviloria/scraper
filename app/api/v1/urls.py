from django.conf.urls import url
from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from api.v1.views import ItemList,ItemDetail

urlpatterns=[
        re_path(r'items/$',ItemList.as_view()),
        re_path(r'items/(?P<item_uuid>[-\w]+)/$',ItemDetail.as_view())
        ]

urlpatterns = format_suffix_patterns(urlpatterns)
