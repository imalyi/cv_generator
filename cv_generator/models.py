from django.db.models import Model, CharField, DateField, ForeignKey, CASCADE, FloatField, FileField, DO_NOTHING, DateTimeField
import cv_generator.settings as settings


class CvTemplate(Model):
    name = CharField(max_length=200)
    file = FileField(upload_to='cv_templates')


class UserCV(Model):
    template = ForeignKey(CvTemplate, on_delete=DO_NOTHING)
    date = DateTimeField(auto_now=True)
    file = FileField(upload_to='users_cv')
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)


class Experience(Model):
    start = DateField()
    end = DateField()
    position = CharField(max_length=150)
    location = CharField(max_length=150)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    description = CharField(max_length=5000)
    company_name = CharField(max_length=150)

    def __str__(self):
        return f"{self.user}: {self.position}({self.start}: {self.end}), {self.location}"


class Education(Model):
    educational_institution = CharField(max_length=250)
    degree = CharField(max_length=250)
    grade_point_average = FloatField(blank=True)
    start = DateField()
    end = DateField()
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    def __str__(self):
        return f"{self.user}: {self.educational_institution}({self.start}: {self.end}), {self.grade_point_average}, {self.degree}"


class ContactDataType(Model):
    value = CharField(max_length=200)

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class ContactData(Model):
    value = CharField(max_length=550)
    type = ForeignKey(ContactDataType, on_delete=CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)


class SocialNetworkType(Model):
    value = CharField(max_length=250)


class SocialNetwork(Model):
    url = CharField(max_length=300)


class SkillType(Model):
    value = CharField(max_length=320)

    def __str__(self):
        return f"{self.value}"


class Skill(Model):
    value = CharField(max_length=250)
    description = CharField(max_length=250)
    type = ForeignKey(SkillType, on_delete=CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
