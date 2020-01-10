from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
from school.models import Schoolinfo
from teacher.models import Teacherinfo
from classstatd.models import Classstatinfo
from material.models import *
# Create your models here.
User = settings.AUTH_USER_MODEL

class ClassQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte=now)  #lte = less than equal

	def search(self, query=None):
		lookup = (
				Q(class_id__icontains=query) |
				Q(content__icontains=query) |
				  Q(slug__icontains=query) |
				  Q(user__first_name__icontains=query) |
				  Q(user__last_name__icontains=query) |
				  Q(user__username__icontains=query))
		return self.filter(lookup)


class ClassManager(models.Manager):
	def get_queryset(self):
		return ClassQuerySet(self.model, using=self._db)
	def published(self):
		return self.get_queryset().published()
	def search(self, query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().published().search(query)


class Classinfo(models.Model):
	def __str__(self):
		return str(self.class_id)+'  '+str(self.class_sch)+'  '+str(self.class_stat)
	user = models.ForeignKey(User, default=1, null=True,  on_delete=models.SET_NULL)
	class_id = models.CharField(null=True, blank=True, max_length=120)
	class_date = models.DateField(auto_now=False, blank=True, auto_now_add=False, null=True, )
	class_cate = models.CharField(null=True, blank=True,max_length=120)
	class_stat = models.CharField(null=True, blank=True,max_length=120)
	class_statkey = models.ForeignKey(Classstatinfo, on_delete=models.CASCADE, null=True, blank=True)
	class_stunum = models.CharField(null=True, blank=True,max_length=120)
	class_time = models.CharField(null=True, blank=True,max_length=120)
	class_place = models.CharField(null=True, blank=True,max_length=120)
	class_count = models.IntegerField(null=True, blank=True, default=1)
	class_sch = models.CharField(null=True, blank=True,max_length=120)
	class_schkey = models.ForeignKey(Schoolinfo, on_delete=models.CASCADE, null=True, blank=True)
	class_tea = models.CharField(null=True, blank=True,max_length=120)
	class_teakey = models.ForeignKey(Teacherinfo, on_delete=models.CASCADE, null=True,blank=True)
	memo = models.CharField(null=True, blank=True,max_length=120)

	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	class_cont_call = models.BooleanField(default=False)
	class_cont_email = models.BooleanField(default=False)
	class_cont_message = models.BooleanField(default=False)

	class_ready = models.BooleanField(default=False)
	class_taken = models.BooleanField(default=False)
	class_done = models.BooleanField(default=False)
	class_re_done = models.BooleanField(default=False)
	class_doc_plan = models.BooleanField(default=False)
	class_doc_preestim = models.BooleanField(default=False)
	class_doc_tea = models.BooleanField(default=False)
	class_doc_finestim = models.BooleanField(default=False)
	class_cal_meth = models.CharField(null=True, blank=True,max_length=120)
	class_deposit_check = models.BooleanField(default=False)
	

	objects = ClassManager()


class dyna_mat_rel(models.Model):
	def __str__(self):
		return str(self.dyna_mat.class_id) + "----" + str(self.dyna_mat.class_statkey.class_title) + "----" + str(self.mat_dyna.mat_name)
	dyna_mat = models.ForeignKey(Classinfo, on_delete=models.CASCADE, null=True, blank=True)
	dyna_mat_num = models.CharField(null=True, blank = True, max_length = 120, default="수량을 입력해주세요")
	mat_dyna = models.ForeignKey(Materialinfo, on_delete=models.CASCADE, null=True, blank=True)
	mat_order_done = models.BooleanField(default=False)
	mat_deliver_done = models.BooleanField(default=False)
	mat_manu_done = models.BooleanField(default=False)
	mat_div_done = models.BooleanField(default=False)



class dyna_tool_rel(models.Model):
	def __str__(self):
		return str(self.dyna_tool.class_id) + "----" + str(self.dyna_tool.class_statkey.class_title) + "----" + str(self.tool_dyna.tool_name)
	dyna_tool = models.ForeignKey(Classinfo, on_delete=models.CASCADE, null=True, blank=True)
	dyna_tool_num = models.CharField(null=True, blank = True, max_length = 120)
	tool_dyna = models.ForeignKey(Toolinfo, on_delete=models.CASCADE, null=True, blank=True)
	tool_re = models.BooleanField(default=False)