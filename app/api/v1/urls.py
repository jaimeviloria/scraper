from django.conf.urls import url
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from api.v1.views import SnippetList, SnippetDetail

urlpatterns = [
    re_path(r"snippets/$", SnippetList.as_view(), name="get_all_snippets"),
    re_path(
        r"snippets/(?P<id>[-\w]+)/$", SnippetDetail.as_view(), name="get_delete_snippet"
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
