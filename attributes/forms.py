from .models import PersonalDetails
from django import forms
from django.contrib.auth.models import User
from .models import Education, Experience, Skill


class PersonalDetailsForm(forms.ModelForm):
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    contact = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}))
    dob = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2051-02-02'}))
    website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Leave empty if you do not have one'}))
    profile = forms.ImageField()
    gender = forms.CharField(widget=forms.Select(choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')),
                                                 attrs={'class': 'form-control'}))
    objective = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Your main objective interest and aim'}))

    class Meta:
        model = PersonalDetails
        exclude = ['user']




class EducationForm(forms.ModelForm):
    school = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bernhardt COllege'}))
    level = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PLUS TWO'}))
    startYear = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2015-01-01'}))
    EndYear = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2019-01-01'}))

    class Meta:
        model = Education
        exclude = ['user']


class ExperienceForm(forms.ModelForm):
    company = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IIT NEPAL'}))
    post = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: CEO'}))
    start_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2017-01-01'}))
    end_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2020-12-12'}))

    class Meta:
        model = Experience
        exclude = ['user']


class SkillForm(forms.ModelForm):
    skill_title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Programmer'}))

    class Meta:
        model = Skill
        exclude = ['user']