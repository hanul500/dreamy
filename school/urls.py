from django.urls import path
from .views import *

urlpatterns = [

    path('', School_table),
    #path('create/', class_create_view),

]
