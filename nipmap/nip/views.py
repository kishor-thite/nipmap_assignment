from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Client, Project
from .forms import ClientForm, ProjectForm
from django.http import JsonResponse



def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_detail(request):
    clients = Client.objects.all()
    return render(request, 'client_detail.html', {'clients': clients})

@login_required
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()
            messages.success(request, 'Client registered successfully.')
            return redirect('client_detail')
    else:
        form = ClientForm()
    return render(request, 'register_client.html', {'form': form})

@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client information updated successfully.')
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form, 'client': client})

@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client deleted successfully.')
        return redirect('client_list')
    return render(request, 'delete_client.html', {'client': client})

@login_required
def add_project(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = client
            project.created_by = request.user
            project.save()
            form.save_m2m()  # Save many-to-many relationships
            messages.success(request, 'Project added successfully.')
            return redirect('client_list')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form, 'client': client})

@login_required
def assigned_projects(request):
    projects = Project.objects.filter(assigned_users=request.user)
    return render(request, 'Creted_projects.html', {'projects': projects})

@login_required
def assigned_to(request):
    projects = Project.objects.filter(assigned_users=request.user)
    return render(request, 'Asign_to.html', {'projects': projects})

@login_required
def get_projects_for_client(request, client_id):
    # Retrieve the client object based on the client_id
    client = get_object_or_404(Client, id=client_id)

    # Query all projects assigned to the client
    projects = Project.objects.filter(client=client)

    # Serialize the projects data if needed
    project_data = [{'id': project.id, 'project_name': project.project_name} for project in projects]

    # Return the projects data as JSON response
    return JsonResponse({'projects': project_data})