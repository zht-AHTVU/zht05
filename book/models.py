from django.db import models

# Create your models here.

class AreaInfo(models.Model):
    area_name = models.CharField(max_length=20)
    area_parent = models.ForeignKey('self', on_delete=True, null=True, blank=True)
