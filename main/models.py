from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# Create your models here.


class Userprofile(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	profile_photo = models.ImageField(upload_to='images/',null=True,blank=True)
	phone_number = models.CharField(max_length=17, null=True, blank=True)
	stripe_customer_id = models.CharField(max_length=50, null=True, blank=True)
	one_click_purchasing = models.SmallIntegerField()

	def __str__(self):
		return self.user.username

class Supplier(models.Model):
	profile = models.ForeignKey(Userprofile, on_delete = models.CASCADE)
	title = models.CharField(max_length=100)

	def __str__(self):
		return str(self.profile.user)

class Search(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	search = models.CharField(max_length=100)


class Payment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stripe_charge_id = models.CharField(max_length=50)
	amount = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username

class Coupon(models.Model):
	code = models.CharField(max_length=15)
	amount = models.FloatField()

	def __str__(self):
		return self.code

class Category(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	def __str__(self):
		return self.name

class Color(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Brand(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Address(models.Model):
 	user = models.ForeignKey(User, on_delete=models.CASCADE)
 	street_address = models.CharField(max_length=100)
 	apartment_address = models.CharField(max_length=100)
 	country = models.CharField(max_length=2)
 	zipcode = models.CharField(max_length=100)
 	address_type = models.CharField(max_length=1)
 	de_fault = models.SmallIntegerField()

 	def __str__(self):
 		return self.user.username


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	billing_address = models.ForeignKey(Address, related_name="billing_adddress",on_delete=models.CASCADE)
	coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
	payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
	shipping_address = models.ForeignKey(Address, related_name="shipping_address", on_delete=models.CASCADE)


	ref_code = models.CharField(max_length=20)
	start_date = models.DateTimeField()
	ordered_date = models.DateTimeField()
	ordered = models.SmallIntegerField()
	being_delivered = models.SmallIntegerField()
	received = models.SmallIntegerField()
	refund_requested = models.SmallIntegerField()
	refund_granted = models.SmallIntegerField()

	def __str__(self):
		return self.user.username


class Product(models.Model):
	vendor = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	supplier =  models.ForeignKey(Supplier, on_delete=models.CASCADE)
	color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
	

	name = models.CharField(max_length=100)
	price = models.FloatField()
	discount_price = models.FloatField(null=True,blank=True)
	label = models.CharField(max_length=1)
	slug = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to='images/',)
	orders = models.IntegerField()
	stock = models.IntegerField()
	reorder_level = models.IntegerField()
	def __str__(self):
		return self.name


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return self.user.username

		
class Wishlist(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return self.user.username

class Refund(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	reason = models.TextField() 
	accepted = models.SmallIntegerField()
	email = models.CharField(max_length=254)


class Ads(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	banner = models.CharField(max_length=100)
	adtext = models.TextField()


class Orderitem(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	ordered = models.SmallIntegerField()
	quantity = models.IntegerField()

	def __str__(self):
		return self.user.username

class Order_items(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	orderitem = models.ForeignKey(Orderitem, on_delete=models.CASCADE)

	def __str__(self):
		return self.order
