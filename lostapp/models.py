from django.db import models
from getherapp.models import Classroom
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Lost(models.Model):
    #id
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    classroom = models.ForeignKey(Classroom, null=True, on_delete=models.SET_NULL, related_name='lost_room')
    image = models.ImageField(upload_to='images/lost', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(1000), MaxValueValidator(9999)]
    ) #4자리 비밀번호 작성
 
    def __str__(self):
        return '{}|{}'.format(self.title, str(self.classroom))

class Comment(models.Model):
    lost_id = models.ForeignKey(Lost, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content