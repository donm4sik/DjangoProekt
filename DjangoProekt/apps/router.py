from django.urls import path, include

from apps.news.views import show_user_info

urlpatterns = [
    path('', show_user_info),
    path('news/', include('apps.news.urls')),
]