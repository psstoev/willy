from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    category_parent = models.ForeignKey('Category', related_name='parent', null=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
