from django import forms
from .models import *


class MaterialForm(forms.Form):
	mat_id = forms.CharField()
	mat_name = forms.CharField()
	mat_shop = forms.CharField()
	mat_price = forms.CharField()
	mat_loc = forms.CharField()
	mat_inven = forms.CharField()


class ToolForm(forms.Form):
	tool_id = forms.CharField()
	tool_name = forms.CharField()
	tool_shop = forms.CharField()
	tool_price = forms.CharField()
	tool_loc = forms.CharField()
	tool_inven = forms.CharField()





class MaterialModelForm(forms.ModelForm):
	class Meta:
		model = Materialinfo
		fields = ['mat_name', 'mat_shop', 'mat_shop', 'mat_price','mat_loc', 'mat_inven']


class ToolModelForm(forms.ModelForm):
	class Meta:
		model = Toolinfo
		fields = ['tool_id','tool_name', 'tool_shop', 'tool_shop', 'tool_price','tool_loc', 'tool_inven']
