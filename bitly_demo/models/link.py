from django.db import models

class Link(models.Model):
    id = models.AutoField(primary_key=True)
    hash_value = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    original_url = models.CharField(max_length=2048)
    ver = models.IntegerField()