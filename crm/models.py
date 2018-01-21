from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name="姓名")
    role = models.ForeignKey("Role", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self): #app = model._meta.app_label return '%s.%s.%s' % (app, model._meta.object_name, self.name)
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=64, unique= True)
    menus = models.ManyToManyField("Menus")

    def __str__(self):
        return self.name


class Menus(models.Model):
    name = models.CharField(max_length=64)
    url_type_choices = (
        (0, 'absolute'),
        (1, 'dynamic'),
    )
    url_type = models.SmallIntegerField(choices=url_type_choices, default=0)
    url_name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Mete:
        unique_together = ('name', 'url_name')

