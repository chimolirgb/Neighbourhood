from django.urls import path,include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path(r'',views.index,name = 'index'),
    #path(r'^signup/$', views.signup, name='signup'),

    path(r'^create/profile/$',views.create_profile, name='create-profile'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path(r'^api/profiles/$', views.ProfileList.as_view()),

    path('category/',views.category,name='category'),
   
    path(r'^hoods/new/post/(\d+)$', views.post_new, name='new-post'),
    path(r'^map$', views.maps, name='maps'),
    path(r'^hoods/new/business/(\d+)$',views.post_business, name='new-business'),
    path(r'^hoods/(\d+)',views.hoods,name='hoods'),
    path(r'^hoods/(\d+)',views.new_hood,name='new-hood'),
    #path(r'^search/', views.search_results, name='search_results'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)