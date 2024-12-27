from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Free, Customer, Beauty, Kiyimlar, Computer
from .forms import ContactForm
from django.views.generic import UpdateView, CreateView,  DeleteView
from django.urls import reverse_lazy
# Create your views here.

class ComputerUpdateView(UpdateView):
    model = Computer
    fields = ('name', 'bio', 'img', 'price', 'price2')
    template_name = 'ComputerEdit.html'

class ComputerDeleteView(DeleteView):
    model = Computer
    template_name = 'ComputerDelete.html'
    success_url = reverse_lazy('index')

class ComputerCreateView(CreateView):
    model = Computer
    template_name = 'ComputerCreateView.html'
    fields = ('name', 'bio', 'img', 'price', 'price2')

def Computerdetail(request, computers):
    computers = get_object_or_404(Computer, slug=computers)
    context = {
        'computers': computers
    }
    return render(request, 'computerDetailView', context=context)

def index(request):
    computer = Computer.objects.all()
    kiyimlar = Kiyimlar.objects.all()
    customer = Customer.objects.all()
    beauty = Beauty.objects.all()
    free = Free.objects.all()
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "free": free,
        "customer": customer,
        "beauty": beauty,
        "kiyimlar": kiyimlar,
        "computer": computer,
        "contact": contact
    }

    return render(request, 'index.html', context=context)
def computer(request):
    computer = Computer.objects.all()
    context = {
        'computer': computer
    }
    return render(request, 'computers.html', context=context)
def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "contact": contact
    }
    return render(request, 'contact.html', context=context)
def mans_clothes(request):
    kiyimlar = Kiyimlar.objects.all()
    context = {
        'kiyimlar': kiyimlar
    }
    return render(request, 'mans_clothes.html', context=context)
def womans_clothes(request):
    customer = Customer.objects.all()
    context = {
        'customer': customer
    }
    return render(request, 'womans_clothes.html', context=context)


def kdetail(request, id):
    kiyimlar = Kiyimlar.objects.get(id=id)
    context = {
        'x': kiyimlar
    }
    return render(request, 'kDetail.html', context=context)

def bdetail(request, id):
     beauty = Beauty.objects.get(id=id)
     context = {
         'x': beauty
     }
     return render(request, 'bDetail.html', context=context)

def cdetail(request, id):
     customer = Customer .objects.get(id=id)
     context = {
         'x': customer
     }
     return render(request, 'cDetail.html',context=context)
def fdetail(request, id):
     free = Free.objects.get(id=id)
     context = {
         'x': free
     }
     return render(request, 'fDetail.html', context=context)




def kdetailView(request):
    return render(request, 'kDetailView', context={})

def bdetailView(request):
    return render(request, 'bDetailView', context={})

def cdetailView(request):
    return render(request, 'cDetailView', context={})

def fdetailView(request):
    return render(request, 'fDetailView', context={})

def computerdetailView(request, computer):
    computer = get_object_or_404(Computer, slug=computer)
    context = {
        'computer': computer
    }
    return render(request, 'computerDetailView', context=context)








