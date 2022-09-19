from django.views.generic import TemplateView
from datetime import datetime


# Create your views here.
class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_title"] = "Громкий новостной заголовок"
        context['news_preview'] = 'Предварительное описание, чтоб заманить читателя'
        context['range'] = range(5)
        context["datetime_obj"] = datetime.now()
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
