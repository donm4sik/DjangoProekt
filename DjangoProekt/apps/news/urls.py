from django.urls import path

from apps.news.views import (
    greeting,
)

urlpatterns = [
    path('', greeting),
]

"127.0.0.1:8000/news/"