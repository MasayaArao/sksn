from django.conf import settings
from django.db import models
import os
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

class Snippet(models.Model):
    title = models.CharField('工事件名', max_length=128)
    LANGUAGE_CHOICES = (
        ('本社', '本社'),
        ('東京支店', '東京支店'),
        ('名古屋支店', '名古屋支店'),
        ('九州支店', '九州支店'),
    )
    accept_date = models.DateField('受付日',default=timezone.now)
    duedate = models.DateField('積算締切日',default=timezone.now)
    STATUS_CHOICES = (
        ('案件立ち上げ', '案件立ち上げ'),
        ('資料受領待ち', '資料受領待ち'),
        ('積算中', '積算中'),
        ('施工中', '施工中'),
        ('設計変更中', '設計変更中'),
        ('案件完了', '案件完了'),
    )

    code = models.TextField('内容', blank=True)
    language = models.CharField('担当事業所',max_length=20, choices=LANGUAGE_CHOICES, default='本社')
    status = models.CharField('進捗状況',max_length=20, choices=STATUS_CHOICES, default='案件立ち上げ')
    description = models.TextField('参考文献・過去積算案件', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    #page = models.CharField(max_length=100)
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

def get_upload_path(instance, filename):
    """アップロード先のパスを決定する関数"""
    return f"file/{instance.page}/{filename}"

class FileUpload(models.Model):
    #page = models.CharField(max_length=255)
    #uped_to = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=get_upload_path)


class Snippet2(models.Model):
    title = models.CharField('タイトル', max_length=128)
    code = models.TextField('内容', blank=True)
    description = models.TextField('参考文献・過去積算案件', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    #page = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Comment2(models.Model):
    text = models.TextField("本文", blank=False)
    commented_at = models.DateTimeField("投稿日", auto_now_add=True)
    commented_to = models.ForeignKey(Snippet2, verbose_name="ポイント",
                                     on_delete=models.CASCADE)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     verbose_name="投稿者",
                                     on_delete=models.CASCADE)

    def __str__(self):
        return self.text

def get_upload_path2(instance, filename):
    """アップロード先のパスを決定する関数"""
    return f"file/{instance.page}/{filename}"

class FileUpload2(models.Model):
    #page = models.CharField(max_length=255)
    #uped_to = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=get_upload_path2)