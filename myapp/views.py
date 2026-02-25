from django.shortcuts import render
from .forms import SimpleForm
from .models import Contact


def simple_form(request):
    form = SimpleForm()
    if request.method=='POST':
        form=SimpleForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            Contact.objects.create(name=name, email=email)
            return render(request,"success.html",{'name':name})
    return render(request,"form.html",{'form':form})