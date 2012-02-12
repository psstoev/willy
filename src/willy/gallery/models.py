from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    category_parent = models.ForeignKey('Category', related_name='parent', null=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
        
class Picture(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=10240)
    uploaded = models.DateTimeField('Upload date')
    owner = models.ForeignKey(User)
    category = models.ManyToManyField(Category, related_name='+')
    pic = models.ImageField(upload_to=settings.USER_FILES_DIR)
