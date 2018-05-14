from django.db import models
class Strategy(models.Model):
	title = models.CharField(max_length ='100')
	pub_time = models.DateField(auto_now_add=True)
	text = models.TextField()
	
	hero =models.ForeignKey('dota2_data.Heros', on_delete=models.CASCADE)

	def __str__(self):
		return self.title

# Create your models here.
