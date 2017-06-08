from django.db import models


class Street(models.Model):
    name = models.CharField(max_length=255)
