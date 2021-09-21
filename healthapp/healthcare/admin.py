from django.contrib import admin
from django.utils.html import format_html
from .models import Heart_Disease, Diabetes, Liver
from .models import Kidney, Cancer, Covid

# Register your models here.


class Heart_Disease_customization(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender', 'chest_pain_type',
                    'resting_blood_pressure', 'cholestrol', 'fasting_blood_sugar']

    search_fields = ['age', 'gender']


class Diabetes_customization(admin.ModelAdmin):
    list_display = ['id', 'pregnancies', 'glucose_level',
                    'blood_pressure', 'skinthickness', 'insulin', 'age']

    search_fields = ['age', 'blood_pressure']


class Liver_customization(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender', 'bilirubin', 'direct_bilirubin',
                    'alkaline_phosphotase', 'alamine_aminotransferase']

    search_fields = ['age', 'gender']


class Kidney_customization(admin.ModelAdmin):
    list_display = ['id', 'age', 'wbc_count', 'blood_urea',
                    'appetite', 'blood_glucose_random', 'pus_cell_clumps']

    search_fields = ['age', 'wbc_count']


class Cancer_customization(admin.ModelAdmin):
    list_display = ['id', 'area_worst', 'area_mean',
                    'area_standard_error', 'perimeter_worst', 'perimeter_mean', 'radius_worst']

    search_fields = ['area_worst', 'area_mean']


class Covid_customization(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width=40 />'.format(object.photo.url))
    list_display = ['id', 'myphoto']


admin.site.register(Heart_Disease, Heart_Disease_customization)
admin.site.register(Diabetes, Diabetes_customization)
admin.site.register(Liver, Liver_customization)
admin.site.register(Kidney, Kidney_customization)
admin.site.register(Cancer, Cancer_customization)
admin.site.register(Covid, Covid_customization)

