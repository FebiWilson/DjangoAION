from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=50)
    Image = models.ImageField(upload_to="app1_manager/images", default="")
    User = models.ForeignKey(User, on_delete=models.CASCADE)

