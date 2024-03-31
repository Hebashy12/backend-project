from django.shortcuts import render, redirect, get_object_or_404
from .models import Dentist, Message
from .form import SignUpForm, AddDentist
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    dentist = Dentist.objects.all()

    return render(request, "home.html", {"dentist": dentist})


def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save()
            auth_login(request, user)
            return redirect("home")

    return render(request, "signup.html", {"form": form})


# def dentistAdd(request):
#     form = AddDentist()
#     if request.user.username == "admin":

#         if request.method == "POST":
#             form = SignUpForm(request.POST)
#             if form.is_valid():

#                 user = form.save()
#                 dentist = Dentist.objects.create(name=user.username, age=40)
#                 auth_login(request, user)
#                 return redirect("home")

#     return render(request, "add.html", {"form": form})


@login_required
def dentistAdd(request):
    if request.user.username == "mohamed":
        form = AddDentist()
        if request.method == "POST":
            form = AddDentist(request.POST)
            if form.is_valid():
                user = form.save()
                # Create a corresponding Dentist object
                Dentist.objects.create(user=user, age=40)
                auth_login(request, user)
                return redirect("home")
        return render(request, "add.html", {"form": form})
    else:
        return redirect("home")


def chat(request, dential_id):
    # try:

    #     dentist = Dentist.objects.get(pk=dential_id)
    #     if request.method == "POST":
    #         message = request.POST["message"]
    #         # send_to = dentist.name

    #         created_by = User.username
    #         message = Message.objects.create(
    #             message=message, send_to=dentist, created_by=request.user
    #         )

    # except Dentist.DoesNotExist:
    #     # raise render(request, "error.html")

    #     return render(request, "error.html")
    # return render(request, "chate.html", {"dentist": dentist})
    dentist = get_object_or_404(Dentist, pk=dential_id)

    if request.method == "POST":
        # Extract message content from POST request
        message_content = request.POST.get("message")
        # Ensure that a message was actually provided before attempting to save
        if message_content:
            # No need to get created_by from User.username directly; use request.user
            Message.objects.create(
                message=message_content, send_to=dentist, created_by=request.user
            )
            # After posting a message, redirect to the same page to display the updated message list
            # and prevent form resubmission on refresh
            return redirect(request.path_info)

    # Assuming you want to pass messages to the template as well
    messages = Message.objects.filter(send_to=dentist).order_by("-created_dt")

    return render(request, "chate.html", {"dentist": dentist, "messages": messages})
