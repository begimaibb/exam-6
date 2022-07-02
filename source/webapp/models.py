from django.db import models

# Create your models here.


class Guest(models.Model):
    status_choices = [('active', 'Active'), ('blocked', 'Blocked')]
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Name")
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="Email")
    text = models.TextField(max_length=100, null=False, blank=False, verbose_name="Text")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated date")
    status = models.CharField(max_length=50, choices=status_choices, default='1')


    def __str__(self):
        return f"{self.id}. {self.name}, {self.email} {self.text}"

    class Meta:
        db_table = "guests"
        verbose_name = "Guest"
        verbose_name_plural = "Guests"

