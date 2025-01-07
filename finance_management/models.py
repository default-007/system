from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from authentication.models import User
from constants import *
from academics.models import *
from dashboard.models import *
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    description = models.TextField(_("description"))
    amount = models.DecimalField(_("amount"), max_digits=5, decimal_places=2)
    date = models.DateTimeField(_("date"), auto_now=True, auto_now_add=True)

    class Meta:
        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Expense_detail", kwargs={"pk": self.pk})


class FeeComponent(models.Model):
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"))

    class Meta:
        verbose_name = _("FeeComponent")
        verbose_name_plural = _("FeeComponents")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("FeeComponent_detail", kwargs={"pk": self.pk})


class FeeStructure(models.Model):

    class Meta:
        verbose_name = _("FeeStructure")
        verbose_name_plural = _("FeeStructures")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("FeeStructure_detail", kwargs={"pk": self.pk})
