from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
home_file = "index.html"
student_file = "student.html"
about_file = "about.html"
contact_file = "contact.html"

def home(request):
    return render(request, home_file, context={"page":"home"})


students_data = [
    {"Name":"Eknath" , "Age":21},
    {"Name":"Raj Kumar" , "Age":12},
    {"Name":"Om sharma" , "Age":23},
    {"Name":"Prem Dutta" , "Age":15},]

def students(request):
    return render(request, student_file, context= {"page": "students data", "students":students_data})

def about(request):
    return render(request, about_file, context= {"page": "about"})

def contact(request):
    return render(request, contact_file, context= {"page": "contact"})