from django.db import models

# Create your models here.


class  Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    description = models.TextField()

    def __str__(self):
        return self.email


class Enrollment(models.Model):
    FullName = models.CharField(max_length=40)
    Email = models.EmailField()
    Gender = models.CharField(max_length=25)
    PhoneNumber = models.CharField(max_length=12)
    DOB = models.CharField(max_length=50)
    SelectMembershipPlan = models.CharField(max_length=200)
    SelectTrainer = models.CharField(max_length=55)
    Reference = models.CharField(max_length=55)
    Address = models.TextField()
    PaymentStatus = models.CharField(max_length=55, blank=True, null= True)
    Price = models.IntegerField(max_length=55, blank=True, null= True)
    DueDate = models.DateTimeField(blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.FullName


class Trainer(models.Model):
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    salary = models.IntegerField(max_length = 25)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name



class MembershipPlan(models.Model):
    plan = models.CharField(max_length = 150)
    price = models.IntegerField(max_length=55)

    def __int__(self):
        return self.id
    



class Gallery(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='gallery')
    timeStamp = models.DateTimeField(auto_now_add=True, blank = True)

    def __inti__(self):
        return self.id



class Attendance(models.Model):
    selectDate = models.DateTimeField(auto_now_add = True)
    phoneNumber = models.CharField(max_length=10)
    login = models.CharField(max_length=150)
    logout = models.CharField(max_length=150)
    selectWorkout = models.CharField(max_length=150)
    trainedBy =models.CharField(max_length=150)

   



