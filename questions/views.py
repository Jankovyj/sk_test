from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, DetailView
from questions.forms import QuestionForm
from questions.models import Question, Comment
from django.utils.translation import ugettext_lazy as _


class AddQuestion(FormView):
    """
    Добавление вопроса
    """
    login_required = True
    template_name = 'questions/add_question.html'
    form_class = QuestionForm

    def get_success_url(self):
        title = self.request.POST['title'].strip() or _('Without title')
        text = self.request.POST['text']
        Question.objects.create(title=title,
                                text=text,
                                user=self.request.user)
        return '/'
        

class QuestionList(ListView):
    """
    Список вопросов
    """
    template_name = 'questions/list_question.html'
    context_object_name = 'questions'
    paginate_by = 5
    model = Question


class QuestionDetail(DetailView):
    template_name = 'questions/detail_question.html'
    model = Question
    context_object_name = 'question'

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        comment_text = self.request.POST['comment_text'].strip()
        Comment.objects.create(text=comment_text,
                               question=self.get_object(),
                               user=self.request.user)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
