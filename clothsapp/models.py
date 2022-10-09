from django.db import models

# Create your models here.

#table for home page
class home_table(models.Model):

    img = models.ImageField(upload_to='home_pix')
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    disc = models.TextField()

    # it is used to rename objects. for excample if the below "objects" is "home"
    #then when you query database it will be like this home_table.home.all().
    objects = models.Manager()

#table for about us page
class about_us_table(models.Model):
    employ_img = models.ImageField(upload_to='about_us_pix')
    employ_name = models.CharField(max_length=50)
    employ_position = models.CharField(max_length=100)
    employ_disc = models.TextField()

    objects = models.Manager()

#creating gallery
class gallery(models.Model):
    gallery = models.ImageField(upload_to='galary')
    objects = models.Manager()
