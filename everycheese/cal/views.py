from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import CalItem
from projects.convert_cal import handler
# Create your views here.
class UploadFileForm(forms.Form):
    file = forms.FileField(label="select a file to process")


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print form.cleaned_data
            cal = CalItem(uploadfile = form.cleaned_data['file'])
            cal.save()
            handler(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'cal/upload.html', {'form': form})

