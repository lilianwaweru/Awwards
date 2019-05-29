from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'posts/$',views.welcome,name = 'welcome'),
    url(r'^project/$',views.ProjectsUpload,name = 'ProjectForm'),
    url(r'^review/$',views.review, name = 'VoteForm'),
    url(r'^profile/$',views.edit_profile, name = 'EditProfile'),
    url(r'^api/profile/$', views.profile_list.as_view()),
    url(r'^api/projects/$', views.project_list.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
