from django import forms
from .models import Experience, Education, Skill, ContactData, UserCV


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


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"
        exclude = ("user",)
        widgets = {
            'start': DateInput(),
            'end': DateInput(),
        }


class ContactDataForm(forms.ModelForm):
    class Meta:
        model = ContactData
        fields = "__all__"
        exclude = ('user', )


class UserCVForm(forms.ModelForm):
    class Meta:
        model = UserCV
        fields = "__all__"
        exclude = ('user', 'date', 'file', )
