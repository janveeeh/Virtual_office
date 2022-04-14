

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from .forms import CareerRegistration
from Head.models import Career, CareerApplicant,Employee
from math import ceil
from Head.views import Logout
from django.shortcuts import redirect
# Create your views here.

#adding and retrieving data

 

def index(request):
    #try:
        #result = request.session['ADMIN']
        #data=Employee.objects.get(id=result)
        
        fm = CareerRegistration()
        stud = Career.objects.all()
        return render(request, 'career/index2.html',{'form':fm, 'stu':stud})
    #except  Exception as e:
        #Logout(request) 
        #print(e)
        #return redirect('login')

    

def add_show(request):
    if request.method == 'POST':
        fm = CareerRegistration(request.POST)
        if fm.is_valid():
            j_ti = fm.cleaned_data['job_title']
            j_ty = fm.cleaned_data['job_type']
            j_r = fm.cleaned_data['job_role']
            reg = Career(job_title=j_ti, job_type=j_ty, job_role=j_r)
            reg.save()
            stud = Career.objects.all()
            return render(request, 'career/index2.html', {'form':fm, 'stu':stud})
        
    else:
        fm = CareerRegistration()
        stud = Career.objects.all()
        return render(request, 'career/view_career.html', {'form':fm, 'stu':stud})

#edit and update function
def update_data(request,id):
    if request.method == 'POST':
        pi = Career.objects.get(pk=id)
        fm = CareerRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Career.objects.get(pk=id)
        fm = CareerRegistration(instance=pi)

    return render(request,'career/edit.html', {'form':fm})

#delete function

def delete_data(request,id):
    if request.method == 'POST':
        pi = Career.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/index/')


'''
from django.shortcuts import render
from django.http import HttpResponse
from .models import Career, CareerApplicant
from math import ceil


def career(request):
        if request.method == "POST":
            print(request)
            job_title = request.POST.get('job_title', '')
            job_type = request.POST.get('job_type', '')
            job_role = request.POST.get('job_role', '')
            qualification = request.POST.get('qualification', '')
            key_skills = request.POST.get('key_skills', '')
            exp = request.POST.get('exp', '')
            required_language = request.POST.get('required_language', '')
            location = request.POST.get('location', '')
            job_description = request.POST.get('job_description', '')
            image = request.POST.get('image', '')
            created_datetime = request.POST.get('created_datetime', '')

            career = Career(job_title=job_title, job_type=job_type, job_role=job_role, qualification=qualification, key_skills=key_skills, exp=exp,
            	required_language=required_language, location=location, job_description=job_description, image=image, created_datetime=created_datetime )
            career.save()
        return render(request, 'career/career_req.html')'''

def view_applicant(request):
    app=CareerApplicant.objects.all()
    params={'stu': app}
    return render(request, "career/view_app.html", params)


def ApplicationView2(request , myid):
    ap = CareerApplicant.objects.filter(id=myid)
    return render(request, 'career/app_view.html', {'ap': ap[0], 'id': myid})



'''def view_career(request): 
    car= Career.objects.all()
    params={'car': car}
    return render(request, "career/view_career2.html", params)
    '''