from django.contrib import admin
from django.urls import path, include

from snippets.views import index

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('snippets/', include('snippets.urls')),
    path("accounts/", include("accounts.urls")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)