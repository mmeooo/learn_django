from django.db import models

# Create your models here.
# 클래스의 기능: 상속
class Question(models.Model):
    question_text= models.CharField(max_length= 100)
    public_date= models.DateTimeField()
    votes= models.BigIntegerField()
# 위의 3개 타입으로 클래스 만들면 ok