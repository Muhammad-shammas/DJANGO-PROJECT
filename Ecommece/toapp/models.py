from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pic/customerprofilepic/')
    address=models.CharField(max_length=40)
    mobile=models.IntegerField(max_length=10,null=False)
