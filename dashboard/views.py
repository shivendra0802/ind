from django.views.generic.base import View
from accounts import forms
from dashboard.forms import JobDetailsForm, JobPostForm, QualificationForm
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
# from .

def jobpost(request):
    if request.method == "POST":
        fm = JobPostForm(request.POST)
        if fm.is_valid():
            company_name = fm.cleaned_data['company_name']
            your_role_in_hiring_process = fm.cleaned_data['your_role_in_hiring_process']
            job_title  = fm.cleaned_data['job_title']
            job_category = fm.cleaned_data['job_category']
            location_of_company = fm.cleaned_data['location_of_company']
            street_address  = fm.cleaned_data['street_address']
            city        = fm.cleaned_data['city']
            country   = fm.cleaned_data['country']
            work_from_home = fm.cleaned_data['work_from_home']
            post_language = fm.cleaned_data['post_language']
            no_of_hiring  = fm.cleaned_data['no_of_hiring']
            always_hiring = fm.cleaned_data['always_hiring']

            instance = JobPost(company_name=company_name, your_role_in_hiring_process=your_role_in_hiring_process,
                    job_title=job_title, job_category=job_category, location_of_company=location_of_company,
                    street_address=street_address, city=city, country=country, work_from_home=work_from_home,
                    post_language=post_language, no_of_hiring=no_of_hiring, always_hiring=always_hiring)

            print(instance)
            instance.save()
            return redirect('comapny-info')

    else:
        fm = JobPostForm()
    return render(request, 'dashboard/dashboard.html', {"fm": fm})





def jobdetailview(request):
    if request.method == "POST":
        fm = JobDetailsForm(request.POST)
        if fm.is_valid():
            employment_type = fm.cleaned_data['employment_type']
            contract_type = fm.cleaned_data['contract_type']
            job_schedule   = fm.cleaned_data['job_schedule']
            supplement_pay     = fm.cleaned_data['supplement_pay']
            benefits     = fm.cleaned_data['benefits']
            job_description     = fm.cleaned_data['job_description']
            
            ins = JobDetails(employment_type=employment_type, contract_type=contract_type, job_schedule=job_schedule, supplement_pay=supplement_pay, benefits=benefits, job_description=job_description)
            print(ins)
            ins.save()
            return redirect('quali')
            # return render(request, 'dashboard/jobinformation.html', {"fm": fm})            
    else:
        fm = JobDetailsForm()
        return render(request, 'dashboard/jobinformation.html', {"fm": fm})            
            # return redirect('')


def company_info(request):
    if request.method == "POST":
        fm = CompanyInformationForm(request.POST)
        if fm.is_valid():
            your_name= fm.cleaned_data["your_name"]
            company_name = fm.cleaned_data["company_name"]
            phone_no     = fm.cleaned_data["phone_no"]
            company_size = fm.cleaned_data["company_size"]
            where_here_about_us = fm.cleaned_data["where_here_about_us"]

            instance = CompanyInformation(your_name=your_name, company_name=company_name, phone_no=phone_no, company_size=company_size, where_here_about_us=where_here_about_us)
            print(instance)
            instance.save()
            return redirect('jobdetail')
    else:
        fm = CompanyInformationForm()
    return render(request, 'dashboard/company-info.html', {"fm": fm})



def qualifi(request):
    if request.method == "POST":
        fm = QualificationForm(request.POST)
        if fm.is_valid():
            education = fm.cleaned_data["education"]
            experience = fm.cleaned_data["experience"]

            instance = Qualification(education=education,experience=experience)
            print(instance)
            instance.save()
    else:
        fm = QualificationForm()
    return render(request, 'dashboard/qualification.html', {"fm": fm})            

    # form = QualificationForm()
    # return render(request, 'dashboard/qualification.html', {"form": form})


class ShowView(ListView):
    model = JobPost 
    template_name = 'dashboard/jobshowpage.html'


def showdata(request):
    job_post = JobPost.objects.all()
    job_detail = JobDetails.objects.all()
    qua   = Qualification.objects.all()
    c_info = CompanyInformation.objects.all()
    
    context = {
        "job_post": job_post,
        "job_detail": job_detail,
        "qua": qua,
        "c_info": c_info,
    }
    return render(request, 'dashboard/jobshowpage.html', context)

def showdatas(request,slug,id=None):
    job_post = JobPost.objects.filter(id=id)
    job_post = JobPost.objects.filter(slug__iexact = slug)
    if job_post.exists():
       job_post = job_post.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    job_detail = JobDetails.objects.filter(id=id).first()
    qua   = Qualification.objects.filter(id=id).first()
    c_info = CompanyInformation.objects.filter(id=id).first()
    
    context = {
        "job_post": job_post,
        "job_detail": job_detail,
        "qua": qua,
        "c_info": c_info,
    }
    return render(request, 'dashboard/showpagedetail.html', context)    





def post_search(request):
    form = JobPostForm()
    results = []
    if 'q' in request.GET:
        form = JobPostForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            # full text search
        results = JobPost.objects.filter(title__search=q)
    return render(request, 'dashboard/jobshowpage.html', {'form':form, 'results':results, 'q': q})  