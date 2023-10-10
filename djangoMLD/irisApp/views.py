from django.shortcuts import render
from joblib import load
model = load('./savedmodel/model.joblib')

def Predictor(request):
    return render(request, 'main.html')

def FormInfo(request):
    sepallength = request.POST['sepallength']
    sepalwidth = request.POST['sepalwidth']
    petallength = request.POST['petallength']
    petalwidth = request.POST['petalwidth']
    y_predict = model.predict([[sepallength, sepalwidth, petallength, petalwidth]])
    if(y_predict[0] == 0):
        y_predict = 'setosa'
    elif(y_predict[0] == 1):
        y_predict = 'versicolor'
    else:
        y_predict = 'verginica'
    return render(request, 'result.html', {'prediction': y_predict})