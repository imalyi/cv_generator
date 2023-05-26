from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Experience, Education, Skill


class DateInput(forms.DateInput):
    input_type = 'date'


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ("user", )


class ExpeienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"
        exclude = ("user",)
        widgets = {
            'start': DateInput(),
            'end': DateInput(),
        }