from django import forms
from .models import Project,Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['usability','design','content']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['title','description','landing_page','link']        


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['project','user']

