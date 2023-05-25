from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def login_user(request):
  template = loader.get_template('login.html')
  if request.method == 'POST':
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      if user is not None:
            login(request, user)
            return redirect("/app")

  context = { }
  return render(request,'login.html',{})

def app(request):
  return render(request,'app.html',{})