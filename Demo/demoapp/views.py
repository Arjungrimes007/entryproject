from django.shortcuts import render
from django.views.decorators.cache import cache_page



@cache_page(60*1)
def home(request):
    return render(request,'index.html')

# Create your views here.
