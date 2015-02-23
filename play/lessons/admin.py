from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from lessons import models

class FileInline(admin.TabularInline):
    model = models.File

class LessonAdmin(MarkdownModelAdmin):
    readonly_fields = ('file_use_in_body',)

    def file_use_in_body(self, instance):
        if instance.slug:
            islug = instance.slug
        else:
            islug = "lesson-slug"

        return "/media/lessons/" + islug + "/filename"

    inlines = [FileInline, ]
    list_display = ("title", "order", "created", "modified", "publish")
    fields = (('title', 'order'),
            ('slug',),
            'icon', 'photo',
            'brief', 'file_use_in_body', 'body', 'publish')

    prepopulated_fields = {"slug": ("title",)}
    ordering = ['order']

admin.site.register(models.Lesson, LessonAdmin)
