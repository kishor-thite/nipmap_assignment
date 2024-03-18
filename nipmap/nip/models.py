from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Client(models.Model):

    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    assigned_users = models.ManyToManyField(User, related_name='assigned_projects')  # Updated related_name
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')  # Updated related_name

    def __str__(self):
        return self.project_name