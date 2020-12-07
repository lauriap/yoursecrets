from django.db import models
from django.contrib.auth.models import User

class Secret(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	secret = models.TextField()

	def __str__(self):
		return self.secret