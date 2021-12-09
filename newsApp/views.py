from django.shortcuts import render
import requests

API_KEY = '#'
articles = ''

# Create your views here.
def home(request):
    # url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    country = request.GET.get('country') #textbox value of search by country
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    #print(data)
    context = {'articles': articles}

    return render(request,'newsApp/home.html', context)
