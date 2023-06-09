from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from app.forms import JobseekerForm, RecuiterForm
from app.models import Login


def index(requests):
    return render(requests, 'index.html')
def jobhome(request):
    return render(request, 'job_listing.html')
def new(request):
    return render(request, 'Recuiter/new.html')
def rec(request):
    return render(request, 'jobseeker/new/Modified_files/index.html')
def beforereg(request):
    return render(request, 'admin/beforereg.html')

def seeker_register(request):
    Jobseeker_Form = JobseekerForm()
    if request.method == 'POST':
        Jobseeker_Form = JobseekerForm(request.POST,request.FILES)
        if Jobseeker_Form.is_valid():
            user=Jobseeker_Form.save(commit=False)
            user.is_Jobseeker =True
            user.save()
            job = Jobseeker_Form.save(commit=False)
            job.user = user
            job.save()
            messages.success(request, 'registration successfully complete')
            return redirect('rec')
    return render(request,'admin/home.html',{'Jobseeker_Form': Jobseeker_Form}, )

def recuiter_register(request):
    Recuiter_Form = RecuiterForm()
    if request.method == 'POST':
        Recuiter_Form = RecuiterForm(request.POST,request.FILES)
        if Recuiter_Form.is_valid():
            user=Recuiter_Form.save(commit=False)
            user.is_Recuiter =True
            user.save()
            job = Recuiter_Form.save(commit=False)
            job.user = user
            job.save()
            messages.success(request, 'registration successfully complete')
            return redirect('Recuiterdash')
    return render(request,'admin/home.html',{'Recuiter_Form': Recuiter_Form}, )



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admindash')
            elif user.is_Jobseeker:
                return redirect('rec')
            elif user.is_Recuiter:
                return redirect('Recuiterdash')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'login.html')

def admindash(request):
    return render(request, 'dash.html')
def Recuiterdash(request):
    return render(request, 'Recuiter/index.html')
def Recuiterview(request):
    data =Login.objects.all()
    return render(request, 'admin/recuiter_view.html', {"data": data})
def accept_recuiter(request,id):
    data = Login.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("Recuiterview")

def reject_recuiter(request,id):
    data = Login.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("Recuiterview")
def logout_view(request):
    logout(request)
    # return redirect('%s?next=%s' % (settings.LOGOUT_URL, request.path))
    return redirect('index')


