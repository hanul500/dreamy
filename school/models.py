from django.db import models

# Create your models here.


class SchoolQueryset(models.QuerySet):
	pass

class SchoolManager(models.Manager):
	pass

class Schoolinfo(models.Model):
	def __str__(self):
		return str(self.sch_name)
	sch_code = models.CharField(null=True, blank=True ,max_length=120)
	sch_id = models.CharField(null=True, blank=True ,max_length=120)
	sch_name = models.CharField(null=True, blank=True ,max_length=120)
	sch_email = models.CharField(null=True, blank=True ,max_length=120)
	sch_address = models.CharField(null=True, blank=True ,max_length=120)
	sch_tel = models.CharField(null=True, blank=True ,max_length=120)


class Schoolteainfo(models.Model):
	schtea_id = models.CharField(null=True, blank=True ,max_length=120)
	schtea_name = models.CharField(null=True, blank=True ,max_length=120)
	schtea_email = models.CharField(null=True, blank=True ,max_length=120)
	schtea_pos = models.CharField(null=True, blank=True ,max_length=120)
	schtea_tel1 = models.CharField(null=True, blank=True ,max_length=120)
	schtea_tel2 = models.CharField(null=True, blank=True ,max_length=120)
	schtea_tel3 = models.CharField(null=True, blank=True ,max_length=120)
	schtea_schkey = models.ForeignKey(Schoolinfo, on_delete=models.CASCADE, null=True,blank=True)