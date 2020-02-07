from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    if request.method=='POST':
        print('hello login')
        return redirect('login')
    else:
        return render(request,'accounts/login.html')
def logout(request):
    return redirect('home')
def dashboard(request):
    return render(request,'accounts/dashboard.html')
def register(request):
    if request.method=='POST':
        print('hello register')
        return redirect('register')
    else:
        return render(request,'accounts/register.html')
