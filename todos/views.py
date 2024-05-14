from django.http import HttpResponse
from django.shortcuts import render

from .models import TodoItem
from .todoist import send_to_todoist


def index(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'index.html', {'todo_items': todo_items})


def complete_todo(request, todo_id: int):
    todo_item = TodoItem.objects.get(id=todo_id)
    success = send_to_todoist(todo_item)
    if success:
        todo_item.completed = True
        todo_item.save()
        return HttpResponse("<span class='message success'>Todo item completed</span>")
    else:
        return HttpResponse("<span class='message error'>Could not complete todo</span>")
