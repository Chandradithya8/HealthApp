from django.db import models
from django.utils import timezone

# Create your models here.


class Heart_Disease(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    chest_pain_type = models.CharField(max_length=100)
    resting_blood_pressure = models.IntegerField()
    cholestrol = models.IntegerField()
    fasting_blood_sugar = models.IntegerField()
    resting_ecg = models.CharField(max_length=100)
    heart_rate = models.IntegerField()
    excersise_induced_angina = models.CharField(max_length=100)
    st_depression = models.IntegerField()
    st_segment = models.CharField(max_length=100)
    major_vessels = models.CharField(max_length=100)
    thal = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.age)


class Diabetes(models.Model):
    pregnancies = models.IntegerField()
    glucose_level = models.IntegerField()
    blood_pressure = models.IntegerField()
    skinthickness = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.IntegerField()
    DiabetesPedigreeFunction = models.IntegerField()
    age = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.age)


class Liver(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    bilirubin = models.IntegerField()
    direct_bilirubin = models.IntegerField()
    alkaline_phosphotase = models.IntegerField()
    alamine_aminotransferase = models.IntegerField()
    aspartate_aminotransferase = models.IntegerField()
    total_proteins = models.IntegerField()
    albumin = models.IntegerField()
    albumin_and_globulin_ratio = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.age)


class Kidney(models.Model):
    age = models.IntegerField()
    wbc_count = models.IntegerField()
    blood_urea = models.IntegerField()
    appetite = models.CharField(max_length=100)
    blood_glucose_random = models.IntegerField()
    pus_cell_clumps = models.CharField(max_length=100)
    hypertension = models.CharField(max_length=100)
    anemia = models.CharField(max_length=100)
    packed_cell_volume = models.IntegerField()
    blood_pressure = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.age)


class Cancer(models.Model):
    area_worst = models.IntegerField()
    area_mean = models.IntegerField()
    area_standard_error = models.IntegerField()
    perimeter_worst = models.IntegerField()
    perimeter_mean = models.IntegerField()
    radius_worst = models.IntegerField()
    radius_mean = models.IntegerField()
    perimeter_standard_error = models.IntegerField()
    texture_worst = models.IntegerField()
    texture_mean = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.area_worst)


class Covid(models.Model):
    photo = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)
