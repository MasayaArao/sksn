from django.conf import settings
from django.db import models
import os
import datetime

class Snippet(models.Model):
    title = models.CharField('タイトル', max_length=128)
    code = models.TextField('内容', blank=True)
    description = models.TextField('参考文献・過去積算案件', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    text = models.TextField("本文", blank=False)
    commented_at = models.DateTimeField("投稿日", auto_now_add=True)
    commented_to = models.ForeignKey(Snippet, verbose_name="ポイント",
                                     on_delete=models.CASCADE)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     verbose_name="投稿者",
                                     on_delete=models.CASCADE)

    def __str__(self):
        return self.text

def dir_path_name(instance, filename):
    date_time = datetime.datetime.now()  # 現在の時刻を取得
    date_dir = date_time.strftime('%Y/%m/%d')  # 年/月/日のフォーマットの作成
    time_stamp = date_time.strftime('%H-%M-%S')  # 時-分-秒のフォーマットを作成
    new_filename = time_stamp + filename  # 実際のファイル名と結合
    dir_path = os.path.join('file', date_dir, new_filename)  # 階層構造にする
    return dir_path

class FileUpload(models.Model):
    upload = models.FileField(upload_to=dir_path_name)
    
    #uploaded_at = models.DateTimeField("投稿日", auto_now_add=True)
    
    #uploaded_page = models.ForeignKey(Snippet,on_delete=models.CASCADE)
    '''
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     verbose_name="投稿者",
                                     on_delete=models.CASCADE)
    def __str__(self):
        return self.upload
    '''