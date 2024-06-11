from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import pandas as pd

def home(request):


    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file=request.FILES['file']
        df = pd.read_csv(file)
        print(df.to_string())
    else:
        form = UploadFileForm()



    if (request.GET):
        data=request.GET['userText']
    else:
        data=' '
    return render(request, "home.html",{'KEY':data, 'form': form})