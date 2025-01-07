from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from authentication.models import User
from constants import *
from academics.models import *
from dashboard.models import *
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    description = models.TextField(_(""))
    amount = models.DecimalField(_(""), max_digits=5, decimal_places=2)
    date = models.DateTimeField(_(""), auto_now=True, auto_now_add=True)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
