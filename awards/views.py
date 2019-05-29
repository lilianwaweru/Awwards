from django.shortcuts import render,redirect
from .models import Profile,Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,VoteForm,EditProfile
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer


# Create your views here.
def welcome(request):
    projects = Project.objects.all()
    prof = Profile.objects.filter(user=request.user)
    return render(request,'welcome.html',{"projects":projects,"prof":prof})


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

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    logged_user = request.user
    if request.method == 'POST':
        form = EditProfile(request.POST,request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = logged_user
            edit.save()
        return redirect('welcome')

    else:
        
        form = EditProfile()

    return render(request,'profile.html',{'form':form})


class project_list(APIView):
    def get(self, request, format=None):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)


class profile_list(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)
        