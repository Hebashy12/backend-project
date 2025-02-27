# whiteteeth/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("ourTeam/", views.our_team, name="ourTeam"),
    path("contactUs/", views.contact_us, name="contactUs"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("book1/", views.book1, name="book1"),
    path("bookform/", views.bookform, name="bookform"),
    path("aftersignup/", views.aftersignup, name="aftersignup"),
    path("afterlogin/", views.afterlogin, name="afterlogin"),
    path("profile_doctor/", views.profile_doctor, name="profile_doctor"),
    path("details_patient/", views.details_patient, name="details_patient"),
    path("schedule/", views.schedule, name="schedule"),
    path("schedule_patients/", views.schedule_patients, name="schedule_patients"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("chat_patient/", views.chat_patient, name="chat_patient"),
    path("dashboard_patient/", views.dashboard_patient, name="dashboard_patient"),
    path("chat/", views.chat, name="chat"),
    path("payment/", views.payment, name="payment"),
    path("files/", views.files, name="files"),
    path("doctors/", views.doctors, name="doctors"),
    path("dr/", views.dr, name="dr"),
    path("bookdone/", views.bookdone, name="bookdone"),
    path("dentalServices/", views.dentalServices, name="dentalServices"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path('logout/', views.logout, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout')
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #  path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
