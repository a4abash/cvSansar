from django.shortcuts import render, redirect
from .forms import PersonalDetailsForm,EducationForm,ExperienceForm,SkillForm
from .models import Skill,PersonalDetails
from django.contrib.auth.models import User
from attributes.models import PersonalDetails, Education, Experience, Skill

# Create your views here.

def profile(request):
    if request.method == 'GET':
        a = PersonalDetails.objects.get(user_id=request.user.id)
        context = {
            'form': PersonalDetailsForm(instance=a)
        }
        return render(request, 'personaldetail.html', context)
    else:
        a = PersonalDetails.objects.get(user_id=request.user.id)
        form = PersonalDetailsForm(request.POST, request.FILES or None, instance=a)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('dashboard')
        else:
            return render(request, 'personaldetail.html', {'form': form})


def education(request):
    if request.method == 'GET':
        a = User.objects.get(id=request.user.id)
        education = Education.objects.filter(user_id=a)
        context = {
            'eform': EducationForm(),
            'edu': education
        }
        return render(request, 'educationupdate.html', context)
    else:
        form = EducationForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('education')
        else:
            return render(request, 'educationupdate.html', {'eform': form})


def experience(request):
    if request.method == 'GET':
        a = User.objects.get(id=request.user.id)
        experience = Experience.objects.filter(user_id=a)
        context = {
            'expform': ExperienceForm(),
            'experience': experience

        }
        return render(request, 'experienceupdate.html', context)
    else:
        form = ExperienceForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('experience')
        else:
            return render(request, 'experienceupdate.html', {'expform': form})


def skill(request):
    if request.method == 'GET':
        a = User.objects.get(id=request.user.id)
        skill = Skill.objects.filter(user_id=a)
        context = {
            'skill': skill,
            'sform': SkillForm()
        }
        return render(request, 'skillupdate.html', context)
    else:
        form = SkillForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('skill')
        else:
            return render(request, 'skillupdate.html', {'sform': form})


#education delete section
def edu_dlt(request, x):
    d = Education.objects.get(id=x)
    d.delete()
    return redirect('education')


#skill delete section
def skill_dlt(request, x):
    sd = Skill.objects.get(id=x)
    sd.delete()
    return redirect('skill')


#experience delete section
def experience_dlt(request, x):
    ed = Experience.objects.get(id=x)
    ed.delete()
    return redirect('experience')