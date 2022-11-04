from django.shortcuts import render

# Create your views here.
from .models import *


def get_data(request):

    my_data = Table.objects.all() 
    print(my_data)
    return render(request, 'index.html', {'my_data':my_data})

