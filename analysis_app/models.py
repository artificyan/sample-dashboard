from django.db import models
from django.utils import timezone

class Trips(models.Model):

	id = models.AutoField(primary_key=True)
	trip_id = models.IntegerField()
	date = models.DateField()
	retailer = models.CharField(max_length=50)
	brand = models.CharField(max_length=50)
	user_id = models.CharField(max_length=20)
	item_spend = models.IntegerField()
	item_units = models.IntegerField()

	def publish(self):
	    self.save()

	def __str__(self):
	    return str(self.id)