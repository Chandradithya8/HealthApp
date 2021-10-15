import pickle
import numpy as np

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .models import Heart_Disease, Diabetes, Liver
from .models import Kidney, Cancer, Covid

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# Create your views here.

# heart

def heart(request):
    if request.method == "POST":
        age = request.POST['age']
        gender = request.POST.get('gender', False)
        chest_pain_type = request.POST.get('chest_pain_type', False)
        resting_blood_pressure = request.POST['resting_blood_pressure']
        cholestrol = request.POST['cholestrol']
        fasting_blood_sugar = request.POST['fasting_blood_sugar']
        resting_ecg = request.POST.get('resting_ecg', False)
        heart_rate = request.POST['heart_rate']
        excersise_induced_angina = request.POST.get(
            'excersise_induced_angina', False)
        st_depression = request.POST['st_depression']
        st_segment = request.POST.get('st_segment', False)
        major_vessels = request.POST.get('major_vessels', False)
        thal = request.POST['thal']

        heart = Heart_Disease(age=age, gender=gender, chest_pain_type=chest_pain_type,
                              resting_blood_pressure=resting_blood_pressure, cholestrol=cholestrol,
                              fasting_blood_sugar=fasting_blood_sugar, resting_ecg=resting_ecg,
                              heart_rate=heart_rate, excersise_induced_angina=excersise_induced_angina,
                              st_depression=st_depression, st_segment=st_segment, major_vessels=major_vessels,
                              thal=thal)
        heart.save()

        # model building

        if gender == 'Male' or gender == False:
            gender = 0
        else:
            gender = 1

        if chest_pain_type == "Typical anglina" or chest_pain_type == False:
            chest_pain_type = 1
        elif chest_pain_type == "Atypical anglina":
            chest_pain_type = 2
        elif chest_pain_type == "Non anglina":
            chest_pain_type = 3
        else:
            chest_pain_type = 4

        if resting_ecg == "Normal" or resting_ecg == False:
            resting_ecg = 0
        elif resting_ecg == "ST-T wave abnormality":
            resting_ecg = 1
        else:
            resting_ecg = 2

        if excersise_induced_angina == "Yes" or excersise_induced_angina == False:
            excersise_induced_angina = 1
        else:
            excersise_induced_angina = 0

        if st_segment == "Unsloping" or st_segment == False:
            st_segment = 1
        elif st_segment == "Flat":
            st_segment = 2
        else:
            st_segment = 3

        model = pickle.load(open('static/pickle files/healthcare/heart_disease.pkl', 'rb'))
        features = [[age, gender, chest_pain_type, resting_blood_pressure, cholestrol,
                     fasting_blood_sugar, resting_ecg, heart_rate, excersise_induced_angina, st_depression,
                     st_segment, major_vessels, thal]]
        prediction = model.predict(features)

        if prediction == 0:
            result = 'CONGRATULATIONS! YOU DONT HAVE HEART DISEASE'

        else:
            result = 'OOPS! YOU MAY HAVE HEART DISEASE'

        data = {
            'result': result,

        }

        return render(request, 'healthcare/result.html', data)

    return render(request,'healthcare/heart.html')

# diabetes

def diabetes(request):
    if request.method == 'POST':
        pregnancies = request.POST['pregnancies']
        glucose_level = request.POST['glucose_level']
        blood_pressure = request.POST['blood_pressure']
        skinthickness = request.POST['skinthickness']
        insulin = request.POST['insulin']
        bmi = request.POST['bmi']
        DiabetesPedigreeFunction = request.POST['DiabetesPedigreeFunction']
        age = request.POST['age']

        diabetes = Diabetes(pregnancies=pregnancies, glucose_level=glucose_level, blood_pressure=blood_pressure,
                            skinthickness=skinthickness, insulin=insulin, bmi=bmi, DiabetesPedigreeFunction=DiabetesPedigreeFunction,
                            age=age)
        diabetes.save()

        model = pickle.load( open('static/pickle files/healthcare/diabetes_prediction.pkl', 'rb'))
        features = [[pregnancies, glucose_level, blood_pressure,
                     skinthickness, insulin, bmi, DiabetesPedigreeFunction, age]]
        prediction = model.predict(features)

        if prediction == 0:
            result = 'CONGRATULATIONS! YOU DONT HAVE DIABETES'

        else:
            result = 'OOPS! YOU MAY HAVE DIABETES'

        data = {
            'result': result,

        }

        return render(request, 'healthcare/result.html', data)

    return render(request, 'healthcare/diabetes.html')


# liver 

def liver(request):
    if request.method == 'POST':
        age = request.POST['age']
        gender = request.POST.get('gender', False)
        bilirubin = request.POST['bilirubin']
        direct_bilirubin = request.POST['direct_bilirubin']
        alkaline_phosphotase = request.POST['alkaline_phosphotase']
        alamine_aminotransferase = request.POST['alamine_aminotransferase']
        aspartate_aminotransferase = request.POST['aspartate_aminotransferase']
        total_proteins = request.POST['total_proteins']
        albumin = request.POST['albumin']
        albumin_and_globulin_ratio = request.POST['albumin_and_globulin_ratio']

        liver = Liver(age=age, gender=gender, bilirubin=bilirubin, direct_bilirubin=direct_bilirubin,
                      alkaline_phosphotase=alkaline_phosphotase, alamine_aminotransferase=alamine_aminotransferase,
                      aspartate_aminotransferase=aspartate_aminotransferase, total_proteins=total_proteins,
                      albumin=albumin, albumin_and_globulin_ratio=albumin_and_globulin_ratio)

        liver.save()

        if gender == 'Male' or gender == False:
            gender = 1
        else:
            gender = 0

        model = pickle.load(
            open('static/pickle files/healthcare/liver_disease.pkl', 'rb'))
        features = [[age, gender, bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
                     aspartate_aminotransferase, total_proteins, albumin, albumin_and_globulin_ratio]]

        prediction = model.predict(features)
        if prediction == 1:
            result = 'CONGRATULATIONS! YOU DONT HAVE LIVER DISEASE'

        else:
            result = 'OOPS! YOU MAY HAVE LIVER DISEASE'

        data = {
            'result': result,

        }

        return render(request, 'healthcare/result.html', data)

    return render(request,'healthcare/liver.html')


