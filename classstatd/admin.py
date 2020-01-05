from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Classstatinfo)
admin.site.register(stat_mat_rel)
admin.site.register(stat_tool_rel)