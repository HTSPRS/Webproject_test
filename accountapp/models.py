from django.db import models
class Users(models.Model):
    useremail = models.EmailField(max_length=30, primary_key=True, verbose_name="아이디")
    username = models.CharField(max_length=12, verbose_name="사용자")
    password = models.CharField(max_length=12, verbose_name="비밀 번호")
# Create your models here.
