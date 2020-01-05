from django.urls import path
from .views import *

urlpatterns = [
    path('', material_table),
    path('create/', material_create_view),
    path('<str:mat_name>/delete/', material_delete_view),
    path('<str:mat_name>/update/', material_update_view),
    path('tool/', tool_table),
    path('tool/create/', tool_create_view),
    path('tool/<str:tool_name>/delete/', tool_delete_view),
    path('tool/<str:tool_name>/update/', tool_update_view),
]
