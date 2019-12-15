from django.db import models
from datetime import datetime  

# Create your models here.
class List(models.Model):
	item = models.CharField(max_length = 200)
	#completed = models.BooleanField(default=False)
	gram = models.IntegerField(default = 100)
	calories = models.IntegerField(default = 100)
	datetime = models.DateTimeField(default=datetime.now, blank=True)
    
    # showing data 
	def __str__(self):
		return self.item



