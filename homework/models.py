from django.db import models
from markupfield.fields import MarkupField
import os
from django.conf import settings


from django.db import models
from django.dispatch import receiver


def update_filename(instance, filename):
    return os.path.join(settings.MEDIA_ROOT, instance.name)


class File(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    file = models.FileField(upload_to=update_filename)

    def __str__(self):
        return 'File <{}>'.format(self.name)


@receiver(models.signals.post_delete, sender=File)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=File)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = File.objects.get(pk=instance.pk).file
    except File.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(models.signals.pre_save, sender=File)
def auto_rename_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old = File.objects.get(pk=instance.pk)
    except File.DoesNotExist:
        return False

    if not old.name == instance.name:
        new_path = os.path.join(settings.MEDIA_ROOT, instance.name)
        os.rename(old.file.path, new_path)

        instance.file.name = new_path


class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')

    def __str__(self):
        return 'Subject <{}>'.format(self.name)


class Material(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    text = MarkupField(default_markup_type='markdown', verbose_name='text')

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    pinned = models.BooleanField(default=False)

    def __str__(self):
        return 'Material <{}> on {}'.format(self.title, str(self.subject))


class Deadline(models.Model):
    date = models.DateTimeField(verbose_name='date')

    title = models.CharField(max_length=200, verbose_name='title')
    text = MarkupField(default_markup_type='markdown', verbose_name='text')

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return 'Deadline <{}> on {}'.format(self.title, str(self.subject))
