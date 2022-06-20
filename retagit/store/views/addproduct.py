from django.shortcuts import render, redirect
from django.views import View
from store.models import Customer
from store.models import Order
from store.models import Product
from store.models import Category


class AddView(View):
    def get(self,request):
	        #return redirect('addprouct.html')
            return render(request,'addproduct.html')
    def post(self, request):
            name = request.POST.get('name')
            price = request.POST.get('price')
            category = request.POST.get('category')
            description = request.POST.get('description')
            image = request.FILES['image']
            newOrder = Product(
    		      name=name,
                  price= price,
                  category= Category(category),
                  description=description,
                  image=image
    		)
            newOrder.save()

            return redirect('home')
