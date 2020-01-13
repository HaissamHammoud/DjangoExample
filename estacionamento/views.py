from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,Http404, HttpResponse
from .models import Car
from .forms import CarForms
from django.urls import reverse
from django.template import loader

# Create your views here.
def car_entrance(request):
    form = CarForms(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form':form
    }

    return render(request , "carros/Entrada.html",context)

def car_exit(request):
    #HttpResponseRedirect(Car,My_id)
    try:
        car = Car.objects.all()
        print(car)
    except :
        raise Http404("O carro não existe")
    context = {
        'car': car,
    }
    return render(request,"carros/saida.html",{})

def car_menu(request):
    return render(request, "menu.html")


def car_detail_view(request, my_id):
    obj = get_object_or_404(Car, id = my_id)
    context = {
    'object' : obj,
    }
    return render(request,"carros/cardetail.html", context)

def car_redirect(request, my_id):

    print(request.POST)

    number = request.POST['carid']
    try:
            if Car.objects.get(id = number).DoesNotExist:
                return HttpResponseRedirect(reverse('estacionamento:car_detail', args = (number,)))
    except:
        return HttpResponse("car does not exist")
