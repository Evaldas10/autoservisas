from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CarMake(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.make.name} {self.name}"


# ---------------- CAR ----------------

class Car(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="cars"
    )
    make = models.ForeignKey(CarMake, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True)
    license_plate = models.CharField(max_length=50)
    vin_code = models.CharField(max_length=100)
    client_name = models.CharField(max_length=255)

    phone = models.CharField(max_length=20, default="")  # <-- nauja

    description = models.TextField(default="")
    cover = models.ImageField(upload_to="covers", null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} {self.license_plate}"


# ---------------- ORDER ----------------

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    car = models.ForeignKey(
        "Car",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    deadline = models.DateTimeField(null=True, blank=True)

    ORDER_STATUS = (
        ('p', 'Pending'),
        ('i', 'In Progress'),
        ('c', 'Completed'),
        ('x', 'Cancelled'),
    )

    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        default='p',
        blank=True
    )

    due_back = models.DateField(null=True, blank=True)

    reader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def total(self):
        return sum(line.line_sum() for line in self.lines.all())

    def __str__(self):
        return f"{self.date} - {self.car}"


# ---------------- ORDER LINE ----------------

class OrderLine(models.Model):
    order = models.ForeignKey(
        "Order",
        on_delete=models.CASCADE,
        related_name="lines"
    )

    service = models.ForeignKey(
        "Service",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    quantity = models.IntegerField(default=1)

    def line_sum(self):
        if self.service:
            return self.service.price * self.quantity
        return 0


# ---------------- SERVICE ----------------

class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# ---------------- COMMENTS ----------------

class CarComment(models.Model):
    car = models.ForeignKey(
        "Car",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="comments"
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["-date_created"]


# ---------------- USER ----------------

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profile_pics", null=True, blank=True)
