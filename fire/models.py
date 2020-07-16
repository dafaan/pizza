from django.db import models

# Create your models here.

#class sign(models.Model):
#    username = models.CharField(max_length=150)
#    email = models.EmailField()
#    password = models.CharField(max_length=150)
#    confirm_password = models.CharField(max_length=150)
#    city = models.CharField(max_length=150)
#    address = models.CharField(max_length=150)

class menu_list(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=150)
    price = models.IntegerField()


class re(models.Model):
    desc = models.CharField(max_length=200)
    name = models.CharField(max_length=200)