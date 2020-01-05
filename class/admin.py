from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Classinfo)
admin.site.register(dyna_mat_rel)
admin.site.register(dyna_tool_rel)