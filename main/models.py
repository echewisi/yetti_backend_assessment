from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    person= models.OneToOneField(User, on_delete= models.CASCADE, null= True, blank= True)

# Create your models here.
