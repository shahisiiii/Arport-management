from django.db import models

class Airport(models.Model):
    STATUS_CHOICES = [
        ("L", "left"),
        ("R", "right")
    ]

    code = models.CharField(max_length=255, unique=True)
    parent_code = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='child_airports'
    )
    parent_position = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        null=True,
        blank=True
    )
    duration = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.code
