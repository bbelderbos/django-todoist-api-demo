from django.contrib import admin

from .models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created' , 'due_date')

admin.site.register(TodoItem, TodoItemAdmin)
