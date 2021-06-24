from django.db import models
from django.contrib.auth.models import AbstractUser




 
class Lead(models.Model):

    first_name = models.CharField(max_lenght=20)
    last_name = models.CharField(max_lenght=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


class Agent(model.Model):
    user = models.OneToOneFiled(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_lenght=20)
    last_name = models.CharField(max_lenght=20)