from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    landing_page = models.ImageField(upload_to='landing_pages/',blank=True)


     
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title       






class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'images/',blank=True)
    bio = models.CharField(max_length = 70)
    contact = models.CharField(max_length=12)
    project = models.ForeignKey(Project)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

