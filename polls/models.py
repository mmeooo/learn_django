from django.db import models

# Create your models here.
# 클래스의 기능: 상속
class Question(models.Model): # Table
    question_text= models.CharField(max_length= 100) # column, datatype
    public_date= models.CharField(max_length= 100)
    votes= models.DecimalField(max_digits= 20, decimal_places= 10)
# 위의 2개 타입으로 클래스 만들면 ok
# link, string-> CharField, data-> DecimalField
# 보통 max_length= 100으로 함

class Economics(models.Model):
    title= models.CharField(max_length= 100)
    href= models.CharField(max_length= 100)
    create_date= models.CharField(max_length= 100)
