
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('', include('apps.buyer.urls')),
    path('', include('apps.seller.urls')),
    path('', include('apps.product.urls'))
]
