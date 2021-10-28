from django.db import models

# 21.10.21 선택 결과 테이블 정의_최졔

class Choice(models.Model):
    ADHD_CHOICES = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'))
    choices = models.CharField(max_length=1, choices=ADHD_CHOICES, default=0)
    contents = models.TextField()


