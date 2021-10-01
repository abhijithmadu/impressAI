from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stupid = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    dumb = models.IntegerField(default=0)
