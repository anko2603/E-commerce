# from django.shortcuts import render
# Create your views here.
from urllib import request
from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . models import Product
from  app.forms import CustomerRegistrationForm  

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class  CategoryView(View):
    def get(self, request,val):
        product= Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html",locals())
    
# class  CategoryTitle(View):
#     def get(self, request,val):
#         product= Product.objects.filter(title=val)
#         title = Product.objects.filter(category=product[0].category).values('title')
#         return render(request, "app/category.html",locals())
 
class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetails.html",locals()) 
    
# class CustomerRegistrationView(View):
#     def get(self,request):
#         form = CustomerRegistrationForm()
#         return render(request,"app/customerregistration.html",locals())