from django.contrib import admin
from cv_generator.models import Experience, Education, ContactData, ContactDataType, SocialNetworkType, SocialNetwork, SkillType, Skill, CvTemplate, UserCV

models = [Experience, Education, ContactData, ContactDataType, SocialNetworkType, SocialNetwork, SkillType, Skill, CvTemplate, UserCV]

for model in models:
    admin.site.register(model)