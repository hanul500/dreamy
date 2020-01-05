from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone

# Create your models here.

class TeacherQuerySet(models.QuerySet):
	#def published(self):
	#    now = timezone.now()
	#    return self.filter(publish_date__lte=now)  #lte = less than equal

	def search(self, query=None):
		lookup = (
	#            Q(title__icontains=query) |
	#            Q(content__icontains=query) |
	#              Q(slug__icontains=query) |
	#              Q(user__first_name__icontains=query) |
	#              Q(user__last_name__icontains=query) |
				  Q(user__username__icontains=query))
		return self.filter(lookup)

class Teacherinfo(models.Model):
	def __str__(self):
		return self.tea_name
	tea_id = models.CharField(null=True, blank=True ,max_length=120)
	tea_name = models.CharField(null=True, blank=True ,max_length=120)
	tea_email = models.CharField(null=True, blank=True ,max_length=120)
	tea_tel = models.CharField(null=True, blank=True ,max_length=120)
	tea_adress = models.CharField(null=True, blank=True ,max_length=120)
	tea_bankacc = models.CharField(null=True, blank=True ,max_length=120)
	tea_bankname = models.CharField(null=True, blank=True ,max_length=120)
	#timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)





class TeacherManager(models.Manager):
	def get_queryset(self):
		return TeacherQuerySet(self.model, using=self._db)

	#def published(self):
	#    return self.get_queryset().published()

	#def search(self, query=None):
	#    if query is None:
	#        return self.get_queryset().none()
	#    return self.get_queryset().published().search(query)
