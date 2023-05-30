from django.urls import path

from snippets import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("new/", views.snippet_new, name="snippet_new"),
    path("<int:snippet_id>/", views.snippet_detail, name="snippet_detail"),
    path("<int:snippet_id>/edit/", views.snippet_edit, name="snippet_edit"),
    path("<int:snippet_id>/comments/", views.comment_new, name="comment_new"),
    path('',views.index, name='index'),
    path("<int:snippet_id>/new_file", views.new_file, name='new_file'),  # 追加
    path("top/",views.top, name='top'),
    path("top2/",views.top2, name='top2'),
    path("new2/", views.snippet_new2, name="snippet_new2"),
    path("point/<int:snippet_id>/", views.snippet_detail2, name="snippet_detail2"),
    path("point/<int:snippet_id>/edit2/", views.snippet_edit2, name="snippet_edit2"),
    path("point/<int:snippet_id>/new_file2", views.new_file2, name='new_file2'),  # 追加
    path("point/<int:snippet_id>/comments2/", views.comment_new2, name="comment_new2"),
] 