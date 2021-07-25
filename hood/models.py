from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField 
from django.core.validators import MinValueValidator,MaxValueValidator



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    photo = CloudinaryField('image')
    bio = models.CharField(max_length=300)
    name = models.CharField(blank=True, max_length=120)
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)
    neighbourhood = models.ForeignKey('Neighbourhood', blank=True, null=True,on_delete=DO_NOTHING)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def profile(cls):
        profiles = cls.objects.all()
        return profiles

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def save_profile(self):
        self.user

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-pk"]
        
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

class Neighbourhood(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to='images/', null=True)
    admin = models.ForeignKey(Profile, related_name='hoods', null=True,on_delete=DO_NOTHING)
    description = models.CharField(max_length = 300,default='Neighborhood description')

class Business(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='bsimage/')
    description = models.CharField(max_length = 300)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='businesses',on_delete=DO_NOTHING)
    profile = models.ForeignKey(Profile, related_name='profiles',on_delete=DO_NOTHING)

    @classmethod
    def search_by_name(cls,search_term):
        business = cls.objects.filter(title__icontains=search_term)
        return business



class Post(models.Model):
    user = models.ForeignKey(Profile, related_name='profile',on_delete=DO_NOTHING)
    post = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='posts',on_delete=DO_NOTHING)

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name
