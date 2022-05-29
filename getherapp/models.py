from django.db import models

# Create your models here.
<<<<<<< HEAD

class Class(models.Model):
    class_id = models.IntegerField()
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name

class Professor(models.Model):
    professor_id = models.IntegerField()
    professor_name = models.CharField(max_length=20)
    
class Classroom(models.Model):
    classroom_id = models.IntegerField()
    classroom_unit = models.CharField(max_length=20)
    professor_name = models.ForeignKey(Professor, on_delete = models.SET_NULL, null=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)


class Feedback(models.Model):
    user_id = models.IntegerField()
    feedback_date = models.DateTimeField(auto_now_add=True)
    user_phonenum = models.CharField(max_length=100, null=True) #추가해봤어염
    feedback_content = models.TextField()
=======
>>>>>>> 728b2fdb83652e2000d90f1e543263df9c7c25e2
