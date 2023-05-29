from django.contrib import admin
from django.urls import path, include
from cv_generator.views import ExpereinceView, Overview, SkillView, EducationView, ContactDataView, ExpereinceUpdateView, ExpereinceDeleteView, SkillUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),

    path("", Overview.as_view(), name='main'),

    path("expereince/", ExpereinceView.as_view(), name='experience'),
    path("expereince/<int:pk>/update", ExpereinceUpdateView.as_view(), name='experience-update'),
    path("expereince/<int:pk>/delete", ExpereinceDeleteView.as_view(), name='experience-delete'),


    path("skills/", SkillView.as_view(), name='skill'),
    path("skills/<int:pk>/update", SkillUpdateView.as_view(), name='skill-update'),
    path("skills/<int:pk>/delete", SkillView.as_view(), name='skill-delete'),

    path("education/", EducationView.as_view()),
    path("contact_data/", ContactDataView.as_view())

]
