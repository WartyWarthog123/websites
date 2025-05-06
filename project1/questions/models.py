from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    answer_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text