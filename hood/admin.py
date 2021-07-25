from django.contrib import admin
from .models import Profile,Category,Business,Post,Neighbourhood

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Post)
