import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

BASE_CRAIGSLIST_URL= 'https://jaipur.craigslist.org/search/?query={}'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')    #request.POST returns a dictionary
    context={
        'search' : search
    }
    return  render(request, 'my_app/new_search.html', context)