from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from cv_generator.forms import ExpeienceForm, SkillForm, EducationForm, ContactDataForm
from cv_generator.models import Experience, ContactData, Skill, Education


class UserId:
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class Overview(LoginRequiredMixin, TemplateView):
    template_name = 'user/main/overview.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expereince'] = Experience.objects.filter(user_id=self.request.user.id).order_by('start')
        context['skill'] = Skill.objects.filter(user_id=self.request.user.id)
        context['contact_data'] = ContactData.objects.filter(user_id=self.request.user.id)
        context['education'] = Education.objects.filter(user_id=self.request.user.id)
        if not context['expereince'] and not context['skill'] and not context['contact_data'] and not context['education']:
            context['empty'] = True
        else:
            context['empty'] = False
        return context


class ExpereinceView(LoginRequiredMixin, UserId, CreateView):
    template_name = 'user/experience/experience.html'
    form_class = ExpeienceForm
    success_url = '/expereince/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expereince'] = Experience.objects.filter(user_id=self.request.user.id).order_by('start')
        return context


class ExpereinceUpdateView(UpdateView):
    model = Experience
    form_class = ExpeienceForm
    success_url = "/"
    template_name = 'user/experience/experience.html'


class ExpereinceDeleteView(DeleteView):
    model = Experience
    success_url = "/"
    template_name = 'user/main/confirm_delete_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expereince'] = Experience.objects.filter(user_id=self.request.user.id)
        return context


class SkillView(LoginRequiredMixin, UserId, CreateView):
    template_name = 'user/skill/skill.html'
    form_class = SkillForm
    success_url = '/skills/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill'] = Skill.objects.filter(user_id=self.request.user.id)
        return context


class SkillUpdateView(UpdateView):
    model = Skill
    form_class = SkillForm
    success_url = "/"
    template_name = 'user/skill/skill.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill'] = []
        return context


class SkllDeleteView(DeleteView):
    model = Skill
    success_url = "/"
    template_name = 'user/main/confirm_delete_form.html'


class EducationView(LoginRequiredMixin, UserId, CreateView):
    template_name = 'user/education/education.html'
    form_class = EducationForm
    success_url = '/education/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education'] = Education.objects.filter(user_id=self.request.user.id)
        return context




class EducationUpdateView(UpdateView):
    model = Education
    form_class = EducationForm
    success_url = "/"
    template_name = 'user/education/education.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education'] = []
        return context


class EducationDeleteView(DeleteView):
    model = Education
    success_url = "/"
    template_name = 'user/main/confirm_delete_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education'] = Experience.objects.filter(user_id=self.request.user.id)
        return context



class ContactDataView(LoginRequiredMixin, UserId, CreateView):
    template_name = 'user/contact_data/contact_data.html'
    form_class = ContactDataForm
    success_url = '/contact_data/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_data'] = ContactData.objects.all().filter(user_id=self.request.user.id)
        return context

class ContactDataUpdateView(UpdateView):
    model = ContactData
    form_class = ContactDataForm
    success_url = "/"
    template_name = 'user/education/education.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_data'] = []
        return context


class ContactDataDeleteView(DeleteView):
    model = ContactData
    success_url = "/"
    template_name = 'user/main/confirm_delete_form.html'
