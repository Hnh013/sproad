from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .filters import ProductFilter

from .forms import CreateUserForm
# Create your views here.


def dynamic(request):
    products = Product.objects.all()
    myfilter = ProductFilter(request.GET, queryset=products)
    context = {'myfilter':myfilter}
    return render(request, 'dynamic.html', context)

def vendor(request):
    return render(request, 'vendor.html')

def vendorprofile(request):
    return render(request, 'pages-profile.html')


def listproduct(request):
    user=request.user
    products = Product.objects.filter(vendor=user)
    context = {'products':products}
    return render(request, 'my_product_listing.html', context)

def gostore(request):    
    cate = Category.objects.all()
    context = {'cate':cate}
    return render(request,'index.html', context)

def loginUser(request):
    cate = Category.objects.all()
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect!')
    context= {'cate':cate}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginUser')










def index(request):
    cate = Category.objects.all()

    products = Product.objects.all()
    context = {'products':products, 'cate':cate}
    return render(request,'index.html', context)

def singleproduct(request, id):
    cate = Category.objects.all()
    product = Product.objects.get(pk=id)
    context = {'product':product, 'cate':cate}
    return render(request,'single_product.html', context)



def about(request):
    return render(request,'about.html')

def contact(request):
    cate = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        comments = request.POST['comments']

        send_mail(
            subject,
            comments,
            email,
            ['specsotechnologies@gmail.com', 'ayushtyagi2139@gmail.com'],
            fail_silently=False
        )


        return render(request,'contact.html',{'name': name})
    else:
        context = {'cate':cate}
        return render(request,'contact.html',context)


def search(request):
    cate = Category.objects.all()
    if request.method == "POST":
        user = request.user
        query = str(request.POST['query'])
        result = Product.objects.filter(name__icontains=query)

        s_s = Search.objects.create(user=user,search=query)
        s_s.save()

        context= {'result':result,'cate':cate}

    else:
        context= {'cate':cate}
        return render(request,'search.html', context)

    context = {'cate':cate}

    return render(request,'search.html', context)


def addcategory(request):
    cate = Category.objects.all()
    all_cate = Category.objects.all()

    if request.method == "POST":
        name = str(request.POST['name'])
        description = str(request.POST['description'])

        new_cat = Category.objects.create(name=name,description=description)

        new_cat.save()

        return redirect('addcategory')

    else:
        context = {'all_cate':all_cate,'cate':cate}

        return render(request, 'category.html', context)
    context = {'all_cate':all_cate,'cate':cate}

    return render(request, 'category.html', context)

def deletecategory(request, id):
    Category.objects.filter(id=id).delete()
    return redirect('addcategory')

def is_valid_queryparam(param):
    return param != '' and param is not None

def deleteproduct(request, id):
    Category.objects.filter(id=id).delete()
    return redirect('listproduct')

def bigsearch(request):
    qs = Product.objects.all()
    categories = Category.objects.all()
    cate = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    if request.method =="POST":
        category = str(request.POST['category'])
        query = str(request.POST['query'])

        print(category)
        print(query)

        if is_valid_queryparam(query):
            qs = qs.filter(name__icontains=query)

        if is_valid_queryparam(category):
            qs = qs.filter(category__name=category)


        context={'cate':cate, 'qs':qs, 'category':category, 'query':query, 'colors':colors, 'categories':categories, 'brands':brands}
        return render(request,'search2.html', context)

        context={'cate':cate,'colors':colors, 'categories':categories, 'brands':brands }
    return render(request,'search2.html', context)

def filtersearch(request):
    qs = Product.objects.all()
    categories = Category.objects.all()
    cate = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    if request.method =="GET":
        
        color = str(request.GET['color'])
        brand = str(request.GET['brand'])
        min_price = float(request.GET['min_price'])
        max_price = float(request.GET['max_price'])

        

        if is_valid_queryparam(brand):
            qs = qs.filter(brand__name=brand)

        if is_valid_queryparam(color):
            qs = qs.filter(color__name=color)

        if is_valid_queryparam(min_price):
            qs = qs.filter(price__gte=min_price)

        if is_valid_queryparam(max_price):
            qs = qs.filter(price__lt=max_price)




            context={'cate':cate, 'qs':qs , 'colors':colors, 'categories':categories,'brands':brands, 'min_price':min_price, 'max_price':max_price}
        return render(request,'search2.html', context)

    else:
        context={'qs':qs,'cate':cate, 'colors':colors, 'categories':categories, 'brands':brands}
        return render(request,'search2.html', context)
    
    context={'qs':qs,'cate':cate, 'colors':colors, 'categories':categories, 'brands':brands}
        

    return render(request,'search2.html', context)


