from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.edit import FormView, CreateView
from django.views.generic import View, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from cv_generator.forms import ExpeienceForm, SkillForm
from cv_generator.models import Experience, ContactData, Skill


class Overview(TemplateView):
    template_name = 'user/main/overview.html'
    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
        context = {}
        context['expereince'] = Experience.objects.filter(user_id=self.request.user.id).order_by('start')
        #context['contact_data'] = ContactData.objects.filter(user_id=self.request.user.id)
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

