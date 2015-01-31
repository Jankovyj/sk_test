from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from questions.views import AddQuestion, QuestionList, QuestionDetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'body.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', QuestionList.as_view(), name='question_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/$', login_required(AddQuestion.as_view()), name='add_question'),
    url(r'^(?P<pk>\d+)/$', QuestionDetail.as_view(),
        name='detail_question'),
    url(r'^accounts/',
        include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls',
                    namespace='social'))
)
