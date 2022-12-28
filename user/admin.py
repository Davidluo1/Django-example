from django.contrib import admin
#from posts.models import Reaction, UserPosts
from user.models import User

# Register your models here.

# @admin.register(Reaction)
# class ReactionAdmin(admin.ModelAdmin):
#     list_display = ["reaction_type", "description"]


# @admin.register(UserPosts)
# class PostsAdmin(admin.ModelAdmin):
#     list_display = ["title", "description"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email"]