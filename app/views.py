from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_display')
    else:
        form = ImageForm()
    return render(request, 'vatsalya/upload_image.html', {'form': form})

def image_display(request):
    images = Image.objects.all()
    return render(request, 'vatsalya/gallery.html', {'images': images})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('upload_image')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'vatsalya/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'vatsalya/login.html', {'form': form})


def logout_user(request):
    logout(request)
    # Redirect to a page after logout
    return redirect('Home')



def home(request):
    return render(request, 'vatsalya/home.html')

def about(request):
    return render(request,'vatsalya/about.html')

def contact(request):
    return render(request, 'vatsalya/contact.html')

def executive(request):
    return render(request, 'vatsalya/executive.html')

def admission(request):
    return render(request, 'vatsalya/admissionprocedure.html')

def principle(request):
    return render(request, 'vatsalya/principle.html')

def fee(request):
    return render(request, 'vatsalya/fee.html')

def examination(request):
    return render(request, 'vatsalya/examination.html')

def academic(request):
    return render(request, 'vatsalya/aim.html')

def facility(request):
    return render(request,'vatsalya/facility.html')