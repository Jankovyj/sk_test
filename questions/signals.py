from django.db.models.signals import post_save
from django.dispatch import receiver
from questions.models import Comment
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _

@receiver(post_save, sender=Comment)
def send_mail_on_comment(instance, *args, **kwargs):
    """Отправляем письмо автору вопроса"""
    message_text = _('Someone replied to your question')
    send_mail(_('Answer'), message_text, settings.SERVER_EMAIL,
              [instance.question.user.email, ], fail_silently=False)
