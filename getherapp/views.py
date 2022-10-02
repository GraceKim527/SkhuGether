from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import FeedbackForm

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.feedback_date = timezone.now()
            form.save()
            return redirect('index')
    else:
        form = FeedbackForm()
        print(form)
        return render(request, 'feedback.html', {'form': form})

def introduce(request):
    return render(request, 'introduce.html')

# 1관 승연관
def sy_gwan(request):
    return render(request, 'class/sy_gwan.html')

# 2관 일만관
def im_gwan(request):
    return render(request, 'class/im_gwan.html')

# 3관 월당관
def wd_gwan(request):
    return render(request, 'class/wd_gwan.html')

# 5관 나눔관
def nn_gwan(request):
    return render(request, 'class/nn_gwan.html')

# 6관 정보과학관
def jg_gwan(request):
    return render(request, 'class/jg_gwan.html')

# 7관 새천년관
def scn_gwan(request):
    return render(request, 'class/scn_gwan.html')

# 8관 중앙도서관
def library(request):
    return render(request, 'class/library.html')

# 9관 피츠버그홀
def pb_hall(request):
    return render(request, 'class/pb_hall.html')

# 10관 구두인관
def gdin_gwan(request):
    return render(request, 'class/gdin_gwan.html')

# 11관 성베드로학교
def sbdr_school(request):
    return render(request, 'class/sbdr_school.html')

# 12관 미가엘관
def mgell_gwan(request):
    return render(request, 'class/mgell_gwan.html')

# 13관 행복기숙사
def dormitory(request):
    return render(request, 'class/dormitory.html')
