from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from .models import *
from .forms import *
from school.models import *
from classstatd.models import *
from teacher.models import *

# Create your views here.


def class_home(request):
	qs = Classinfo.objects.all()
	context = {'title':'class information','object_list': qs}
	return render(request, 'class/class_table.html', context)

def class_create_view(request):
	form = ClassModelForm(request.POST or None, request.FILES or None)
	sch_obj=Schoolinfo.objects.all()
	classstat_obj=Classstatinfo.objects.all()
	tea_obj=Teacherinfo.objects.all()
	stat_mat_obj=stat_mat_rel.objects.all()
	stat_tool_obj=stat_tool_rel.objects.all()

	print("form created")
	if form.is_valid():
		print("form valid!")
		obj = form.save(commit=False)
		obj.user = request.user
		obj.class_schkey=Schoolinfo.objects.all().filter(sch_name=obj.class_sch)[0]
		obj.class_teakey=Teacherinfo.objects.all().filter(tea_name=obj.class_tea)[0]
		obj.class_statkey=Classstatinfo.objects.all().filter(class_title=obj.class_stat)[0]
		stat_mat_filtered = stat_mat_obj.filter(stat_mat=obj.class_statkey)
		stat_tool_filtered = stat_tool_obj.filter(stat_tool=obj.class_statkey)
		obj.class_id = "C"+'%06d'%len(Classinfo.objects.all())
		obj.save()
		for i in range(len(stat_mat_filtered)):
			dyna_mat_obj = dyna_mat_rel()
			dyna_mat_obj.dyna_mat = obj
			dyna_mat_obj.dyna_mat_num = stat_mat_filtered[i].stat_mat_num
			dyna_mat_obj.mat_dyna = stat_mat_filtered[i].mat_stat
			print(dyna_mat_obj.mat_dyna.mat_name)
			dyna_mat_obj.save()
		for j in range(len(stat_tool_filtered)):
			dyna_tool_obj = dyna_tool_rel()
			dyna_tool_obj.dyna_tool = obj
			dyna_tool_obj.dyna_tool_num = stat_tool_filtered[j].stat_tool_num
			dyna_tool_obj.tool_dyna = stat_tool_filtered[j].tool_stat
			dyna_tool_obj.save()
			print(dyna_tool_obj.tool_dyna.tool_name)
		
		form = ClassModelForm()
	template_name = 'class/class_create.html'
	context = {'form': form, 'sch_obj':sch_obj, 'classstat_obj':classstat_obj, 'tea_obj':tea_obj}
	return render(request, template_name, context)

def class_detail_view(request, class_id):
	# 1 object -> detail view
	obj = get_object_or_404(Classinfo, class_id=class_id)
	template_name = 'class/prgwin.html'
	context = {"class_obj": obj, "sch_obj": obj.class_schkey, "sch_obj": obj.class_schkey,}
	return render(request, template_name, context)


def class_update_view(request, class_id):
	# 1 object -> detail view
	obj = get_object_or_404(Classinfo, class_id=class_id)
	form = ClassModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'class/class_form.html'
	context = {'form': form}
	return render(request, template_name, context)


def class_delete_view(request,class_id):
	obj = get_object_or_404(Classinfo, class_id=class_id)
	template_name = 'class/class_delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/class")
	context = {"object": obj}
	return render(request, template_name, context)

def class_sch_queryinput(request):
	class_obj = Classinfo.objects.all()
	sch_obj = Schoolinfo.objects.all()
	for i in class_obj:
		for j in sch_obj:
			if i.class_sch == j.sch_name:
				i.class_schkey=j
				i.save()
				print(j.sch_name)
				print(type(j))
				print(type(i.class_schkey))
	return render(request, "home.html", {"object":class_obj})
