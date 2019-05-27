from django import forms

class ProjectForm(forms.Form):
    model = Profile
    exclude = ['project']


