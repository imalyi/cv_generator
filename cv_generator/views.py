from django.views.generic.edit import FormView, CreateView
from django.views.generic import  TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from cv_generator.forms import ExpeienceForm, SkillForm, EducationForm, ContactDataForm
from cv_generator.models import Experience, ContactData, Skill, Education


class Overview(TemplateView):
    template_name = 'user/main/overview.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expereince'] = Experience.objects.filter(user_id=self.request.user.id).order_by('start')
        context['skill'] = Skill.objects.filter(user_id=self.request.user.id)
        if not context['expereince'] and not context['skill']:
            context['empty'] = False
        else:
            context['empty'] = True
        return context


class UserId:
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class ExpereinceView(LoginRequiredMixin, UserId, CreateView):
    template_name = 'user/experience/expereince.html'
    form_class = ExpeienceForm
    success_url = '/expereince/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expereince'] = Experience.objects.filter(user_id=self.request.user.id).order_by('start')
        return context


class SkillView(LoginRequiredMixin, UserId, CreateView):
    template_name = 'user/skill/skill.html'
    form_class = SkillForm
    success_url = '/skills/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill'] = Skill.objects.filter(user_id=self.request.user.id)
        return context


class EducationView(LoginRequiredMixin, UserId, CreateView):
    template_name = 'user/education/education.html'
    form_class = EducationForm
    success_url = '/education/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education'] = Skill.objects.filter(user_id=self.request.user.id)
        return context


class ContactDataView(LoginRequiredMixin, UserId, CreateView):
    template_name = 'user/contact_data/contact_data.html'
    form_class = ContactDataForm
    success_url = '/contact_data/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_data'] = Skill.objects.filter(user_id=self.request.user.id)
        return context