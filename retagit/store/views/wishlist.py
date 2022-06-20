from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product

class Wishlist(View):
	def get(self,request):
		productList = list(request.session.get('wishlist').keys())
		#if request.GET.get('increase'):
		#	pId = request.GET.get('increase')
		#	products = request.session.get('cart')
		#	products[pId] += 1
		#	request.session['cart'] = products

		if request.GET.get('decrease'):
			pId = request.GET.get('decrease')
			products = request.session.get('wishlist')
			print(products[pId])
			# if products[pId] > 1:
			# 	products[pId] -= 1
			# 	request.session['cart'] = products
			# 	productList = list(request.session.get('cart').keys())

			del products[pId]
			request.session['wishlist'] = products
			productList = list(request.session.get('wishlist').keys())

		allProduct = Product.getProductById(productList)
		return render(request,'wishlist.html',{"allProduct":allProduct})
