from django.urls import path,include


urlpatterns = [
    path('viewonly/',include('view_only.urls')),
    path('template/',include('with_template.urls')),
    ]
