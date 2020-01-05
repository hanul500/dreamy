from django.shortcuts import render
from .models import *

# Create your views here.
def School_table(request):
	qs = Schoolinfo.objects.all()
	context = {'title':'School information','object_list': qs}
	return render(request, 'school/schooltable.html', context)

#def School_create_view(request):
#	form = SchoolModelForm(request.POST or None, request.FILES or None)
#	print("form created")
#	if form.is_valid():
#		obj = form.save(commit=False)
#		obj.user = request.user
#		#obj.title = form.cleaned_data.get("title") + "0"
#		obj.save()
#		form = ClassModelForm()
#	template_name = 'class/class_form.html'
#	context = {'form': form}
#	return render(request, template_name, context)
