from django import forms
from django.contrib.auth.models import User
from .models import Profile,Category,Neighbourhood,Post,Business
from .models import *


        
        
class CategoryForm(forms.ModelForm):  
    class Meta:
        model = Category
        fields = ('name','description')


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','name','bio')

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'photo', 'bio']

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'neighbourhood']

class BusinessForm(forms.ModelForm):
    class Meta:
            model = Business
            exclude = ['neighbourhood', 'profile']
