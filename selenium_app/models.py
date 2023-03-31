from django.db import models

# Create your models here.
class SearchClass (models.Model):
    name=models.CharField(max_length=200)
