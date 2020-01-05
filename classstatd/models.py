from django.db import models
from material.models import *

# Create your models here.
class Classstatinfo(models.Model):
	def __str__(self):
		return self.class_title
	class_code = models.CharField(max_length=120)
	recipe_cate = models.CharField(max_length=120)
	class_title = models.CharField(null=False, blank=True ,max_length=120)
	class_minicate = models.CharField(null=True, blank=True,max_length=120)
	class_detail = models.TextField(null=True, blank=True)

class stat_mat_rel(models.Model):
	def __str__(self):
		return str(self.stat_mat.class_title) + "----" + str(self.mat_stat.mat_name)
	stat_mat = models.ForeignKey(Classstatinfo, on_delete=models.CASCADE, null=True, blank=True)
	mat_stat = models.ForeignKey(Materialinfo, on_delete=models.CASCADE, null=True, blank=True)
	stat_mat_num = models.CharField(null=True, blank = True, max_length = 120)


class stat_tool_rel(models.Model):
	def __str__(self):
		return str(self.stat_tool.class_title) + "----" + str(self.tool_stat.tool_name)
	stat_tool = models.ForeignKey(Classstatinfo, on_delete=models.CASCADE, null=True, blank=True)
	tool_stat = models.ForeignKey(Toolinfo, on_delete=models.CASCADE, null=True, blank=True)
	stat_tool_num = models.CharField(null=True, blank = True, max_length = 120)