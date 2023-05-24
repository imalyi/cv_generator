from django.contrib import admin
from cv_generator.models import User, Experience, Education, ContactData, ContactDataType, SocialNetworkType, SocialNetwork, SkillType, Skill

models = [User, Experience, Education, ContactData, ContactDataType, SocialNetworkType, SocialNetwork, SkillType, Skill]

for model in models:
    admin.site.register(model)
