import datetime
from django.db import models

# Create your models here.
# class Destination(models.Model):
#     id:int
#     title_name: str
#     img:str
#     desc:str
#     read_more=bool
    
class Destination(models.Model):
    # id=models.IntegerField
    title_name= models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    read_more=models.BooleanField(default=False)
    ###############

class Doctors(models.Model):
    dr_name=models.CharField(max_length=100)
    dr_email=models.CharField(max_length=100)
    dr_phone=models.CharField(max_length=100)
    dr_specialization=models.CharField(max_length=100)
    dr_address=models.CharField(max_length=100)
    dr_appoinments=models.CharField(max_length=100)
    dr_topics=models.CharField(max_length=100)
    dr_price=models.IntegerField()
    dr_dates=models.DateTimeField(default=datetime.datetime(2022, 1, 1, 0, 0))
    dr_desc=models.TextField()
    dr_img=models.ImageField(upload_to='pics')


class RegisterUsers(models.Model):
    name_user=models.CharField(max_length=100)
    email_user=models.CharField(max_length=100)
    password_user=models.CharField(max_length=100)
    phone_user=models.CharField(max_length=100)
    accept_user= models.BooleanField(default=False)


class Schedule(models.Model):
    doctor_id=models.IntegerField()
    day=models.CharField(max_length=100)
    dr_name=models.CharField(max_length=100)
    start_time=models.IntegerField()
    end_time=models.IntegerField()
    dr_dates=models.DateTimeField(default=datetime.datetime(2022, 1, 1, 0, 0))

class Appointment(models.Model):
    doctor_id=models.IntegerField()
    schedule_id=models.IntegerField()
    patient_name=models.CharField(max_length=100)
    doctor_name=models.CharField(max_length=100)
    patient_phone=models.CharField(max_length=100)
    appointment_time=models.CharField(max_length=100)
    duration=models.IntegerField()
    description=models.TextField()
    appoint_date=models.DateTimeField(default=datetime.datetime(2022, 1, 1, 0, 0))


class FilesPatients(models.Model):
    files_name=models.FileField(upload_to='patient_files/')
    patient_name=models.CharField(max_length=100)
