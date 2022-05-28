
import sys
import os
from pathlib import Path
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent
with open("try.txt", "w") as f:
    print(BASE_DIR, file=f)
    print(os.listdir(BASE_DIR), file=f)
sys.path.append(BASE_DIR)
  
import WeridText as WT

# Create your views here.

def code(request):
    return render(request, 'code.html')


def encode_run(request):
    text = WT.encode(request.GET['text_to_encode'])
    return render(request, 'result.html', {"result" : text })

def decode_run(request):
    text = request.GET['text_to_decode']
    text = WT.decode(text, text_sep = '\r\n—weird—\r\n')
    return render(request, 'result.html', {"result" : text })