from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse
# Create your views here.

def product_list(request):
    api_url = "http://127.0.0.1:8000/api/products/"
    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            products = response.json()  
        except requests.exceptions.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON response from API"}, status=500)
    else:
        return JsonResponse({"error": "Failed to fetch API data"}, status=response.status_code)

    return render(request, "product_list.html", {"products": products})
def category_list(request):
    response = requests.get('http://127.0.0.1:8000/api/categories/')
    categories = response.json()
    return render(request, 'category_list.html', {'categories': categories})

def order_list(request):
    response = requests.get('http://127.0.0.1:8000/api/orders/')
    orders = response.json()
    return render(request, 'order_list.html', {'orders': orders})

def add_to_order(request, product_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        requests.post('http://127.0.0.1:8000/api/orders/', data={
            'product': product_id,
            'quantity': quantity,
        })
    return redirect('product_list')