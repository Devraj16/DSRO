from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.
# @login_required(login_url='login')
def index(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request,'index.html')
    
def about(request):
    # return HttpResponse("This is the about page.")
    return render(request,'about.html')

def blog(request):
    # return HttpResponse("Welcome to our blog.")
    return render(request,'blog.html')

def contact(request):
    # return HttpResponse("This is the contact page.")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact=Contact(name=name, email=email, message=message, timestamp=datetime.now())
        contact.save()  # Save the contact form data to the database
        messages.success(request, 'Your message has been sent successfully!')
        
        
    return render(request,'contact.html') 

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Django's default User model uses 'username', not 'email' for authentication.
        # So we need to get the username from the email if you're using email as login.
        from django.contrib.auth.models import User
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # change 'home' to your landing page
            else:
                messages.error(request, "Invalid credentials.")
        except User.DoesNotExist:
            messages.error(request, "Email not found.")

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Registration successful. You can now log in.")
        login(request, user)  # Optional: log in after registration
        return redirect('login')  # Change to your desired landing page

    return render(request, 'register.html')
    # return HttpResponse("Welcome to our blog.")
    # return render(request,'register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def dyson(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request,'dysonmission.html')

def voidwalker(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request,'voidwalkermission.html')

def kepler(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request,'keplermission.html')

def intergalactic(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request,'intergalacticmission.html')

def quantum(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request,'quantummission.html')

def terraforming(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request,'terraformingmission.html')
    