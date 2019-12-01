from rest_framework import serializers
from core.models import Snippet, URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ("url",)


class SnippetSerializer(serializers.ModelSerializer):
    urls = URLSerializer(many=True, read_only=True)

    class Meta:
        model = Snippet
        fields = ("id", "text", "urls")
