from django.shortcuts import render
from core.models import Item
from api.v1.serializers import ItemSerializer
from rest_framework import mixins,views,generics,permissions,authentication,exceptions
from rest_framework.schemas import AutoSchema


class ItemList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    """
    list Items
    """

    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    permission_classes=(permissions.IsAuthenticated,)
    authentication_classes=(authentication.BasicAuthentication,authentication.SessionAuthentication)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        response=self.create(request, *args, **kwargs)
        return response

class ItemDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    """
    Retrieve, Update or Delete an Item
    """

    schema=AutoSchema()
    authentication_classes=(authentication.BasicAuthentication,authentication.SessionAuthentication)
    lookup_field='item_uuid'
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        response=self.update(request, *args, **kwargs)
        return response

    def delete(self, request, *args, **kwargs):
        response=self.destroy(request, *args, **kwargs)
        return response

