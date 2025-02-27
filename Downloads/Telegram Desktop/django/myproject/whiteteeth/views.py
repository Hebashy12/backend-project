import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Destination
from .models import RegisterUsers
from .models import Doctors
from .models import Schedule
from .models import Appointment
from .models import FilesPatients
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User, auth

# from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import FilesPatientsForm

# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import logout
# from django.urls import reverse
# myapp/views.py


def index(request):
    # return HttpResponse("Hello, world. You're at the myapp index.")

    # fetch from database model
    dest = Destination.objects.all()
    # dest= RegisterUsers.objects.all()
    return render(request, "index.html", {"dest": dest})
    # return render(request, 'index.html',{'users': users})


# these are static data objects
# dest1=Destination()
# dest1.title_name="Periodontal Surgery django"
# dest1.desc="Periodontal surgery is a specialized procedure designed to treat gum disease"
# dest1.img='c1.png'
# dest1.read_more=True

# dest2=Destination()
# dest2.title_name="Payment note django"
# dest2.desc="You can pay through different methods And at any time"
# dest2.img='c2.png'
# dest2.read_more=False

# dest_objs=[dest1,dest2]


# return render (request,'index.html',{'dest':dest_objs}) #array
# return render (request,'index.html',{'dest1':dest1 , 'dest2':dest2})
# return render (request,'index.html')


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def our_team(request):
    return render(request, "ourTeam.html")


