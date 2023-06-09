from django.contrib import messages
from django.shortcuts import redirect, render
from app.forms import ApplicationForm, JobseekerForm
from app.models import Preferences, Login, Application


def jobView(request):
  job = Preferences.objects.all()
  return render(request, 'jobseeker/job_details.html', {"job": job})


def application(request):
    # job = Application.objects.all()
    Application_Form = ApplicationForm()
    if request.method == 'POST':
            Application_Form = ApplicationForm(request.POST,request.FILES)
            if Application_Form.is_valid():
                # job.status = 1
                Application_Form.save()
                return redirect('jobView')
    return render(request, 'jobseeker/apply1.html', {'Application_Form': Application_Form})
def Applied(request):
    u = request.user
    data = Application.objects.all()
    return render(request, 'jobseeker/Applied.html', {'data': data})

def jobprofile(request):
  u=request.user
  data = Login.objects.filter(username=u)
  return render(request, 'jobseeker/profile.html', {"data": data})

def profile_update(request,id):
    sche = Login.objects.get(id=id)
    form = JobseekerForm(instance=sche)
    if request.method == 'POST':
        form = JobseekerForm(request.POST, instance=sche)
        if form.is_valid():
            form.save()
            return redirect('jobprofile')
    return render(request, 'jobseeker/profile_update.html', {'form': form})



