from django.shortcuts import render, redirect
from .forms import PersonalDetailsForm,EducationForm,ExperienceForm,SkillForm
from django.contrib.auth.models import User
from attributes.models import PersonalDetails, Education, Experience, Skill

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


# render html to pdf
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


# View page for the generated pdf only used if you view the pdf it is not used here
class ViewPDF(View):
    template_name = 'download.html'

    def get(self, request, *args, **kwargs):
        a = User.objects.get(id=request.user.id)
        attr = PersonalDetails.objects.get(user_id=a)
        education = Education.objects.filter(user_id=a)
        skill = Skill.objects.filter(user_id=a)
        experience = Experience.objects.filter(user_id=a)
        context = {
            'user': a,
            'attr': attr,
            'skill': skill,
            'education': education,
            'experience': experience,
        }
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

    def post(self, request, *args, **kwargs):
        pass


# Used for downloading the generated pdf
class DownloadPDF(View):
    template_name = 'download.html'

    def get(self, request, *args, **kwargs):
        a = User.objects.get(id=request.user.id)
        attr = PersonalDetails.objects.get(user_id=a)
        education = Education.objects.filter(user_id=a)
        skill = Skill.objects.filter(user_id=a)
        experience = Experience.objects.filter(user_id=a)
        context = {
            'user': a,
            'attr': attr,
            'skill': skill,
            'education': education,
            'experience': experience,
        }
        pdf = render_to_pdf(self.template_name, context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "My%s.pdf" % ("resume")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


# profile update section
def updateprofile(request):
    if request.method == 'GET':
        a = User.objects.get(id=request.user.id)
        attr = PersonalDetails.objects.get(user_id=a)
        context = {
            'user': a,
            'uform': PersonalDetailsForm(instance=attr)
        }
        return render(request, 'updatePersonaldetail.html', context)
    else:
        a = PersonalDetails.objects.get(user_id=request.user.id)
        form = PersonalDetailsForm(request.POST, request.FILES or None, instance=a)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('dashboard')
        else:
            return render(request, 'updatePersonaldetail.html', {'form': form})


# education section
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


# experience section
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


# skill section
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


# education delete section
def edu_dlt(request, x):
    d = Education.objects.get(id=x)
    d.delete()
    return redirect('education')


# skill delete section
def skill_dlt(request, x):
    sd = Skill.objects.get(id=x)
    sd.delete()
    return redirect('skill')


# experience delete section
def experience_dlt(request, x):
    ed = Experience.objects.get(id=x)
    ed.delete()
    return redirect('experience')