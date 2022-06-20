from django import template
register = template.Library()

@register.filter(name='is_in_wishlist')
def is_in_wishlist(product,wishlist):
	keys = wishlist.keys()
	for id in keys:
		if int(id) == product.id:
			return True
	return False

@register.filter(name='wishlist_quantity')
def wishlist_quantity(product,wishlist):
	keys = wishlist.keys()
	for id in keys:
		if int(id) == product.id:
			return wishlist.get(id)
	return 0

@register.filter(name='price_subtotal')
def price_subtotal(product,wishlist):
	keys = wishlist.keys()
	for id in keys:
		if int(id) == product.id:
			return int(wishlist.get(id))*product.price

@register.filter(name='price_total')
def price_total(products,wishlist):
	total = 0
	for p in products:
		total += price_subtotal(p,wishlist)

	return total

@register.filter(name="currency")
def currency(number):
	return "₹"+str(number)


@register.filter(name="multipy")
def multipy(num,num2):
	return num*num2
