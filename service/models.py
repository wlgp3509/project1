from django.db import models


from django.forms.widgets import RadioSelect


# 21.10.21 선택 결과 테이블 정의_최졔
# 120p 참조

class Choice(models.Model):

    ADHD_CHOICES = [('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')]
    contents = models.TextField()

    def __str__(self):
        return self.contents
