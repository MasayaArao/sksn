from django import forms
from snippets.models import Snippet,Comment,FileUpload
from snippets.models import Snippet2,Comment2,FileUpload2

class DateInput(forms.DateInput):
    input_type = 'date'

class SnippetForm(forms.ModelForm): 
    class Meta:    
        model = Snippet
        fields = ('status','title','language','accept_date','duedate','code', 
                  'description')
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select','style': 'width: 170px'}),
            'language': forms.Select(attrs={'class': 'form-select','style': 'width: 140px'}),
            'accept_date': DateInput(attrs={'class': 'date_input','style': 'width: 140px'}),
            'duedate': DateInput(attrs={'class': 'date_input','style': 'width: 140px'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('upload',)

# SearchFormクラスを定義
class SearchForm(forms.Form):
    STATUS_CHOICES = (
        ('', ''),
        ('案件立ち上げ', '案件立ち上げ'),
        ('資料受領待ち', '資料受領待ち'),
        ('積算中', '積算中'),
        ('施工中', '施工中'),
        ('設計変更中', '設計変更中'),
        ('案件完了', '案件完了'),
    )

    LANGUAGE_CHOICES = (
        ('', ''),        
        ('本社', '本社'),
        ('東京支店', '東京支店'),
        ('名古屋支店', '名古屋支店'),
        ('九州支店', '九州支店'),
    )

    query = forms.CharField(label='工事件名', required=False, max_length=100)#required=False を指定することで、検索条件が空でもフォームを送信できる
    query2 = forms.ChoiceField(choices =LANGUAGE_CHOICES, label='担当事業所', required=False)
    query3 = forms.ChoiceField(choices =STATUS_CHOICES, label='進捗状況', required=False)
    start_date = forms.DateField(label='積算締切日', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(label='～', widget=forms.DateInput(attrs={'type': 'date'}), required=False)

class SnippetForm2(forms.ModelForm):
    class Meta:
        model = Snippet2
        fields = ('title', 'code', 'description')
    

class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ('text', )

class FileUploadForm2(forms.ModelForm):
    class Meta:
        model = FileUpload2
        fields = ('upload',)

# SearchFormクラスを定義
class SearchForm2(forms.Form):
    query = forms.CharField(label='検索', max_length=100)