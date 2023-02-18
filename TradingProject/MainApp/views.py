from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import File, Candle
from django.core.files.storage import default_storage
import csv
import json
import asyncio
from datetime import datetime, timedelta
import pandas as pd
# Create your views here.

def main(request):
    if request.method == "POST":
        timeframe = request.POST['timeframe']
        file = request.FILES['csv_file']
        File.objects.create(file=file)

        df = pd.read_csv(file, delimiter=',')
        df = df.resample(timeframe).agg({
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last",
        })
        print(df)
        
    return render (request, 'main.html')  


