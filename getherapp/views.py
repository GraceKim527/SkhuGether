from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime, time
from getherapp.models import Classroom, Class
from .forms import FeedbackForm
from django.db.models import Q

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
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "중앙도서관")
    classes = Class.objects.all()
    return render(request, 'class/library.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 9관 피츠버그홀
def pb_hall(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "피츠버그홀")
    classes = Class.objects.all()
    return render(request, 'class/pb_hall.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 10관 구두인관
def gdin_gwan(request):
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "구두인관")
    classes = Class.objects.all()
    return render(request, 'class/gdin_gwan.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 12관 성베드로학교
def sbdr_school(request):
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "성베드로학교")
    classes = Class.objects.all()
    return render(request, 'class/sbdr_school.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 11관 미가엘관
def mgell_gwan(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "미가엘관")
    classes = Class.objects.all()
    return render(request, 'class/mgell_gwan.html',
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 'classrooms':classrooms, 'classes': classes})

# 13관 행복기숙사
def dormitory(request):
    # 이게 모델 내용 가져오는 것
    classrooms = Classroom.objects.order_by('id').filter(kwan_name = "행복기숙사")
    return render(request, 'class/dormitory.html',
    {'classrooms':classrooms})

def classroom(request, unit_id, id): #unit==unit_id==Class.room_id, id==classroom.id
    classroom = get_object_or_404(Classroom, unit = unit_id, id = id)
    classes = Class.objects.all().order_by('time2')

    '''월요일'''
    mon_classes = classes.filter(room_id=id)
    mon_classes = list(mon_classes.filter(Q(date1='월') | Q(date2='월'))) #유닛이 같고 월요일인 강의인 객체들을 쿼리셋에서 리스트로 변환
    mon_test =[] # 월요일 수업이 있으면 요소 추가할 리스트
    for i in mon_classes: 
        mon_test.append(i) 
    if len(mon_test)<1: #월 수업을 추가했는데 리스트 길이가 1도 안된다면 공강임
        mon_classes = '공강'
    else: # 리스트 길이가 1이상이면 공강 아니니까
        mon_classes = classes.filter(room_id=id)
        mon_classes = mon_classes.filter(Q(date1='월') | Q(date2='월')) # 찐 mon_classes에 유닛같은 월수업 객체 모두 담기

    '''화요일'''
    tue_classes = classes.filter(room_id=id)
    tue_classes = list(tue_classes.filter(Q(date1='화') | Q(date2='화')))
    tue_test =[] 
    for i in tue_classes: 
        tue_test.append(i) 
    if len(tue_test)<1: 
        tue_classes = '공강'
    else: 
        tue_classes = classes.filter(room_id=id)
        tue_classes = tue_classes.filter(Q(date1='화') | Q(date2='화'))

    '''수요일'''
    wed_classes = classes.filter(room_id=id)
    wed_classes = list(wed_classes.filter(Q(date1='수') | Q(date2='수')))
    wed_test =[] 
    for i in wed_classes: 
        wed_test.append(i) 
    if len(wed_test)<1: 
        wed_classes = '공강'
    else: 
        wed_classes = classes.filter(room_id=id)
        wed_classes = wed_classes.filter(Q(date1='수') | Q(date2='수'))
        

    '''목요일''' 
    thu_classes = classes.filter(room_id=id)
    thu_classes = list(thu_classes.filter(Q(date1='목') | Q(date2='목')))
    thu_test =[] 
    for i in thu_classes: 
        thu_test.append(i) 
    if len(thu_test)<1: 
        thu_classes = '공강'
    else: 
        thu_classes = classes.filter(room_id=id)
        thu_classes = thu_classes.filter(Q(date1='목') | Q(date2='목'))
        

    '''금요일'''
    fri_classes = classes.filter(room_id=id)
    fri_classes = list(fri_classes.filter(Q(date1='금') | Q(date2='금')))
    fri_test =[]
    for i in fri_classes: 
        fri_test.append(i) 
    if len(fri_test)<1: 
        fri_classes = '공강'
    else: 
        fri_classes = classes.filter(room_id=id)
        fri_classes = fri_classes.filter(Q(date1='금') | Q(date2='금'))


    return render(request, 'classroom.html', 
    {'now_date':now_date, 'now_time':now_time, 'now_weekday':now_weekday, 
    'time_list': time_list, 
    'classroom': classroom, 'classes': classes,
    'mon_classes':mon_classes,'tue_classes':tue_classes,'wed_classes':wed_classes,'thu_classes':thu_classes,'fri_classes':fri_classes,
    'mon_test':mon_test,'tue_test':tue_test,'wed_test':wed_test,
    })
