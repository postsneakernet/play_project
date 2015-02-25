from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from quizzes import models

class AnswerInline(admin.TabularInline):
    model = models.Answer


class QuestionAdmin(MarkdownModelAdmin):
    readonly_fields = ('check_if_one_and_only_one_correct_answer',)

    def check_if_one_and_only_one_correct_answer(self, instance):
        msg = ""
        amount = models.Answer.objects.filter(question__slug=instance.slug).\
                filter(is_correct_answer=True).count()

        if amount > 1:
            msg = "Warning: you have selected more than one correct answer"
        elif amount == 0:
            msg = "Please remember to select only one correct answer"
        else:
            msg += "Everything looks fine, you have selected one correct answer"

        return msg


    list_display = ('title', 'lesson', 'publish',)
    ordering = ['lesson']
    inlines = [AnswerInline, ]
    fields = (('title', 'slug'),
            ('lesson', 'publish'),
            'question_text', 
            ('check_if_one_and_only_one_correct_answer',))

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Question, QuestionAdmin)
