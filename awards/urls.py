from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'posts/$',views.welcome,name = 'welcome'),
    url(r'^viewprofile/$',views.view_profile,name ='view_profile'),
    url(r'^project/$',views.ProjectsUpload,name = 'ProjectForm'),
    url(r'^review/$',views.review, name = 'VoteForm'),
    url(r'^profile/$',views.edit_profile, name = 'EditProfile'),
    url(r'^search/', views.search, name='search_title'),
    url(r'^api/profile/$', views.profile_list.as_view()),
    url(r'^api/projects/$', views.project_list.as_view()),
    url(r'^api-token-auth/',obtain_auth_token)
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
