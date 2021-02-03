from django.contrib import admin
from .models import PersonalDetails, Experience, Education, Skill
# Register your models here.
admin.site.register([PersonalDetails, Experience, Education, Skill])

