from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def feedback(request):
    return render(request, 'feedback.html')

def introduce(request):
    return render(request, 'introduce.html')

def dormitory(request):
    return render(request, 'class/dormitory.html')

def gdin_gwan(request):
    return render(request, 'class/gdin_gwan.html')

def im_gwan(request):
    return render(request, 'class/im_gwan.html')

def jg_gwan(request):
    return render(request, 'class/jg_gwan.html')

def library(request):
    return render(request, 'class/library.html')

def mgell_gwan(request):
    return render(request, 'class/mgell_gwan.html')

def nn_gwan(request):
    return render(request, 'class/nn_gwan.html')

def pb_hall(request):
    return render(request, 'class/pb_hall.html')

def sbdr_school(request):
    return render(request, 'class/sbdr_school.html')

def scn_gwan(request):
    return render(request, 'class/scn_gwan.html')

def sy_gwan(request):
    return render(request, 'class/sy_gwan.html')

def wd_gwan(request):
    return render(request, 'class/wd_gwan.html')