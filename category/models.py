from django.db import models

# Create your models here.

class Categories(models.Model):
    c_name=models.CharField(max_length=200)
    c_img=models.ImageField(upload_to='pics')