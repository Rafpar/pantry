from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pantry import settings

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
