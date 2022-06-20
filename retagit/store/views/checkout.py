from django.shortcuts import render, redirect
from django.views import View
from store.models import Order
from store.models import Customer
from store.models import Product


class Checkout(View):
	def get(self,request):
		return redirect('cart')

	def post(self,request):
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		cart = request.session.get('cart')
		products = Product.getProductById(list(cart.keys()))
		customer = request.session.get('customer')
		print(address,phone,cart,products,customer)

		for product in products:
			newOrder = Order(
					product=product,
					customer=Customer(id=customer),
					quantity=cart[str(product.id)],
					price=product.price,
					address=address,
					phone=phone,
				)
			newOrder.save()

		for product in products:
			newOr = Product.objects.get(
					name=product.name
					# customer=Customer(id=customer),
					# quantity=cart[str(product.id)],
					# price=product.price,
					# address=address,
					# phone=phone,
					#
					# productID = Product(id)
					# name = models.CharField(max_length=220)
					# price = models.IntegerField(default=0)
					# category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
					# description = models.TextField()
					# image = models.ImageField(upload_to='upload/products')
					# date = models.DateTimeField(auto_now_add=True)
				)
			#newOr.delete()

		request.session['cart'] = {}
		return redirect('order')
