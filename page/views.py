from django.shortcuts import render, redirect
from django.contrib import messages
from .form import Myform

#it cheaks if a file is a csv file by cheaking if it ends with .csv if it is not it shows a error massage else it saves in database and shows a sussess massege
def model_form_upload(request):
    if request.method == 'POST':
        form = Myform(request.POST, request.FILES)
        myfile = request.FILES['csv_file']
        if not myfile.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect('simple_upload')
        if form.is_valid():
            form.save()
            messages.success(request,'You CSV file is know saved')
            # you need to add this line to show the success massage in template
            success = True
            # messages.success(request, 'You CSV file is know saved')
            return redirect('simple_upload')
    else:
        form = Myform()
    return render(request, 'simple_upload.html', {
        'form': form
    })


