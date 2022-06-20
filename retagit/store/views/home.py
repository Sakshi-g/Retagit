from django.shortcuts import render,redirect
from django.views import View
from store.models import Product
from store.models import Order
from store.models import Category

class Home(View):

	def get(self,request):
		cart = request.session.get('cart')
		wishlist = request.session.get('wishlist')
		categories = Category.getAllCategory()
		products = Product.getAllProduct().order_by('-id')
		orders = Order.getAllOrder().order_by('-id')
		#p = products.value_list('Product')
		#p = set(products[0]['Product']).difference(set(orders[0]['Order']))
		#q = p.getProductById().order_by('-id')

		print(products)
		print(orders)
		# print(p)
		# print(q)

		if request.GET.get('id'):
			filterProductById = Product.objects.get(id=int(request.GET.get('id')))
			return render(request, 'productDetail.html',{"product":filterProductById,"categories":categories})

		if not cart:
			request.session['cart'] = {}

		if not wishlist:
			request.session['wishlist'] = {}

		if request.GET.get('category_id'):
			filterProduct = Product.getProductByFilter(request.GET['category_id'])
			return render(request, 'home.html',{"products":filterProduct,"categories":categories})

		return render(request, 'home.html',{"products":products,"categories":categories})

	def post(self,request):
		product = request.POST.get('product')

		cart = request.session.get('cart')
		wishlist = request.session.get('wishlist')
		if wishlist:

			quantity = wishlist.get(product)
			if quantity:
				wishlist[product] = quantity+1
			else:
				wishlist[product] = 1
		else:
			wishlist = {}
			wishlist[product] = 1
		if cart:
			quantity = cart.get(product)
			if quantity:
				cart[product] = quantity+1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1

		print(cart)
		print(wishlist)

		if cart:
			request.session['cart'] = cart
			#return redirect('cart')
		if wishlist:
			request.session['wishlist'] = wishlist
			#return redirect('wishlist')
		return redirect('cart')
		return redirect('wishlist')
