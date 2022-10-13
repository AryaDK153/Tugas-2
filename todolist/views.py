from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from todolist.models import Task
from todolist.forms import AddTaskForm
from django.contrib.auth.models import User

# from LAB03
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# Registration Form
def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
        else:
                messages.info(request, 'Periksa kembali input anda!')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# Login Function
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:task")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
            # login(request, user)
            # return redirect('todolist:task')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Logout Function
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:lobby'))
    response.delete_cookie('last_login')
    return response
    # logout(request)
    # return redirect('todolist:login')

# New Task Function
@login_required(login_url='/todolist/login/')
def new_task(request):
    form = AddTaskForm()

    if request.method == "POST":
        uid = request.user.id
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title !="" and description !="":
            Task.objects.create(user = User.objects.get(pk = uid), title=title, description=description)
            return redirect('todolist:task')
        else:
            messages.info(request, 'Judul atau Deskripsi tidak boleh kosong!')

    context = {'form' : form}
    return render(request, 'new_task.html', context)


# Todolist
@login_required(login_url='/todolist/login/')
def show_task(request):
    task_list = Task.objects.filter(user=request.user.id)
    print(task_list)
    context = {
        'user': request.user.get_username,
        'task_list': task_list,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

# Lobby
def show_todolist_lobby(request):
    context = {
        'nama' : 'Arya Daniswara Khairan',
        'id' : '2106702781',
    }
    return render(request, "lobby.html", context)

def todolist_json(request):
    data = Task.objects.filter(user=request.user.id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def new_task_instant(request):
    if request.method == "POST":
        uid = request.user.id
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title !="" and description !="":
            Task.objects.create(user = User.objects.get(pk = uid), title=title, description=description)
            return HttpResponse(b"CREATED", status=201)
        else:
            messages.info(request, 'Judul atau Deskripsi tidak boleh kosong!')
            return HttpResponseNotFound()
    return HttpResponseNotFound()