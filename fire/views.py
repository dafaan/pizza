from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import menu_list, re
# Create your views here.



def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        city = request.POST['city']
        address = request.POST['address']

        user = User.objects.create_user(username=username, email=email, password=password1)#, city=city, address=address)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'sign_up.html')


def login(request):
    
    return render(request, 'login.html')


def home(request):
    re1 = re.objects.all()

    return render(request, 'home.html', {'re1':re1})
    
def menu(request):
    items = menu_list.objects.all()

    return render(request, 'menu.html', {'items':items})

#def send(request):
#    if request.method == 'POST':
#        username = request.POST['username']
#        email = request.POST['email']
#        password1 = request.POST['password1']
#        password2 = request.POST['password2']
#        city = request.POST['city']
#        address = request.POST['address']

#        user = user.objects.create_user(username=username, email=email, password=password1, city=city, address=address)
#        user.save()
#        return redirect('/')
#    else:
#        return render(request, 'login.html')