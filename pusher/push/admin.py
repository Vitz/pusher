from django.contrib import admin
from .models import PostRow
# Register your models here.


@admin.register(PostRow)
class PostRowAdmin(admin.ModelAdmin):
    list_filter = ['group_id']
