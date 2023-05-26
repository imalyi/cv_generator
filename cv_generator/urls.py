from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from cv_generator.views import ExpereinceView, Overview, SkillView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", Overview.as_view()),
    path("expereince/", ExpereinceView.as_view()),
    path("skills/", SkillView.as_view()),
]
