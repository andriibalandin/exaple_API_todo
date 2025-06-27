from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created', 'completed']
    search_fields = ['title', 'user', 'slug']
    list_filter = ['completed', 'created', 'user']
    prepopulated_fields = {'slug': ('title',)}
    