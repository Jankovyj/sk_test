from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Основная модель
    """
    title = models.CharField(max_length=255, verbose_name=_('title'))
    text = models.TextField(verbose_name=_('text'))
    user = models.ForeignKey(User,)
    dt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'sk_question'
        verbose_name = _('question')
        verbose_name_plural = _('questions')

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Модель комментария
    """
    text = models.TextField(verbose_name=_('text'))
    question = models.ForeignKey(Question, related_name='comment')
    user = models.ForeignKey(User)
    dt = models.DateTimeField(auto_now = True)

    class Meta:
        managed = True
        db_table = 'sk_comment'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
