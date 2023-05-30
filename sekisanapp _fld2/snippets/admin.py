from django.contrib import admin
from snippets.models import Snippet
from .models import FileUpload

admin.site.register(Snippet)
admin.site.register(FileUpload)
