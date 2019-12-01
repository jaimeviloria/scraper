from django.db import models
import uuid

class Item(models.Model):
    item_uuid=models.UUIDField(max_length=64,primary_key=True,blank=True,default=uuid.uuid4(),editable=False)
    item_name=models.CharField(max_length=128)

