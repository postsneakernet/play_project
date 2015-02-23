from django.db import models

def lesson_dir(instance, filename):
    return '/'.join(['lessons', instance.slug, filename])

def file_dir(instance, filename):
    return '/'.join(['lessons', instance.lesson.slug, filename])

class LessonQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=1)
    slug = models.SlugField(max_length=200, unique=True)
    brief = models.TextField(max_length=600)
    body = models.TextField()
    icon = models.ImageField(upload_to=lesson_dir, )
    photo = models.ImageField(upload_to=lesson_dir)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = LessonQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class File(models.Model):
    file = models.FileField(upload_to=file_dir)
    lesson = models.ForeignKey(Lesson)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
