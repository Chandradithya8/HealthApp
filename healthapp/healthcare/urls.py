from django.urls import path
from . import views
 
urlpatterns = [
    path('heart_disease_prediction',views.heart,name="heart"),
    path('diabetes_prediction',views.diabetes,name='diabetes'),    
    path('liver_disease_prediction',views.liver,name='liver'),
    path('kidney_disease_prediction',views.kidney,name="kidney"),
    path('cancer_disease_prediction',views.cancer,name="cancer"),
    path('covid_disease_prediction',views.covid,name="covid"),
]

