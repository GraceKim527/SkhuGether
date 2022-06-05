from django.db import models

# Create your models here.
class Class(models.Model):
    # class_id = models.IntegerField()
    class_name = models.CharField(max_length=50)
    class_date1 = models.CharField(max_length=20, null=True, blank=True)
    class_date2 = models.CharField(max_length=20, null=True, blank=True)
    class_time1 = models.TimeField(max_length=50, null=True, blank=True)
    class_time2 = models.TimeField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.class_name

class Professor(models.Model):
    # professor_id = models.IntegerField()
    professor_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.professor_name

class Classroom(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    professor_name = models.ForeignKey(Professor, on_delete = models.SET_NULL, null=True)
    class_date1 = models.ForeignKey(Class, on_delete = models.SET_NULL, null=True, related_name = 'date1')
    class_date2 = models.ForeignKey(Class, on_delete = models.SET_NULL, null=True, related_name = 'date2')
    class_time1 = models.ForeignKey(Class, on_delete = models.SET_NULL, null=True, related_name = 'time1')
    class_time2 = models.ForeignKey(Class, on_delete = models.SET_NULL, null=True, related_name = 'time2')
    # classroom_id = models.IntegerField()
    classroom_unit = models.CharField(max_length=20)

    def __str__(self):
        return self.classroom_unit

class Feedback(models.Model):
    user_id = models.CharField(max_length=50)
    feedback_date = models.DateTimeField(auto_now_add=True)
    user_phonenum = models.CharField(max_length=100, null=True) #추가해봤어염
    feedback_content = models.TextField()

    def __str__(self):
        return self.user_id