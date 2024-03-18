from django.urls import path
from nip import views
from django.contrib import admin

urlpatterns = [
    path('', views.client_detail, name='client_detail'),
    path('register-client/', views.register_client, name='register_client'),
    path('edit-client/<int:client_id>/', views.edit_client, name='edit_client'),
    path('delete-client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('add-project/<int:client_id>/', views.add_project, name='add_project'),
    path('assigned-projects/', views.assigned_projects, name='assigned_projects'),
    path('assigned-to/', views.assigned_to, name='assigned_to'),
    path('admin/', admin.site.urls),
    path('client/<int:client_id>/projects/', views.get_projects_for_client, name='client'),
]