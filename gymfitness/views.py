from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from gymfitness.models import Contact,MembershipPlan,Trainer
from gymfitness.models import Enrollment
from gymfitness.models import Gallery
from gymfitness.models import Attendance


# Create your views here.
def Home(request):
    return render(request,"index.html")


def signup(request):
    if request.method=="POST":
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
    
        if len(username)>10 or len(username)<10:
             messages.info(request,"Phone Number must be 10") 
             return redirect('/signup')
        if pass1 != pass2:
            messages.info(request,"Password incorrect!") 
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone number is taken")
                return redirect('/signup')
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is taken")
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is created Please login")
        return redirect('/login')
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":
        username = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username = username, password = pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfull")
            return redirect('/')
        else:
            messages.error(request,"Invalid Login!!")
            return redirect('/login')
    return render(request,"handlelogin.html")



def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('/login')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        number = request.POST.get('num')
        desc = request.POST.get('desc')
        myquery = Contact(name = name, email=email, phonenumber=number, description=desc)
        myquery.save()

        messages.info(request, "Thanks for Contacting us we will get back to you soon")
        return redirect('/contact')

    return render(request,"contact.html")



def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please login and try again!")
        return redirect('/login')

    Membership = MembershipPlan.objects.all()
    SelectTrainer = Trainer.objects.all()
    context = {"Membership": Membership, "SelectTrainer":SelectTrainer}

    if request.method == "POST":
        FullName = request.POST.get('fullName')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        PhoneNumber = request.POST.get('PhoneNumber')
        DOB = request.POST.get('DOB')
        member = request.POST.get('member')
        trainer = request.POST.get('trainer')
        reference = request.POST.get('reference')
        address = request.POST.get('address')
        query = Enrollment(FullName = FullName, Email=email, Gender=gender,PhoneNumber=PhoneNumber, DOB=DOB, SelectMembershipPlan = member, SelectTrainer = trainer, Reference=reference, Address=address )
        query.save()
        print(query)
        messages.success(request, "Thanks for the Enrollment....")
        return redirect('/join')
    return render(request, "enroll.html", context)


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please login and try again!")
        return redirect('/login')

    user_phone = request.user
    posts = Enrollment.objects.filter(PhoneNumber = user_phone)
    attendance = Attendance.objects.filter(phoneNumber = user_phone)
    print(posts)
    context = {"posts":posts, "attendance":attendance}
    return render(request, 'profile.html', context)



def gallery(request):
    posts = Gallery.objects.all()
    context = {"posts": posts}
    return render(request,"gallery.html", context)




def attendance (request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please login and Try Again!!")
        return redirect('/login')

    SelectTrainer = Trainer.objects.all()
    context = {"SelectTrainer": SelectTrainer}

    if request.method == "POST":
        phoneNumber = request.POST.get('PhoneNumber')
        login = request.POST.get('logintime')
        logout = request.POST.get('loginouttime')
        selectWorkout = request.POST.get('workout')
        trainedBy = request.POST.get('trainer')

        query = Attendance(phoneNumber=phoneNumber, login=login, logout=logout, selectWorkout=selectWorkout, trainedBy=trainedBy)
        query.save()
        messages.warning(request, "Attendance has been Applied Successfully!!")
        return redirect('/attendance')

    return render(request,"attendance.html",context)


