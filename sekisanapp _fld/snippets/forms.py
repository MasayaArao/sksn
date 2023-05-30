from django import forms

from snippets.models import Snippet,Comment,FileUpload


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('upload',)