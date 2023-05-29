import django
django.setup()
from django.contrib.auth.models import User


user = User.objects.create_user('igor', password='343877')
user.is_superuser = True
user.is_staff = True
user.save()
