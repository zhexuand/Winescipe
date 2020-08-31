from django.contrib import admin
from homebase.models import ImagePost, WinescipeUser, Like, Comment, UserConnection

# Register your models here.

admin.site.register(ImagePost)
admin.site.register(WinescipeUser)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserConnection)



