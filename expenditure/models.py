from django.db import models
from django.contrib.auth.models import User

class Expenditure(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	price = models.FloatField(null=True, blank=True, default=None)

	def __str__(self):
		return self.name