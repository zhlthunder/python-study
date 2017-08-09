from django.db import models

class User(models.Model):
	name=models.CharField(max_length=30)
	headimg=models.FileField(upload_to='./upload/')
	
	def __unicode__(self):
		return self.name
