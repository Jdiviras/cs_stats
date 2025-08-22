from django.db import models

# Create your models here.
class Stat(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    value = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "Stat"
        verbose_name_plural = "Stats"
    
    def __str__(self):
        return self.name
