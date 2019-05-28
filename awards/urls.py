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
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
