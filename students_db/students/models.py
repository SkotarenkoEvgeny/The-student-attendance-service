from django.db import models

# Create your models here.
class Student(models.Model):
    """Student model"""

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"


    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name= u"Ім’я"
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище"
    )

    midle_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"По батькові"
    )

    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name=True,
        null=True)

    ticket = models.IntegerField(
        blank=False,
        verbose_name=u"Білет"
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки"
    )

    student_group = models.ForeignKey(
        'Group',
        verbose_name=u"Група",
        blank = False,
        null = True,
        on_delete = models.PROTECT
    )

    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    """
    Group model
    """

    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва"
    )

    leader = models.OneToOneField(
        'Student',
        verbose_name=u"Старовста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові дані"
    )

    def __str__(self):
        if self.leader:
            return u"%s(%s, %s)"%(self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u"%s"%(self.title)