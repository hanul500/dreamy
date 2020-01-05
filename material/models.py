from django.db import models

# Create your models here.
class Materialinfo(models.Model):
	def __str__(self):
		return self.mat_name
	mat_id = models.CharField(null=True, blank=True ,max_length=120)
	mat_name = models.CharField(null=True, blank=True ,max_length=120)
	mat_shop = models.CharField(null=True, blank=True ,max_length=120)
	mat_price = models.CharField(null=True, blank=True ,max_length=120)
	mat_loc = models.CharField(null=True, blank=True ,max_length=120)
	mat_inven = models.CharField(null=True, blank=True ,max_length=120)
	

class Toolinfo(models.Model):
	def __str__(self):
		return self.tool_name
	tool_id = models.CharField(null=True, blank=True ,max_length=120)
	tool_name = models.CharField(null=True, blank=True ,max_length=120)
	tool_shop = models.CharField(null=True, blank=True ,max_length=120)
	tool_price = models.CharField(null=True, blank=True ,max_length=120)
	tool_loc = models.CharField(null=True, blank=True ,max_length=120)
	tool_inven = models.CharField(null=True, blank=True ,max_length=120)
	