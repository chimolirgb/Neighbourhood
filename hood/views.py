

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile,Category
from .forms import ProfileForm,UpdateUserProfileForm,UpdateUserForm,CategoryForm,PostForm,BusinessForm,PostForm

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer
from .models import *
import datetime as dt


# Create your views here.


def index(request):
    date = dt.date.today()
    hoods = Neighbourhood.objects.all()
    return render(request, 'index.html',{"date":date, "hoods":hoods})

    

def category(request):
    if request.method == 'POST':
        form =CategoryForm(request.POST,request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user.profile
            category.save()
        return redirect('/')
    else:
        form =CategoryForm()

    return render(request,'categories.html',{'form':form})
   

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('Index')
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile(request,username):
 
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        # 'projects': projects,
    }
    return render(request, 'profile.html',params)



@login_required(login_url='/accounts/login/')
def hoods(request,id):
    date = dt.date.today()
    post=Neighbourhood.objects.get(id=id)
    brushs = Post.objects.filter(neighbourhood=post)
    business = Business.objects.filter(neighbourhood=post)
    return render(request,'each_hood.html',{"post":post,"date":date,"brushs":brushs, "business":business})

@login_required(login_url='/accounts/login/')
def new_hood(request,id):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = Neighbourhood(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.profile = profile
            hood.save()
        return redirect('index')
    else:
        form = Neighbourhood()
    return render(request, 'new_hood.html', {"form": form})

def maps(request):
    date = dt.date.today()
    return render(request, 'maps.html',{"date":date})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.objects.filter(name=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all( )

        return render(request, 'search.html',{"message":message,"business": searched_businesses,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def post_new(request,id):
    date = dt.date.today()
    hood=Neighbourhood.objects.get(id=id)
    posts = Post.objects.filter(neighbourhood=hood)
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.profile = profile
            post.neighbourhood = hood
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request,'new_post.html',{"form":form,"posts":posts,"hood":hood,  "date":date})

def post_business(request,id):
    date = dt.date.today()
    hood=Neighbourhood.objects.get(id=id)
    business = Business.objects.filter(neighbourhood=hood)
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.profile = request.user.profile
            business.neighbourhood = hood
            business.save()
            return redirect('index')
    else:
        form = BusinessForm()
        return render(request,'new_business.html',{"form":form,"business":business,"hood":hood,  "date":date})


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category(category_name=form.cleaned_data.get('category_name'),
                        user=request.user)
            category.save()
            return redirect('welcome')
        else:
            return render(request, 'addcategory.html', {'form': form})
    else:
        form = CategoryForm()
        return render(request, 'addcategory.html', {'form': form})




def logout(request):
    logout(request)
    return redirect('login')

