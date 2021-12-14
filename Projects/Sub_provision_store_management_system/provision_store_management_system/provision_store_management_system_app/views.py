from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def render_index(request):
    return HttpResponse("""
    <html>
    <head>
    <title>
    Provision Store Management System
    </title>
    </head>
    <body>
    <h1>Hello, World</h1>
    <p>Here we have the PROVISION MASTER</p>
    </body>
    </html>
    """)

def render_login(request):
    return render(request, "authentication/login.html")

def render_dashboard(request):
    return render(request, "control_system/dashboard.html")