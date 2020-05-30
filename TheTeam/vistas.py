"""TheTeam Vistas."""
#django
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase

config = {

  "apiKey": "AIzaSyB9iCZUG4_b6d9x0ZOLUzpO--E-RIZgWuw",
  "authDomain": "theteambackend.firebaseapp.com",
  "databaseURL": "https://theteambackend.firebaseio.com",
  "projectId": "theteambackend",
  "storageBucket": "theteambackend.appspot.com",
  "messagingSenderId": "559754082260",
  "appId": "1:559754082260:web:88c4
}
firebase = pyrebase.initialize_app(config)
 auth = firebase.auth()

 def singIn(request):
#cambiar el nombre del archivo
     return render(request,"singIn.html")

def postsing(request):
    return render(request,"welcome.html")
