from django.conf import settings
from todoist_api_python.api import TodoistAPI

from .models import TodoItem


def send_to_todoist(todo_item: TodoItem) -> bool:
    api = TodoistAPI(settings.TODOIST_API_TOKEN)
    try:
        due_string = todo_item.due_date.replace(tzinfo=None).isoformat("T") + "Z"
        task = api.add_task(
            content=todo_item.title,
            due_datetime=due_string,
        )
        print(task)
        return True
    except Exception as error:
        print(error)
        return False
