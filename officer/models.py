from django.db import models



# Create your models here.

class Seminar(models.Model):
    sem_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    conducted_by = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Fertilizer(models.Model):
    fert_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='fertilizer')
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Irrigation(models.Model):
    irri_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='irrigation')
    price = models.IntegerField(verbose_name='Price', default=0)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Pesticide(models.Model):
    PTYPE = (
        ('Fungicide', 'Fungicide'),
        ('Insecticide', 'Insecticide'),
        ('Herbicide', 'Herbicide'),
        ('Nematicide', 'Nematicide'),
        ('Rodenticide', 'Rodenticide'),
        ('Acaricide', 'Acaricide'),
        ('Molluscicide', 'Molluscicide'),
        ('Bactericide', 'Bactericide'),
        ('Algalicide', 'Algalicide'),
        ('Avicide', 'Avicide'),
    )
    pest_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=100, choices=PTYPE)
    image = models.ImageField(upload_to='pesticide')
    price = models.IntegerField(verbose_name='Price', default=0)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Crops(models.Model):
    crop_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='crops')
    season = models.CharField(max_length=100, verbose_name='Season', default=None)
    climate = models.CharField(max_length=100, verbose_name='Climate', default=None)
    soil = models.CharField(max_length=100, verbose_name='Soil', default=None)
    price = models.IntegerField(verbose_name='Price', default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Scheme(models.Model):
    gov_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Scheme Name')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
