from django.contrib import admin
from django.urls import path, include

from snippets.views import top

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', top, name='top'),
    path('snippets/', include('snippets.urls')),
    path("accounts/", include("accounts.urls")),
    path('admin/', admin.site.urls),
]