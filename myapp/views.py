from django.shortcuts import render

# Create your views here.

def product_list(request):
    product_key_list = ['ID','Name','Description','Price']
    product_dict = {'Name': 'Moto E3 Power',
                    'ID':1234,
                    'Price': 8000,
                    'Description': '8MB Camera'}
    return render(request, 'index.html', {'product_dict': product_dict, 
                                          'product_key_list':product_key_list })
