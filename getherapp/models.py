from email.policy import default
from django.db import models 
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Subject(models.Model):
    kind = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    kwan_num = models.SmallIntegerField(
        validators=[
            MinValueValidator(1), MaxValueValidator(13)
            ]
    ) 
    kwan_name = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/classroom', null=True, blank=True)

    def __str__(self):
        return str(self.unit)

class Class(models.Model):
    div = models.SmallIntegerField(null=True,
        validators=[
            MinValueValidator(1), MaxValueValidator(3)]
    )    
    date1 = models.CharField(max_length=10)
    date2 = models.CharField(max_length=10, null=True)
    time1 = models.TimeField()
    time2 = models.TimeField()
    prof_id = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL, related_name='class_profid')
    room_id = models.ForeignKey(Classroom, null=True, on_delete=models.SET_NULL, related_name='class_roomid')
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='class_subid')

    def __str__(self):
        return self.room_id

class Feedback(models.Model):
    user_id = models.CharField(max_length=50)
    feedback_date = models.DateTimeField(auto_now_add=True)
    user_phonenum = models.CharField(max_length=100, null=True) #추가해봤어염
    feedback_content = models.TextField(default = "글을 작성해주세요.")
 
    def __str__(self):
        return self.user_id

        # models 수정