from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile', views.updateprofile, name='updateprofile'),  # personal details editing section
    path('education', views.education, name='education'),  # education section
    path('experience', views.experience, name='experience'),  # experience section
    path('skill', views.skill, name='skill'),  # skill section
    path('eduDelete/<int:x>', views.edu_dlt, name='edu_dlt'),  # delete the data from education table
    path('skillDelete/<int:x>', views.skill_dlt, name='skill_dlt'),  # delete the data from skill table
    path('expDelete/<int:x>', views.experience_dlt, name='experience_dlt'),  # delete the data from experience table
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),  # home page for viewing pdf redirect to pdf_view to view the pdf before downloading
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),  # pdf download section
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
