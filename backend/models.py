from django.core.exceptions import ValidationError
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Trip(models.Model):
    name = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def clean(self) -> None:
        if self.start > self.end:
            raise ValidationError("Start should be before end")
        return super().clean()
