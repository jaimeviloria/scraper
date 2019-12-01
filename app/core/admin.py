from django.contrib import admin
from .models import Snippet, URL


class SnippetAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "urls")


class URLAdmin(admin.ModelAdmin):
    list_display = ("url",)


a_rs = {Snippet: SnippetAdmin, URL: URLAdmin}

for o_r, a_r in a_rs.items():
    admin.site.register(o_r, a_r)
