from django.db.models import Model, CharField, IntegerField, DateField, ForeignKey, CASCADE, FloatField
import cv_generator.settings as settings


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
    title = CharField(max_length=250)
    degree = CharField(max_length=250)
    average = FloatField(blank=True)
    start = DateField()
    end = DateField()
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    def __str__(self):
        return f"{self.user}: {self.title}({self.start}: {self.end}), {self.average}, {self.degree}"


class ContactDataType(Model):
    value = CharField(max_length=200)


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
