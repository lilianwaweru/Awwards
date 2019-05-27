from django.shortcuts import render,redirect
from .models import Profile,Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm

# Create your views here.
def welcome(request):
    projects = Project.objects.all()
    return render(request,'welcome.html',{"projects":projects})


@login_required(login_url='/accounts/login/')
def ProjectsUpload(request):
    logged_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            ProjectsUpload = form.save(commit=False)
            ProjectsUpload.Project = logged_user
            ProjectsUpload.save()
            return redirect('welcome')

    else:
         form = ProjectForm()

    return render(request,'project.html',{'form':form})           


@login_required(login_url='/accounts/login/')
def review(request):
    logged_user = request.user
    if request.method == 'POST':
        form = VoteForm(request.POST,request.FILES)
        if form.is_valid():
        review = form.save(commit=False)
        review.Project = logged_user
        review.save()
        return redirect('welcome')

    else:
        form =  VoteForm()

    return render(request,'review.html',{'form':form})
             
    