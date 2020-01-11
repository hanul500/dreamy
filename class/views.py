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

@login_required
def class_home(request):
	qs = Classinfo.objects.all()
	


	context = {'title':'class information','object_list': qs}
	return render(request, 'class/class_table.html', context)

@login_required
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
		obj.class_id = "C"+ "%06d"%(int(Classinfo.objects.all()[len(Classinfo.objects.all())-1].class_id[1:])+1)
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

@login_required
def class_detail_view(request, class_id):
	obj = get_object_or_404(Classinfo, class_id=class_id)
	mat_obj = list(dyna_mat_rel.objects.all().filter(dyna_mat=obj))
	tool_obj = list(dyna_tool_rel.objects.all().filter(dyna_tool=obj))
	form_class = ClassTableCheckForm(request.POST or None, instance=obj)
	if form_class.is_valid():
		for i in range(len(dyna_mat_rel.objects.all().filter(dyna_mat=obj))):
			
			if request.POST.get('mat_deliver_done%d'%(i+1))==None:
				mat_obj[i].mat_deliver_done = False
			else:
				mat_obj[i].mat_deliver_done = True
			if request.POST.get('mat_order_done%d'%(i+1))==None:
				mat_obj[i].mat_order_done = False
			else:
				mat_obj[i].mat_order_done = True
			mat_obj[i].dyna_mat_num=request.POST.get('dyna_mat_num%d'%(i+1))

			mat_obj[i].save()
			print(request.POST.get(request.POST.get('dyna_mat_num%d'%(i+1))))
			#print(mat_obj[i].mat_deliver_done)

		if obj.class_cont_call or obj.class_cont_message or obj.class_cont_email:
			obj.class_process="수업문의"
			if obj.class_doc_plan or obj.class_doc_preestim or obj.class_doc_tea:
				obj.class_process="서류제출"
				if True:
					obj.class_process="재료주문"
					if True:
						obj.class_process="도착확인"
						if obj.class_done:
							obj.class_process="수업준비"
							if obj.class_ready:
								obj.class_process="재료준비"
								if obj.class_taken:
									obj.class_process="강사수거"
									if obj.class_re_done:
										obj.class_process="도구반납"
										if obj.class_doc_finestim or (obj.class_cal_meth != None):
											if obj.class_deposit_check:
												obj.class_process="완료"
										

		obj.save()
		form_class.save()
			
			
			#for j in range(len(dyna_mat_rel.objects.all().filter(dyna_mat=obj))):
			#	form_mat[j].save()

	template_name = 'class/prgwin.html'
	context = {"class_obj": obj, "sch_obj": obj.class_schkey, "classstat_obj": obj.class_statkey, "mat_obj":dyna_mat_rel.objects.all().filter(dyna_mat=obj),"tool_obj":tool_obj}#"schtea_obj":Schoolteainfo.objects.all().filter(schtea_schkey=obj.class_schkey)[0]}
	#print(dyna_mat_rel.objects.all().filter(dyna_mat=obj)[0].mat_dyna.mat_name)
	return render(request, template_name, context)

@login_required
def class_update_view(request, class_id):
	# 1 object -> detail view
	obj = get_object_or_404(Classinfo, class_id=class_id)
	form = ClassModelForm(request.POST or None, instance=obj)
	sch_obj=Schoolinfo.objects.all()
	classstat_obj=Classstatinfo.objects.all()
	tea_obj=Teacherinfo.objects.all()
	stat_mat_filtered = stat_mat_rel.objects.all().filter(stat_mat=obj.class_statkey)
	stat_tool_filtered = stat_tool_rel.objects.all().filter(stat_tool=obj.class_statkey)
	if form.is_valid():
		if request.POST.get('class_stat') != obj.class_stat:
			list(dyna_mat_obj.filter(dyna_mat=obj)).delete()
			list(dyna_tool_obj.filter(dyna_tool=obj)).delete()
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
		form.save()
	template_name = 'class/class_update.html'
	context = {'form': form, 'obj':obj, 'sch_obj':sch_obj, 'classstat_obj':classstat_obj, 'tea_obj':tea_obj}
	return render(request, template_name, context)

@login_required
def class_delete_view(request,class_id):
	obj = get_object_or_404(Classinfo, class_id=class_id)
	template_name = 'class/class_delete.html'
	if request.method == "POST":
		obj.delete()
		
	context = {"object": obj}
	return render(request, template_name, context)

@login_required
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
