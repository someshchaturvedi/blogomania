from __future__ import unicode_literals
from django.db import models
class blog_item(models.Model):
	cog_id = models.CharField(max_length = 10 , unique=True)
	title=  models.CharField(max_length=100 , null=True)
	text =  models.TextField(null=True)
	def __str__(self):
		return(self.cog_id)

