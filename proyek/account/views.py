from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login
from .models import User, DataProject, Pesan
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    msg= None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user dibuat'
            return redirect('program:index')
        else:
            msg = 'form tidak valid'
    else:
        form = SignUpForm()
    return render(request,'register.html',{'form':form,'msg':msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method =='POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('program:adminpage')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request,'login.html',{'form':form,'msg':msg})

def admin(request):
    data_projects = DataProject.objects.all()
    return render(request,'account/admin.html',{'object_list':data_projects})

class IndexProject(ListView):
    queryset = DataProject.objects.all()
class TambahProject(CreateView):
    model = DataProject
    fields ='__all__'
    success_url = reverse_lazy('program:adminpage')
class DetailProject(DetailView):
    model = DataProject
class UpdateProject(UpdateView):
    model = DataProject
    fields ='__all__'
    success_url = reverse_lazy('program:adminpage')
class DeleteProject(DeleteView):
    model = DataProject
    fields ='__all__'
    success_url = reverse_lazy('program:adminpage')

# pesanan
class IndexPesan(ListView):
    queryset = Pesan.objects.all()
class TambahPesan(CreateView):
    model = Pesan
    fields='__all__'
    success_url = reverse_lazy('program:konten')