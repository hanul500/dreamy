from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from .models import *
from .forms import *


# Create your views here.
def material_table(request):
	qs = Materialinfo.objects.all()
	context = {'title':'material information','object_list': qs}
	return render(request, 'material/mattable.html', context)

def tool_table(request):
	qs = Toolinfo.objects.all()
	context = {'title':'Tool information','object_list': qs}
	return render(request, 'material/tooltable.html', context)


def material_create_view(request):
	form = MaterialModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():

		obj = form.save(commit=False)
		obj.user = request.user
		obj.mat_id = "M"+'%06d'%len(Materialinfo.objects.all())
		obj.save()
		form = MaterialModelForm()
	template_name = 'material/create_mat.html'
	context = {'form': form}
	return render(request, template_name, context)


def tool_create_view(request):
	form = ToolModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.tool_id = "T"+'%06d'%len(Toolinfo.objects.all())
		obj.save()
		form = ToolModelForm()
	template_name = 'material/create_tool.html'
	context = {'form': form}
	return render(request, template_name, context)

def material_update_view(request, mat_id):
	# 1 object -> detail view
	obj = get_object_or_404(Materialinfo, mat_id=mat_id)
	form = MaterialModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'material/create_mat.html'
	context = {'form': form}
	return render(request, template_name, context)

def tool_update_view(request, tool_id):
	# 1 object -> detail view
	obj = get_object_or_404(Toolinfo, tool_id=tool_id)
	form = ToolModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'material/create_tool.html'
	context = {'form': form}
	return render(request, template_name, context)

def material_delete_view(request,mat_id):
	obj = get_object_or_404(Materialinfo, mat_id=mat_id)
	template_name = 'material/delete_mat.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/material/")
	context = {"object": obj}
	return render(request, template_name, context)

def tool_delete_view(request,tool_id):
	obj = get_object_or_404(Toolinfo, tool_id=tool_id)
	template_name = 'material/delete_tool.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/material/")
	context = {"object": obj}
	return render(request, template_name, context)