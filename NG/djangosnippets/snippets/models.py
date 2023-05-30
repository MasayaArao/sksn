from django.conf import settings
from django.db import models
from django.utils import timezone

class Snippet(models.Model):
    title = models.CharField('タイトル',max_length=128)
    code = models.TextField('コード',blank=True)
    description = models.TextField('説明',blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    verbose_name="投稿者",
                                    on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="投稿日")
    updated_at = models.DateTimeField(verbose_name="更新日")
    '''
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()  # 新規作成時の時刻を保存
        self.modified = timezone.now()  # 保存されるたびに更新
        return super(Snippet, self).save(*args, **kwargs)
    '''
    def __str__(self):
        return self.title
