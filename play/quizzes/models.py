from django.db import models
from lessons.models import Lesson


class QuestionQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Question(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    lesson = models.ForeignKey(Lesson)
    question_text = models.TextField()
    default_answer = models.CharField(max_length=200, default="skipped")
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = QuestionQuerySet.as_manager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.TextField()
    is_correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
