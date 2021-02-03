from django.shortcuts import redirect, render, HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from attributes.models import PersonalDetails, Education, Experience, Skill


def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm(),
        }
        return render(request, 'signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is successfully created")
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        u = request.POST.get('username')
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("error occured")
            messages.error(request, "Your Password does not match")
            return redirect('signin')


def personaldetail(request):
    if request.method == 'GET':
        return render(request, 'personaldetail.html')
    else:
        pass


# Jobseeker project update section
def dashboard(request):
    if request.method == 'GET':
        try:
            a = User.objects.get(id=request.user.id)
            attr = PersonalDetails.objects.get(user_id=a)
            education = Education.objects.filter(user_id=a)
            skill = Skill.objects.filter(user_id=a)
            experience = Experience.objects.filter(user_id=a)
            context = {
                'user': a,
                'form': SignUpForm(),
                'attr': attr,
                'skill': skill,
                'education': education,
                'experience': experience,
            }
            return render(request, 'dashboard.html', context)
        except:
            a = User.objects.get(id=request.user.id)
            education = Education.objects.filter(user_id=a)
            skill = Skill.objects.filter(user_id=a)
            experience = Experience.objects.filter(user_id=a)
            context = {
                'user': a,
                'form': SignUpForm(),
                'skill': skill,
                'education': education,
                'experience': experience,
            }
            return render(request, 'dashboard.html', context)
    else:
        return render(request, 'dashboard.html')


# for signout
def signout(request):
    logout(request)
    return redirect('signin')