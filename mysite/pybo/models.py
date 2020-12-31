from django.db import models

# 질문
class Question(models.Model):
    subject = models.CharField(max_length=200) # 제목
    content = models.TextField() # 내용
    create_date = models.DateTimeField() # 작성일시

# 답변
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

