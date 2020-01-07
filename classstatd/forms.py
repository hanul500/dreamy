from django import forms
from .models import *


class ClassstatForm(forms.Form):
	class_code = models.CharField()
	class_title = models.CharField()
	class_minicate = models.CharField()
	class_detail = models.TextField()


class ClassstatModelForm(forms.ModelForm):
	class Meta:
		model = Classstatinfo
		fields = ['class_title', 'class_minicate', 'class_detail']

