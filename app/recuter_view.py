from django.contrib import messages
from django.shortcuts import redirect, render

from app.forms import PreferencesForm, RecuiterForm
from app.models import Preferences, Login


def preview(request):
    recuiter = Login.objects.get(name=request.user)
    data = Preferences.objects.filter(recuiter=recuiter)
    return render(request, 'Recuiter/preview.html', {"data": data})
def Preference_fun(request):
    Preferences_Form = PreferencesForm()
    u = request.user
    if request.method == 'POST':
        Preferences_Form = PreferencesForm(request.POST)
        if Preferences_Form.is_valid():
            obj=Preferences_Form.save()
            obj.recuiter = u
            obj.save()
            messages.info(request, 'successfully complete')
            return redirect('preview')
    return render(request, 'Recuiter/preference.html', {'Preferences_Form': Preferences_Form})

def preference_delete(request,id):
    data = Preferences.objects.get(id=id)
    data.delete()
    return redirect('preview')

def preference_update(request,id):
    sche = Preferences.objects.get(id=id)
    form = PreferencesForm(instance=sche)
    if request.method == 'POST':
        form = PreferencesForm(request.POST,instance=sche)
        if form.is_valid():
            form.save()
            return redirect('preview')
    return render(request,'Recuiter/prefe_update.html',{'form':form})
def profile(request):
    data = Login.objects.filter(is_Recuiter=True)
    return render(request, 'Recuiter/profile.html', {"data": data})
def profile_update_rec(request,id):
    sche = Login.objects.get(id=id)
    form = RecuiterForm(instance=sche)
    if request.method == 'POST':
        form = RecuiterForm(request.POST, instance=sche)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'Recuiter/profile_update.html', {'form': form})
def Applications(request,id):
    data = Applications.objects.filter()



