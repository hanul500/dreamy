from django import forms
from .models import *
from school.models import Schoolinfo
from teacher.models import Teacherinfo
from classstatd.models import *


class ClassForm(forms.Form):
	#class_id = forms.CharField()
	class_date = forms.DateField()
	#class_schkey = forms.ModelChoiceField(queryset=Schoolinfo.objects.all(),initial=0,label="class_schkey")

	class_cate = forms.CharField()
	#class_statkey = forms.ModelChoiceField(queryset=Classstatinfo.objects.all(),initial=0,label="class_statkey")

	#class_teakey = forms.ModelChoiceField(queryset=Teacherinfo.objects.all(),initial=0,label="class_teakey")
	class_sch = forms.CharField()
	class_tea = forms.CharField()
	class_stat = forms.CharField()



	class_count = forms.IntegerField()
	class_stunum = forms.CharField()
	class_time = forms.CharField()
	class_place = forms.CharField()
	memo = forms.CharField()
	class_ready = forms.BooleanField()
	class_taken = forms.BooleanField()
	class_done = forms.BooleanField()
	class_doc_plan = forms.BooleanField()
	class_doc_preestim = forms.BooleanField()
	class_doc_tea = forms.BooleanField()
	class_doc_finestim = forms.BooleanField()
	class_cal_meth = forms.CharField()
	class_deposit_check = forms.BooleanField()


class dyna_mat_relForm(forms.Form):
	dyna_mat_num = forms.CharField()
	mat_order_done = forms.BooleanField()
	mat_deliver_done = forms.BooleanField()
	mat_manu_done = forms.BooleanField()
	mat_div_done = forms.BooleanField()





class ClassModelForm(forms.ModelForm):
	class Meta:
		model = Classinfo
		fields = ['class_date','class_sch','class_cate', 'class_stat', 'class_tea','class_count','class_stunum','class_time','class_place','memo']

	def clean_title(self, *args, **kwargs):
		instance = self.instance
		print(instance)
		print("cleantitle")
		class_time = self.cleaned_data.get('class_time')
		qs = Class.objects.filter(class_time__iexact=class_time)
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():  #중복 방지
			raise forms.ValidationError("This title has already been used.")
		return class_time



class ClassTableCheckForm(forms.ModelForm):
	class Meta:
		model = Classinfo
		fields = ['memo', 'class_ready','class_taken','class_done','class_re_done','class_cont_call','class_cont_email','class_cont_message', 'class_doc_plan',
		'class_doc_preestim','class_doc_tea','class_doc_finestim','class_cal_meth',
		'class_deposit_check']

class dynamatTableCheckForm(forms.ModelForm):
	class Meta:
		model = dyna_mat_rel
		fields = ['mat_deliver_done', 'mat_order_done','mat_manu_done','mat_div_done','dyna_mat_num']
