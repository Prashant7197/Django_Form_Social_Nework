from django.contrib import admin
from .models import Profile, Post, Comments, FriendRequest

admin.site.register(Profile)
admin.site.register(FriendRequest)
admin.site.register(Post)
admin.site.register(Comments)
# Register your models here.
