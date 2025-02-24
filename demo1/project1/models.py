from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    is_active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, null=True)

def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_correct = models.BooleanField(default=False)
    feedback = models.TextField(blank=True, null=True)

def __str__(self):
    return self.choice_text
