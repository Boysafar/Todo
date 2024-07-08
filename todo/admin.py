from django.contrib import admin
from todo.models import Todo
import requests


def send_tasks_to_telegram(self, request, queryset):
    for todo in queryset:
        text = f"{todo.id}. {todo.name}\n"
        text += f"Description: {todo.description}\n"
        text += f"Status: {todo.status}"
        # send_msg_with_bot(text)
        TOKEN = "7355857174:AAHcjHeIJ_k6EQ19UTjx2idofAyNIsmygqo"
        CHAT_ID =  963020731

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"

        requests.get(url)


# def send_msg_with_bot(text):

send_tasks_to_telegram.short_description = "Telegramga yuborish"



@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "status")
    search_fields = ("name", )
    list_filter = ("status", )
    actions = (send_tasks_to_telegram, )

