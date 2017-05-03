from django.db import models

# Create your models here.
class join(models.Model):
	email = models.CharField(max_length=50)
	passwd = models.CharField(max_length=50)
	nick = models.CharField(max_length=20)
	birth = models.IntegerField()

	def __str__(self):
		return self.email