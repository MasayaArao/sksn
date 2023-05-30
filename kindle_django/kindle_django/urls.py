from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewonly/', include('view_only.urls')),
    path('template/', include('with_template.urls')),
    path('note/', include('note.urls')),
]
