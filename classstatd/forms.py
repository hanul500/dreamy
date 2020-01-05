from django import forms
from .models import *


class ClassstatForm(forms.Form):
	class_code = models.CharField()
	recipe_cate = models.CharField()
	class_title = models.CharField()
	class_minicate = models.CharField()
	class_detail = models.TextField()


class ClassstatModelForm(forms.ModelForm):
	class Meta:
		model = Classstatinfo
		fields = ['recipe_cate', 'class_title', 'class_minicate', 'class_detail']

