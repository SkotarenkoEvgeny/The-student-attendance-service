from django.db import models


class Exams(models.Model):
    """exams models"""

    class Meta(object):
        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"

    subjekt_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва іспиту"
    )

    date_time = models.DateTimeField(
        blank=False,
        verbose_name=u"Дата іспиту"
    )

    teacher_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач"
    )

    title = models.OneToOneField(
        "Group",
        max_length=256,
        blank=False,
        verbose_name=u"Група"
    )

