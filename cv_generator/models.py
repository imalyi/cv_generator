from django.db.models import Model, CharField, IntegerField, DateField, ForeignKey, CASCADE, FloatField


class User(Model):
    name = CharField(max_length=100)
    surname = CharField(max_length=100)


class Experience(Model):
    start = DateField()
    end = DateField()
    position = CharField(max_length=150)
    location = CharField(max_length=150)
    user = ForeignKey(User, on_delete=CASCADE)


class Education(Model):
    title = CharField(max_length=250)
    degree = CharField(max_length=250)
    average = FloatField(blank=True)
    start = DateField()
    end = DateField()


class ContactDataType(Model):
    value = CharField(max_length=200)


class ContactData(Model):
    value = CharField(max_length=550)
    type = ForeignKey(ContactDataType, on_delete=CASCADE)


class SocialNetworkType(Model):
    value = CharField(max_length=250)


class SocialNetwork(Model):
    url = CharField(max_length=300)


class SkillType(Model):
    value = CharField(max_length=320)


class Skill(Model):
    value = CharField(max_length=250)
    description = CharField(max_length=250)
    type = ForeignKey(SkillType, on_delete=CASCADE)