def contact_us(request):
    return render(request, "contactUs.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = RegisterUsers.objects.get(name_user=username)
            auth_user = User.objects.get(username=username)
            if user.password_user == password:
                messages.info(request, "Login successful!")
                auth_login(request, auth_user)
                request.session["user_id"] = user.id
                return redirect("afterlogin")
            else:
                messages.info(request, "Incorrect password.")
        except RegisterUsers.DoesNotExist:
            messages.info(request, "Username does not exist.")

    return render(request, "login.html")

    # signup


def signup(request):
    if request.method == "POST":
        name_user = request.POST["name_user"]
        email_user = request.POST["email_user"]
        password_user = request.POST["password_user"]
        phone_user = request.POST["phone_user"]
        accept_user = request.POST.get("accept_user", False) == "on"
        # Check if user with the same name already exists
        if RegisterUsers.objects.filter(name_user=name_user).exists():
            messages.info(
                request, "Username already taken. Please choose a different name."
            )
            # messages.error(request, 'Username already taken. Please choose a different name.')
            return redirect("signup")

        # user=User.objects.create_user()
        user = RegisterUsers(
            name_user=name_user,
            email_user=email_user,
            password_user=password_user,
            accept_user=accept_user,
            phone_user=phone_user,
        )
        user.save()
        auth_user = User.objects.create_user(
            username=name_user,
            email=email_user,
            password=password_user,
        )
        # Authenticate and log in the user
        auth_login(request, auth_user)

        # messages.success(request, 'Sign up successful!')
        request.session["user_id"] = user.id
        return redirect("aftersignup")  # Redirect to the index page

        # return HttpResponseRedirect(reverse('index'))  # Redirect to the success page

    else:
        return render(request, "signup.html")


# def success(request):
#     return HttpResponse("Sign up successful!")


def book1(request):
    return render(request, "book.html")


def bookform(request):
    if request.method == "POST":
        patient_name = request.POST["patient_name"]
        patient_phone = request.POST["patient_phone"]
        doctor_name = request.POST["doctor_name"]
        appoint_date = request.POST["appoint_date"]
        appointment_time = request.POST["appointment_time"]
        description = request.POST["description"]

        # As duration is disabled in the form, set it here
        duration = 1

        # Assuming doctor_id and schedule_id are provided somewhere, for now using 0
        doctor_id = 0
        schedule_id = 0

        appointment = Appointment(
            patient_name=patient_name,
            patient_phone=patient_phone,
            doctor_name=doctor_name,
            appoint_date=appoint_date,
            appointment_time=appointment_time,
            description=description,
            duration=duration,
            doctor_id=doctor_id,
            schedule_id=schedule_id,
        )
        appointment.save()

        # messages.success(request, 'Appointment booked successfully!')
        return redirect("bookdone")

    return render(request, "bookform.html")

    # return render(request, 'bookform.html')


def aftersignup(request):
    return render(request, "after-signup.html")


def afterlogin(request):

    return render(request, "after-login.html")


#


def profile_doctor(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("aftersignup")  # If no user ID in session, redirect to signup

    user1 = RegisterUsers.objects.get(id=user_id)
    return render(request, "profile_doctor.html", {"user1": user1})
    # return render(request,'profile_doctor.html')


#
def details_patient(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("afterlogin")  # If no user ID in session, redirect to signup

    user = RegisterUsers.objects.get(id=user_id)
    return render(request, "details_patient.html", {"user1": user})
    # return render(request,'profile_doctor.html')

    # return render(request,'details_patient.html')


def schedule(request):
    # Fetch all schedule entries
    schedules = Schedule.objects.all()
    return render(request, "schedule.html", {"schedules": schedules})


def schedule_patients(request):
    # Fetch all schedule entries
    schedules = Schedule.objects.all()
    return render(request, "schedule_patients.html", {"schedules": schedules})


def dashboard(request):

    # Fetch the user ID from the session
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")  # Redirect to login if not logged in

    # Fetch the logged-in user data
    user = RegisterUsers.objects.get(id=user_id)

    if request.method == "POST":
        dr_id = request.POST["dr_id"]
        day = request.POST["day"]
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]
        dr_dates = request.POST["dr_dates"]

        # Convert dr_dates to date object
        # dr_dates = datetime.datetime.strptime(dr_dates, "%Y-%m-%d").date()

        # Create and save the new schedule entry
        schedule_entry = Schedule(
            dr_name=user.name_user,
            day=day,
            start_time=start_time,
            end_time=end_time,
            dr_dates=dr_dates,
            doctor_id=dr_id,
        )
        schedule_entry.save()

        # messages.success(request, 'Data stored successfully!')
        return redirect("dashboard")

    # Fetch existing schedule entries for the logged-in doctor
    schedules = Schedule.objects.filter(dr_name=user.name_user)

    # Fetch appointment data for the logged-in doctor
    #
    # appointments = Appointment.objects.all()
    appointments = Appointment.objects.filter(doctor_name=user.name_user)

    # Fetch all FilesPatients objects
    files_patients = FilesPatients.objects.all()
    # Pass the user and schedules data to the template
    context = {
        "user1": user,
        "schedules": schedules,
        "appointments": appointments,
        "files_patients": files_patients,
    }

    return render(request, "dashboard.html", context)


def chat_patient(request):
    return render(request, "chat_patient.html")


# def dashboard_patient(request):
#     return render(request,'dashboard_patient.html')
def dashboard_patient(request):
    # Fetch the user ID from the session
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")  # Redirect to login if not logged in

    # Fetch the logged-in user data
    user = RegisterUsers.objects.get(id=user_id)

    if request.method == "POST":
        # Get the form data
        doctor_name = request.POST["doctor_name"]
        patient_name = request.POST["patient_name"]
        appoint_date = request.POST["appoint_date"]
        appointment_time = request.POST["appointment_time"]
        duration = 1  # Fixed duration of 1 hour as per your form
        description = request.POST["description"]

        # As duration is disabled in the form, set it here
        duration = 1

        # Assuming doctor_id and schedule_id are provided somewhere, for now using 0
        doctor_id = 0
        schedule_id = 0

        appointment = Appointment(
            patient_name=patient_name,
            doctor_name=doctor_name,
            appoint_date=appoint_date,
            appointment_time=appointment_time,
            description=description,
            duration=duration,
            doctor_id=doctor_id,
            schedule_id=schedule_id,
        )
        appointment.save()
        # messages.success(request, 'Appointment created successfully!')

        return redirect("dashboard_patient")  # Redirect to the same page after saving

    # Fetch all appointment data
    # appointments = Appointment.objects.all()
    appointments = Appointment.objects.filter(patient_name=user.name_user)

    # Fetch all FilesPatients objects
    # files_patients = FilesPatients.objects.all()
    # Fetch FilesPatients objects related to the logged-in user

    if request.method == "POST":
        # Create a form instance with POST data and the logged-in user's name
        form = FilesPatientsForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form without committing to set the patient_name manually
            files_patient = form.save(commit=False)
            files_patient.patient_name = user.name_user
            files_patient.save()
            messages.success(request, "File uploaded successfully!")
            return redirect("dashboard_patient")
    else:
        # Initialize the form with the logged-in user's name
        form = FilesPatientsForm(initial={"patient_name": user.name_user})
    files_patients = FilesPatients.objects.filter(patient_name=user.name_user)

    # Pass the user, appointments, and files_patients data to the template
    context = {
        "user": user,
        "appointments": appointments,
        "files_patients": files_patients,
    }

    return render(request, "dashboard_patient.html", context)


def chat(request):
    return render(request, "chat.html")


def payment(request):
    return render(request, "payment.html")


def files(request):
    if request.method == "POST":
        form = FilesPatientsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "File uploaded successfully!")
            return redirect("files")  # Adjust the redirection as needed
    else:
        form = FilesPatientsForm()

    # Fetch all files stored in the database
    files_patients = FilesPatients.objects.all()

    # Pass the form and files_patients queryset to the template
    return render(
        request, "files.html", {"form": form, "files_patients": files_patients}
    )

    # Pass the form and files_patients queryset to the template


def doctors(request):
    return render(request, "doctors.html")


def dr(request):
    return render(request, "dr1.html")


def bookdone(request):
    return render(request, "book-done.html")


def dentalServices(request):
    return render(request, "dental-services.html")


# def logout_view(request):
#     if 'user_id' in request.session:
#         del request.session['user_id']
#     return redirect('index')
# def logout(request):
#     auth.logout(request)
#     return redirect('/')

# def custom_logout_view(request):
#     logout(request)
#     return redirect('index')  # Redirect to the home page or any other page


# Create your views here.
