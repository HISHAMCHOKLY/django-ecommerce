from django.db import models

# Create your models here.

class Brands(models.Model):
    b_name=models.CharField(max_length=200)
    b_img=models.ImageField(upload_to='pics')
