from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def register(requests):
    if requests.method == 'POST':
        form = RegistrationForm(requests.POST)
        if form.is_valid():
            form.save()

    elif requests.method == 'GET':
        form = RegistrationForm()

    return render(requests, 'users/register.html', {'form':form})