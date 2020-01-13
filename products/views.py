from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import  ProductForm ,RawProductForm
# Create your views here.




def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)

def top_products(request):
    obj = {}
    for i in range(3):
        if(Product.objects.get(id=i+1)):
            obj[i] = Product.objects.get(id=i+1)
            print(obj[i])
        else:
            break
    context = {
    'object': [obj[0],obj[1],obj[2]]
    }

    context['object'].append(Product.objects.get(id=4+1))


    return render(request,"products/top_products.html", context)



def product_dynamic_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
    context = {
    'object' : obj,
    }
    return render(request,"products/detail.html", context)


def loja_view(request):
        return render(request,"menu_loja.html", {})


        #este é um metodo ultilizando formulario html puro
        #Nao recomendado


        # def product_create_view(request):
        #     if request.method == "POST":
        #
        #         new_title = request.POST.get('title')
        #         Product.objects.create(title = new_title)
        #     context = {}
        #     return render(request, "products/product_create.html", context)

        #este é um metodo pronto que cria um formulario ja pre montado
        #bom para agilidae e prototipos  pois economisa tempo e facilita o teste

        # def product_create_view(request):
        #     form = ProductForm(request.POST or None )
        #     if form.is_valid():
        #         form.save()
        #
        #     context = {
        #     'form': form
        #     }
        #     return render(request, "products/product_create.html", context)