def registerUser(request):
    cate = Category.objects.all()
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Welcome to Sproad ,"+ user +" Your account was successfully created!")
            context={'cate':cate}
            return render(request,'login.html',context)
    context = {'form':form, 'cate':cate}
    return render(request, 'register.html', context)

def checkout(request):
    return render(request,'checkout.html')



#######################################################################################
############################### CART OPTIONS #############################################

@login_required(login_url='index')
def cart(request):
    user = request.user
    cate = Category.objects.all()
    cl = Cart.objects.filter(user=user)

    context = {'cl':cl, 'cate':cate}
    return render(request,'cart.html', context)

@login_required(login_url='index')
def removefromcart(request,id):
    user = request.user
    cl = Cart.objects.filter(user=user)
    cate = Category.objects.all()
    Cart.objects.filter(pk=id).delete()
    context = {'cate':cate, 'cl':cl}
    return render(request,'cart.html', context)

@login_required(login_url='index')
def addtocart(request,id):
    user = request.user
    cl = Cart.objects.filter(user=user)
    cate = Category.objects.all()
    
    product = Product.objects.get(pk=id)
    quantity = 1

    Cart.objects.create(user=user,product=product,quantity=quantity)
    context = {'cate':cate, 'cl':cl}
    return render(request,'cart.html', context)



#########################################################################################
################################ WISHLIST OPITONS##############################################

@login_required(login_url='index')
def wishlist(request):
    user = request.user
    cate = Category.objects.all()
    
    wi = Wishlist.objects.filter(user=user)
    context = {'wi':wi, 'cate':cate}

    return render(request, 'wishlist.html', context)



@login_required(login_url='index')
def addtowishlist(request,id):
    user = request.user
    cate = Category.objects.all()
    wi = Wishlist.objects.filter(user=user)
    
    product = Product.objects.get(pk=id)
    quantity = 1

    Wishlist.objects.create(user=user,product=product,quantity=quantity)
    context = {'wi':wi, 'cate':cate}

    return render(request, 'wishlist.html', context)

@login_required(login_url='index')
def removefromwishlist(request,id):
    user = request.user
    cate = Category.objects.all()

    wi = Wishlist.objects.filter(user=user)
    Wishlist.objects.filter(pk=id).delete()
    return render(request, 'wishlist.html', context)




def createup(request):
    cate = Category.objects.all()

    user = request.user
    if request.method == "POST" and request.FILES["profile_photo"]:

        profile_photo = (request.FILES['profile_photo']) 
        phone_number = str(request.POST['phone_number']) 
        stripe_customer_id = str(request.POST['stripe_customer_id']) 
        one_click_purchasing = int(request.POST['one_click_purchasing'])

        profile = Userprofile.objects.create(user=user,profile_photo=profile_photo, phone_number= phone_number,
           stripe_customer_id=stripe_customer_id,one_click_purchasing=one_click_purchasing )

        profile.save()

        context= {'cate':cate}
        return render(request,'index.html', context)

    else:
        context = {'cate':cate}
        return render(request, 'useprofile.html', context)

    context = {'cate':cate}

    return render(request, 'useprofile.html', context)


        


########################################################################################
########################### VENDOR VIEWS ##############################################

def createproduct(request):
    cate = Category.objects.all()
    user = request.user
    colors = Color.objects.all()
    brands = Brand.objects.all()

    if request.method == "POST" and request.FILES["image"]:

        name = str(request.POST['name'])
        label = str(request.POST['label'])
        price = float(request.POST['price'])
        discount_price = float(request.POST['discount_price'])
        slug = str(request.POST['slug'])
        description = str(request.POST['description'])
        image = request.FILES['image']
        cate = str(request.POST['category'])
        category = Category.objects.get(name=cate)

        col = str(request.POST['color'])
        color = Color.objects.get(name=col)

        bra = str(request.POST['brand'])
        brand = Brand.objects.get(name=bra)


        supp = str(request.POST['supplier'])
        supply = User.objects.get(username=supp)
        supply2 = Userprofile.objects.get(user=supply)
        supplier = Supplier.objects.get(profile=supply2)

        reorder_level = int(request.POST['reorder_level'])
        stock = int(request.POST['stock'])
        orders = int(request.POST['orders'])
        vendor = user

        product = Product.objects.create(vendor=vendor, name=name, label=label, price=price,
            discount_price=discount_price, slug=slug, description=description, brand=brand, color=color,
            image=image, category=category, supplier=supplier, reorder_level=reorder_level,
            stock=stock, orders=orders)

        product.save()
        return redirect('createproduct')

    else:
        context = {'cate':cate, 'colors':colors, 'brands':brands}
        return render(request, 'add_product_listing.html', context)

    context = {'cate':cate, 'colors':colors, 'brands':brands}

    return render(request, 'add_product_listing.html', context)
