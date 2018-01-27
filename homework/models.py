from django.db import models
from markupfield.fields import MarkupField


class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')

    def __str__(self):
        return 'Subject <{}>'.format(self.name)


class Material(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    text = MarkupField(default_markup_type='markdown', verbose_name='name')

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    pinned = models.BooleanField(default=False)

    def __str__(self):
        return 'Material <{}> on {}'.format(self.title, str(self.subject))


class Deadline(models.Model):
    date = models.DateTimeField(verbose_name='date')

    title = models.CharField(max_length=200, verbose_name='title')
    text = MarkupField(default_markup_type='markdown', verbose_name='name')

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return 'Deadline <{}> on {}'.format(self.title, str(self.subject))
