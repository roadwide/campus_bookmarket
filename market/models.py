from django.db import models
class Market(models.Model):
    username = models.CharField(max_length=128)
    bookname = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    major =models.CharField(max_length=128)
    grade = models.CharField(max_length=128)
    qq = models.CharField(max_length=128)
    pic = models.CharField(max_length=128)
    type=models.CharField(max_length=128)