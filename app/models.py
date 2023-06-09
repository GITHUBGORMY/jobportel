from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class Login(AbstractUser):
    is_Jobseeker = models.BooleanField(default=False)
    is_Recuiter = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    companyname = models.CharField(max_length=200)
    registrationNo = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    phone = models.FloatField(null=True)
    location =models.CharField(max_length=200, null=True)
    jobTitle = models.CharField(max_length=200, null=True)
    Required_job= models.CharField(max_length=200, null=True)
    Qualification= models.CharField(max_length=200, null=True)
    Experience = models.CharField(max_length=200, null=True)
    profilepicture = models.FileField(upload_to='documents/', null=True)
    status = models.IntegerField(default=0, null=True)

def __str__(self):
    return str(self.companyname)
class Preferences(models.Model):
    recuiter = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    Companyname = models.CharField(max_length=200 , unique = True)
    location = models.CharField(max_length=200)
    jobTitle = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=200, null=True)
    Experience = models.CharField(max_length=200, null=True)
    salary = models.CharField(max_length=200, null=True)
    Description = models.CharField(max_length=200, null=True)
    date = models.DateField(auto_now=False)
    status=  date = models.DateField(auto_now=False)
    status = models.IntegerField(default=0, null=True)
class Skill(models.Model):
    seeker = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    primary_skill = models.CharField(max_length=200, null=True)
    secondary_skill = models.CharField(max_length=200, null=True)
class Application(models.Model):
    seeker = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    prefer = models.ForeignKey(Preferences, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=200, null=True)
    job= models.CharField(max_length=200, null=True)
    applicant = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    resume = models.FileField(upload_to='Documents/', null=True)
    date = models.DateField(auto_now=False)
    status = models.IntegerField(default=0, null=True)
    def __str__(self):
        return str(self.applicant)
0
