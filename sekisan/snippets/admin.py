from django.contrib import admin
from snippets.models import Snippet,Snippet2
from .models import FileUpload,FileUpload2
from .models import Comment,Comment2


admin.site.register(Snippet)
admin.site.register(Snippet2)
admin.site.register(FileUpload)
admin.site.register(FileUpload2)
admin.site.register(Comment)
admin.site.register(Comment2)