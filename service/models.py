from django.db import models


# 21.10.21 선택 결과 테이블 정의_최졔
# 120p 참조

class Choice(models.Model):
    choice = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
