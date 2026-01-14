from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # admin paneldeki model adini deyisdirmek ucundu
    class Meta:
        verbose_name_plural = 'categories'

    # admin panelde sutunun adini deyisdirmek ucundu
    def __str__(self):
        return self.name    