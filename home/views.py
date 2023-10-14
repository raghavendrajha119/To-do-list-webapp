from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact,Note
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request,'index.html')
def registerUser(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password1=form.cleaned_data.get('password1') #for first time
            password2=form.cleaned_data.get('password2') #for check password again
            print(username,password1)
            user=authenticate(username=username,password=password1)
            login(request,user)
            return redirect("/")
        else:
            print(form.errors)
            return render(request,'register.html',{'form':form})
    else:
        form = UserCreationForm()
        return render(request,'register.html', {'form': form})                                  
def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact =  Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        
    return render (request,'contact.html')
class NoteList(ListView):
    model= Note
    template_name='home/note_list.html'
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
class NoteView(DetailView):
    model = Note
    template_name = 'home/note_view.html'
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
class NoteCreate(CreateView):
    model=Note
    template_name = 'home/note_new.html'
    fields=['Task','Reminder','Date']
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url=reverse_lazy('note_list')
class NoteUpdate(UpdateView):
    model = Note
    template_name='home/note_edit.html'
    fields = ['Task', 'Reminder','Date']
    success_url = reverse_lazy('note_list')
class NoteDelete(DeleteView):
    model = Note
    template_name='home/note_delete.html'
    success_url = reverse_lazy('note_list')