from django.shortcuts import redirect, render, HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from attributes.models import PersonalDetails, Education, Experience, Skill
from attributes.forms import PersonalDetailsForm
from django.contrib.auth.decorators import login_required


# home page
def home(request):
    return render(request, 'index.html')


# signup page
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


# login page
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        u = request.POST.get('username')
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            id = request.user.id
            x = checkIfExist(id)
            if x == 10:
                return redirect('dashboard')
            else:
                return redirect('firstPersonaldetail')
        else:
            messages.error(request, "Your Password does not match")
            return redirect('signin')


# check if user is new
def checkIfExist(id):
    try:
        a = PersonalDetails.objects.get(user_id=id)
        return 10
    except:
        return 20


# redirects new user to personaldetail section
@login_required(login_url='signin')
def firstPersonaldetail(request):
    r = checkIfExist(request.user.id)
    if r == 10:
        return redirect('dashboard')
    else:
        if request.method == 'GET':
            context = {
                'form': PersonalDetailsForm()
            }
            return render(request, 'firstPersonaldetail.html', context)
        else:
            form = PersonalDetailsForm(request.POST, request.FILES or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.user_id = request.user.id
                data.save()
                return redirect('dashboard')
            else:
                return render(request, 'firstPersonaldetail.html', {'form': form})


# User dashboard
@login_required(login_url='signin')
def dashboard(request):
    if request.method == 'GET':
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
    else:
        return render(request, 'dashboard.html')


# about us page
def aboutUs(request):
    return render(request, 'about.html')


# User logout section
def signout(request):
    logout(request)
    return redirect('signin')