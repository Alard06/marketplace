from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.main.views import index

urlpatterns = [
    path('', index, name='index'),
]