from django.db import models
from django.contrib.auth.models import User

gender = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))


class PersonalDetails(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True, help_text="Leave Blank if you don't have one")
    profile = models.ImageField(upload_to='profile/', blank=True, null=True)
    gender = models.CharField(choices=gender, max_length=10)
    objective = models.TextField(help_text="About Yourself")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Education(models.Model):
    school = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    startYear = models.DateField(default='2019-09-09')
    EndYear = models.DateField(default='2019-09-09')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.school


class Experience(models.Model):
    company = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company


class Skill(models.Model):
    skill_title = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_title