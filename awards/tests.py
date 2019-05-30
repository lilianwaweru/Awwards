from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Project

# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user()
        self.new_profile = Profile(user=self.user,bio='Test Bio',contact='0712345678')
        self.new_profile.save_profile()
        self.new_project = Project(title='title',description='description',link='http://awards',project_user=self.project_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

    def test_save_instance(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_profile(self):
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==


class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user()
        self.profile = Profile(user=self.user,bio='Bio',contact='0712345678')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
