from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from .models import *
from .forms import *


def classstat_table_view(request):
	pass

def classstat_create_view(request):
	form = ClassstatModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():

		obj = form.save(commit=False)
		obj.user = request.user
		obj.mat_id = "M"+'%06d'%len(Materialinfo.objects.all())
		obj.save()
		form = MaterialModelForm()
	template_name = 'material/create_mat.html'
	context = {'form': form}
	return render(request, template_name, context)
