import requests
from django.http import JsonResponse
from django.shortcuts import render

def fetch_data(request):
    url = 'https://dummyjson.com/products'  
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        return render(request,"index.html",{"data":data})
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)
    
