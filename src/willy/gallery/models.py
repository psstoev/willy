from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)
    category_parent = models.ForeignKey('Category', related_name='parent')
    owner = models.ForeignKey(User)
