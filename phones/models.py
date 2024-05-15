from django.db import models



class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True)