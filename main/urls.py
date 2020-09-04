from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('dynamic',views.dynamic, name='dynamic'),
    path('createup',views.createup,name='createup'),
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('checkout', views.checkout, name='checkout'),
    path('cart', views.cart, name='cart'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('bigsearch', views.bigsearch, name='bigsearch'),
    path('filtersearch', views.filtersearch, name='filtersearch'),
    path('search', views.search, name='search'),
    path('singleproduct/<str:id>', views.singleproduct, name='singleproduct'),
    path('addtocart/<str:id>', views.addtocart, name='addtocart'),
    path('addtowishlist/<str:id>', views.addtowishlist, name='addtowishlist'),
    path('removefromcart/<str:id>', views.removefromcart, name='removefromcart'),
    path('removefromwishlist/<str:id>', views.removefromwishlist, name='removefromwishlist'),
    path('createproduct',views.createproduct, name='createproduct'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('deletecategory/<str:id>', views.deletecategory, name='deletecategory'),
    path('addcategory', views.addcategory, name='addcategory'),
    path('vendor',views.vendor, name='vendor'),
    path('vendorprofile',views.vendorprofile, name='vendorprofile'),
   
    path('deleteproduct/<str:id>',views.deleteproduct,name='deleteproduct'),
    path('listproduct',views.listproduct,name='listproduct'),
    path('gostore',views.gostore, name='gostore')


    ]