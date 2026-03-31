from django.db import models
# from django.contrib.auth.models import User
# import uuid
# from django.utils import timezone
# from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


# pirma lentele


class Car(models.Model):

    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField()
    vin_code = models.CharField()
    client_name = models.CharField()
    description = models.TextField(default="")
    cover = models.ImageField(upload_to="covers", null=True, blank=True)
    # owner = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True
    # )
    # def display_(pavadinimas koki sukursi)(self):
    #     pavadinimas koki sukursi = self.pavadinimas koki sukursi.all()
    #     result = ""
    #     for  pavadinimas koki sukursi in pavadinimas koki sukursi:
    #       result += pavadinimas koki sukursi.name + ","
    #     return result
    # sukuria virtualius stulpeliu duombazei

    def __str__(self):
        return f"{self.make} {self.model} {self.license_plate}"


# ORM (object related mapping) - automatinis python klasių susiejimas su DB lentelėmis

# ------------------------------------------------------

# sukuriame antra lentele

class Order(models.Model):
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    car = models.ForeignKey(
        to="Car", on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateTimeField(
        verbose_name="Deadline", null=True, blank=True)

    ORDER_STATUS = (
        ('p', 'Pending'),
        ('i', 'In Progress'),
        ('c', 'Completed'),
        ('x', 'Cancelled'),
    )

    status = models.CharField(
        verbose_name="Status", choices=ORDER_STATUS, blank=True, default="p")
    due_back = models.DateField(null=True, blank=True)
    reader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def total(self):
        return sum(line.line_sum() for line in self.lines.all())

    def __str__(self):
        return f"{self.date} - {self.car}"

# ----------------------------------------------------

# trecia lentele


class OrderLine(models.Model):
    order = models.ForeignKey(
        to="Order", on_delete=models.CASCADE, related_name="lines")
    service = models.ForeignKey(
        to="Service", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Quantity", default=1)

    def line_sum(self):
        return self.service.price * self.quantity

    def __str__(self):
        return f"{self.service.name} - {self.quantity} ({self.order.car}"
# ------------------------------------------------------
# ketvirta lentele


class Service(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class CarComment(models.Model):
    car = models.ForeignKey(to="Car", on_delete=models.SET_NULL,
                            null=True, blank=True, related_name="comments")

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["-date_created"]


# nuotraukos ikelimui

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profile_pics", null=True, blank=True)


# -----------------------------------------------------------------------
# teminale

# python manage.py makemigrations darys pakeitimus
# python manage.py migrate pakeitimai duomenu bazeje

# ------------------------------------------------------
# serverio paleidimas

# python manage.py runserver
