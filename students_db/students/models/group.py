from django.db import models
from django.core.exceptions import ValidationError


class Group(models.Model):
    """Group model"""

    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"
        ordering = ['title']

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Група",
        unique=True
    )

    leader = models.OneToOneField(
        'Student',
        verbose_name=u"Староста",
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
            return u"%s(%s, %s)" % (
                self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u"%s" % (self.title)

    def clean(self):
        """Validation for group"""

        # if len(Group.objects.filter(title=self.title)) > 0:
        #     raise ValidationError({'title': ('group exists')})

        if self.leader == None:
            raise ValidationError({'leader': ('input the group leader')})
