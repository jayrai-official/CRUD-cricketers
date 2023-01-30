from django.shortcuts import render,HttpResponseRedirect
from databook.models import Cricketer

# Create your views here.

# homep page operations code 
def home(request):
    if request.method == 'POST':
        fetched_name = request.POST['name']
        fetched_origin_country = request.POST['origin-country']
        fetched_jersey_no = request.POST['jersey-no']

        regsiter = Cricketer(name = fetched_name,country=fetched_origin_country,jersey_no=fetched_jersey_no)
        regsiter.save()

    stored_data = Cricketer.objects.all()
    return render(request,'databook/index.html',{'cricketers':stored_data})

# delete data code 
def delete_data(request,id):
    if request.method == 'POST':
        data = Cricketer(pk=id)
        data.delete()
    return HttpResponseRedirect('/')

# update data code 
def update_data(request,id):
    if request.method == 'POST':
        get_data = Cricketer.objects.get(pk=id)
        fetched_name = request.POST['name']
        fetched_country = request.POST['origin-country']
        fetched_jersey_no = request.POST['jersey-no']

        get_data.name = fetched_name
        get_data.country = fetched_country
        get_data.jersey_no = fetched_jersey_no

        get_data.save()

        return HttpResponseRedirect('/')
    else:
        get_data = Cricketer.objects.get(pk=id)
        return render(request,'databook/update.html',{'data':get_data})

