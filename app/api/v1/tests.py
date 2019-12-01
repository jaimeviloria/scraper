import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from core.models import Snippet
from api.v1.serializers import SnippetSerializer

# initialize the APIClient app
client = Client()


class GetAllSnippets(TestCase):
    """ Test module for GET all snippets API """

    def setUp(self):
        Snippet.objects.create(text="www.google.com")
        Snippet.objects.create(text="www.test.com")
        Snippet.objects.create(text="http://www.anothertest.com")
        Snippet.objects.create(text="https://www.andanothertest.com")

    def test_get_all_snippets(self):
        # get API response
        response = client.get(reverse("get_all_snippets"))
        # get data from db
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleSnippetTest(TestCase):
    """ Test module for GET single snippet API """

    def setUp(self):
        self.ggl = Snippet.objects.create(text="www.google.com")
        self.testsite = Snippet.objects.create(text="www.test.com")
        self.anothertest = Snippet.objects.create(text="http://www.anothertest.com")
        self.andagain = Snippet.objects.create(text="https://www.andanothertest.com")

    def test_get_valid_single_snippet(self):
        response = client.get(reverse("get_delete_snippet", kwargs={"id": self.ggl.id}))
        snippet = Snippet.objects.get(pk=self.ggl.pk)
        serializer = SnippetSerializer(snippet)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_snippet(self):
        response = client.get(reverse("get_delete_snippet", kwargs={"id": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewSnippetTest(TestCase):
    """ Test module for inserting a new snippet """

    def setUp(self):
        self.valid_payload = {
            "text": "w3.coolsite.io",
        }
        self.invalid_payload = {
            "text": "",
        }

    def test_create_valid_snippet(self):
        response = client.post(
            reverse("get_all_snippets"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_snippet(self):
        response = client.post(
            reverse("get_all_snippets"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleSnippetTest(TestCase):
    """ Test module for deleting an existing snippet record """

    def setUp(self):
        self.ggl = Snippet.objects.create(text="www.google.com")
        self.testsite = Snippet.objects.create(text="www.test.com")
        self.anothertest = Snippet.objects.create(text="http://www.anothertest.com")
        self.andagain = Snippet.objects.create(text="https://www.andanothertest.com")

    def test_valid_delete_snippet(self):
        response = client.delete(
            reverse("get_delete_snippet", kwargs={"id": self.ggl.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_snippet(self):
        response = client.delete(reverse("get_delete_snippet", kwargs={"id": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
