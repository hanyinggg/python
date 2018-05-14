from django.db import models
from django.contrib.auth.models import User

class Heros(models.Model):
	name = models.CharField(max_length = 50)
	img = models.ImageField(upload_to='', blank=True)
	attr = models.TextField()
	background = models.TextField()
	talent = models.TextField()

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('dota2_data:detail',kwargs={'pk':self.pk})

class Skills(models.Model):
	name = models.CharField(max_length = 50)
	logo =models.ImageField(upload_to='', blank=True)
	detail = models.TextField()
	heros  = models.ForeignKey(Heros, on_delete=models.CASCADE)
	def __str__(self):
		return self.name


class Items(models.Model):
	name = models.CharField(max_length = 50)
	logo = models.ImageField(upload_to='', blank=True)
	price = models.IntegerField()
	intro = models.TextField()
	detail = models.TextField()
	def __str__(self):
		return self.name

# Create your models here.