# kidney

def kidney(request):
    if request.method == 'POST':
        age = request.POST['age']
        wbc_count = request.POST['wbc_count']
        blood_urea = request.POST['blood_urea']
        appetite = request.POST.get('appetite', False)
        blood_glucose_random = request.POST['blood_glucose_random']
        pus_cell_clumps = request.POST.get('pus_cell_clumps', False)
        hypertension = request.POST.get('hypertension', False)
        anemia = request.POST.get('anemia', False)
        packed_cell_volume = request.POST['packed_cell_volume']
        blood_pressure = request.POST['blood_pressure']

        kidney = Kidney(age=age, wbc_count=wbc_count, blood_urea=blood_urea, appetite=appetite,
                        blood_glucose_random=blood_glucose_random, pus_cell_clumps=pus_cell_clumps, hypertension=hypertension,
                        anemia=anemia, packed_cell_volume=packed_cell_volume, blood_pressure=blood_pressure)

        kidney.save()

        if appetite == "Good" or appetite == False:
            appetite = 0
        else:
            appetite = 1

        if pus_cell_clumps == "Present" or pus_cell_clumps == False:
            pus_cell_clumps = 1
        else:
            pus_cell_clumps = 0

        if hypertension == 'Yes' or hypertension == False:
            hypertension = 1
        else:
            hypertension = 0

        if anemia == 'Yes' or anemia == False:
            anemia = 1
        else:
            anemia = 0

        model = pickle.load(
            open('static/pickle files/healthcare/kidney_disease.pkl', 'rb'))
        features = [[age, wbc_count, blood_urea, appetite, blood_glucose_random, pus_cell_clumps,
                     hypertension, anemia, packed_cell_volume, blood_pressure]]

        prediction = model.predict(features)
        if prediction == 0:
            result = 'CONGRATULATIONS! YOU DONT HAVE KIDNEY DISEASE'

        else:
            result = 'OOPS! YOU MAY HAVE KIDNEY DISEASE'

        data = {
            'result': result,

        }

        return render(request, 'healthcare/result.html', data)

    return render(request, 'healthcare/kidney.html')


# cancer

def cancer(request):
    if request.method == "POST":
        area_worst = request.POST['area_worst']
        area_mean = request.POST['area_mean']
        area_standard_error = request.POST['area_standard_error']
        perimeter_worst = request.POST['perimeter_worst']
        perimeter_mean = request.POST['perimeter_mean']
        radius_worst = request.POST['radius_worst']
        radius_mean = request.POST['radius_mean']
        perimeter_standard_error = request.POST['perimeter_standard_error']
        texture_worst = request.POST['texture_worst']
        texture_mean = request.POST['texture_mean']

        cancer = Cancer(area_worst=area_worst, area_mean=area_mean, area_standard_error=area_standard_error,
                        perimeter_worst=perimeter_worst, perimeter_mean=perimeter_mean, radius_worst=radius_worst,
                        radius_mean=radius_mean, perimeter_standard_error=perimeter_standard_error, texture_worst=texture_worst,
                        texture_mean=texture_mean)

        cancer.save()

        model = pickle.load(
            open('static/pickle files/healthcare/cancer_disease.pkl', 'rb'))

        features = [[area_worst, area_mean, area_standard_error, perimeter_worst, perimeter_mean, radius_worst,
                     radius_mean, perimeter_standard_error, texture_worst, texture_mean]]

        prediction = model.predict(features)

        if prediction == 0:
            result = 'CONGRATULATIONS! YOU DONT HAVE BREAST CANCER DISEASE'

        else:
            result = 'OOPS! YOU MAY HAVE BREAST CANCER DISEASE'

        data = {
            'result': result,

        }

        return render(request, 'healthcare/result.html', data)

    return render(request,'healthcare/cancer.html')


# covid

def covid(request):
    if request.method == "POST":
        fs = FileSystemStorage()
        fileobj = request.FILES['covid_image']
        file_name = fileobj.name
        file_name = file_name.replace(" ","")
        filepath = fs.save(file_name,fileobj)
        filepath = fs.url(filepath)
        # print(type(filepath))
        filepath = filepath[1:]

        covid = Covid(photo=fileobj)
        covid.save()

        model_path = 'static/h5 files/covid_detection_model.h5'
        img = image.load_img(filepath, target_size=[224, 224])
        x = image.img_to_array(img)
        x = x/255
        x = np.expand_dims(x, axis=0)
        model = load_model(model_path)
        preds = model.predict(x)
        if preds > 0.5:
            # print('positive')
            result = "OOPS YOU MAY HAVE COVID DISEASE"
        else:
            # print('negative')
            result = "CONGRATULATIONS YOU DON'T HAVE COVID DISEASE"

        data = {
            'result' : result
        }
        return render(request, 'healthcare/result.html', data)

        # return render(request, 'webpages/home.html')

    return render(request, 'healthcare/covid.html')

 
