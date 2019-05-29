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

def vote_project(request, project_id):
    project = Project.objects.get(id=project_id)
    rating = round(((project.design + project.usability + project.content)/3),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            if project.design == 1:
                project.design = int(request.POST['design'])
            else:
                project.design = (project.design + int(request.POST['design']))/2
            if project.usability == 1:
                project.usability = int(request.POST['usability'])
            else:
                project.usability = (project.design + int(request.POST['usability']))/2
            if project.content == 1:
                project.content = int(request.POST['content'])
            else:
                project.content = (project.design + int(request.POST['content']))/2
            project.save()
    else:
        form = VoteForm()
    return render(request,'vote.html',{'form':form,'project':project,'rating':rating})



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


@login_required(login_url='/accounts/login/')
def view_profile(request):
    current_user = request.user
    projects = Project.objects.filter(project_user = current_user)

    try:   
        prof = Profile.objects.get(user=current_user)
    except Exception as e:
        return redirect('EditProfile')

    return render(request,'view_profile.html',{'profile':prof,'projects':projects})


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
        