from django.shortcuts import render
from core.models import Snippet, URL
from api.v1.serializers import SnippetSerializer
from rest_framework import (
    mixins,
    views,
    generics,
    permissions,
    authentication,
    exceptions,
)
from rest_framework.schemas import AutoSchema

import re


class SnippetList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    """
    list Snippets
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = []
    authentication_classes = []
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return response

    def perform_create(self, serializer):
        urls = find_urls(serializer.initial_data["text"])
        urls_list = []
        for url in urls:
            obj, created = URL.objects.get_or_create(url=url)
            urls_list.append(obj.id)
        serializer.save(urls=urls_list)


class SnippetDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    Retrieve, Update or Delete an Snippet
    """

    schema = AutoSchema()
    permission_classes = []
    authentication_classes = []
    lookup_field = "id"
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return response


def find_urls(text):
    urls = re.findall(
        "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        text,
    )
    return urls
