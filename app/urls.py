from django.urls import path

from app import views, recuter_view, jobseeker_view

urlpatterns = [
    path('', views.index, name="index"),
    path('jobhome', views.jobhome, name="jobhome"),
    path('new', views.new, name="new"),
    path('rec', views.rec, name="rec"),
    path('beforereg', views.beforereg, name="beforereg"),
    path('seeker_register', views.seeker_register, name="seeker_register"),
    path('recuiter_register', views.recuiter_register, name="recuiter_register"),
    path('Recuiterdash', views.Recuiterdash, name="Recuiterdash"),
    path('admindash', views.admindash, name="admindash"),
    path('accept_recuiter/<int:id>', views.accept_recuiter, name="accept_recuiter"),
    path('reject_recuiter/<int:id>', views.reject_recuiter, name="reject_recuiter"),

    path('login_view', views.login_view, name="login_view"),
    path('Recuiterview', views.Recuiterview, name="Recuiterview"),
    path('logout_view', views.logout_view, name="logout_view"),

#Recuiter
    path('Preference_fun', recuter_view.Preference_fun, name="Preference_fun"),
    path('preview', recuter_view.preview, name="preview"),
    path('preview', recuter_view.preview, name="preview"),
    path('preference_delete/<int:id>', recuter_view.preference_delete, name="preference_delete"),
    path('preference_update/<int:id>', recuter_view.preference_update, name="preference_update"),
    path('profile', recuter_view.profile, name="profile"),
    path('profile_update_rec/<int:id>', recuter_view.profile_update_rec, name="profile_update_rec"),

#jobseeker
    path('jobView',jobseeker_view.jobView,name="jobView"),
    path('application',jobseeker_view.application,name="application"),
    path('jobprofile',jobseeker_view.jobprofile,name="jobprofile"),
    path('Applied',jobseeker_view.Applied,name="Applied"),
    path('profile_update/<int:id>',jobseeker_view.profile_update,name="profile_update"),
]

