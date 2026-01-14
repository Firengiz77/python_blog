from django.db import models
from django.contrib.auth.models import User

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



STATUS_CHOISES = (
    (0, 'Deactive'),
    (1, 'Active')
)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/blog/%Y/%d/%m")
    description = models.TextField(max_length=2000)
    status = models.IntegerField(choices=STATUS_CHOISES, default=0)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    


