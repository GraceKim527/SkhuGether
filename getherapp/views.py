from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime, time
from getherapp.models import Classroom, Class
from .forms import FeedbackForm

# Create your views here.
# 이게 현재 시간과 요일 가져오는 것
# 트랜스외국인이 돼야 한다면 순서 바꿔주면 됨
days = ['월', '화', '수', '목', '금', '토', '일']
now = datetime.now()
now_date = now.date()
now_time = now.time()
weekday = now.weekday()
now_weekday = days[weekday]

am9 = time(9, 00, 00, 000000)
am9_30 = time(9, 30, 00, 000000)
am10 = time(10, 00, 00, 000000)
am10_30 = time(10, 30, 00, 000000)
am11 = time(11, 00, 00, 000000)
am11_30 = time(11, 30, 00, 000000)
pm12 = time(12, 00, 00, 000000)
pm12_30 = time(12, 30, 00, 000000)
pm1 = time(13, 00, 00, 000000)
pm1_30 = time(13, 30, 00, 000000)
pm2 = time(14, 00, 00, 000000)
pm2_30 = time(14, 30, 00, 000000)
pm3 = time(15, 00, 00, 000000)
pm3_30 = time(15, 30, 00, 000000)
pm4 = time(16, 00, 00, 000000)
pm4_30 = time(16, 30, 00, 000000)
pm5 = time(17, 00, 00, 000000)
pm5_30 = time(17, 30, 00, 000000)
pm6 = time(18, 00, 00, 000000)
pm6_30 = time(18, 30, 00, 000000)
pm7 = time(19, 00, 00, 000000)

time_list = [am9, am9_30, am10, am10_30, am11, am11_30, pm12, pm12_30, pm1, pm1_30, pm2, pm2_30, pm3, pm3_30, pm4, pm4_30, pm5, pm5_30, pm6, pm6_30,pm7]

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
            return redirect('feedback_cp')
    else:
        form = FeedbackForm()
        return render(request, 'feedback.html', {'form': form})

def feedback_cp(request):
    return render(request, 'feedback_cp.html')

def introduce(request):
    return render(request, 'introduce.html')

# 1관 승연관
def sy_gwan(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "승연관")
    classes = Class.objects.all()
    return render(request, 'class/sy_gwan.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 2관 일만관
def im_gwan(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "일만관")
    classes = Class.objects.all()
    return render(request, 'class/im_gwan.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 3관 월당관
def wd_gwan(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id',).filter(kwan_name = "월당관")
    classes = Class.objects.all()
    return render(request, 'class/wd_gwan.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 5관 나눔관
def nn_gwan(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "나눔관")
    classes = Class.objects.all()
    return render(request, 'class/nn_gwan.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 6관 정보과학관
def jg_gwan(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "정보과학관")
    classes = Class.objects.all()
    return render(request, 'class/jg_gwan.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 7관 새천년관
def scn_gwan(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "새천년관")
    classes = Class.objects.all()
    return render(request, 'class/scn_gwan.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 8관 중앙도서관
def library(request):
    return render(request, 'class/library.html')

# 9관 피츠버그홀
def pb_hall(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "피츠버그홀")
    classes = Class.objects.all()
    return render(request, 'class/pb_hall.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 10관 구두인관
def gdin_gwan(request):
    return render(request, 'class/gdin_gwan.html')

# 11관 성베드로학교
def sbdr_school(request):
    return render(request, 'class/sbdr_school.html')

# 12관 미가엘관
def mgell_gwan(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "미가엘관")
    classes = Class.objects.all()
    return render(request, 'class/mgell_gwan.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 13관 행복기숙사
def dormitory(request):
    return render(request, 'class/dormitory.html')

def classroom(request, unit_id, id):
    classroom = get_object_or_404(Classroom, unit = unit_id, id = id)
    classes = Class.objects.all().order_by('time2')
    
    return render(request, 'classroom.html', 
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 
    'time_list': time_list, 
    'classroom': classroom, 'classes': classes})
