from django.urls import path,include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path(r'^create/profile/$',views.create_profile, name='create-profile'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path(r'^api/profiles/$', views.ProfileList.as_view()),

]
    