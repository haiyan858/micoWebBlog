from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True) # 通过字段user，声明UserProfile类与User类之间的关系是一对一的
    birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return "user {}".format(self.user.username)

