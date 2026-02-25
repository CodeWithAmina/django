from django.shortcuts import render, get_object_or_404, redirect
from .forms import SimpleForm
from .models import Contact


# CREATE
def contact_create(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            Contact.objects.create(name=name, email=email)
            return redirect('contact_list')
    else:
        form = SimpleForm()
    return render(request, 'contact_form.html', {'form': form})


# READ - List all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


# READ - Get single contact
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})


# UPDATE
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = SimpleForm(initial={'name': contact.name, 'email': contact.email})
    return render(request, 'contact_form.html', {'form': form, 'contact': contact})


# DELETE
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})