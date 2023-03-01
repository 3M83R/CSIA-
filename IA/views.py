from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ContactForm, Addhostels, OnDemandForm
from .models import  hostels, Customers, OnDemand
from django.contrib import messages
from django.db.models import Q 
from django.urls import reverse

# Create your views here.
################################################################

def about_us(request):
  return render(request, 'IA/about_us.html')

################################################################

def show_hostels(request, hostel_id):
  hostel = hostels.objects.get(pk=hostel_id)
  return render(request, 'IA/show_hostels.html', { 'hostel': hostel})

################################################################

def login(request):
  return render(request, 'IA/login.html')

################################################################

def search(request):
  if request.method == 'POST':  
    cin = request.POST['cin']
    cout = request.POST['cout']
    adults = request.POST['adults']
    kids = request.POST['kids']
    hcin = hostels.objects.filter(checkindate__lte = cin, checkoutdate__gte = cout, adults__gte = adults,children__gte = kids) 
    return render(request, 'IA/search.html', {
    'cin' : cin, 
    'cout' : cout, 
    'hcin' : hcin, 
    'adults' : adults,
    'kids' : kids,
    }) 

  else:
    return render(request, 'IA/search.html', {})
  
################################################################

def on_demand(request):
  on_demand = OnDemandForm()
  context = {
    'on_demand': on_demand
  }
  if request.method == 'POST':
      
    on_demand = OnDemandForm(request.POST)
    if on_demand.is_valid():
        messages.success(request, "Your request has been received! We will contact you shortly!")
        on_demand.save()
        return HttpResponseRedirect('/on_demand')
    else:
      messages.warning(request, "You might have inputed some wrong data, please try again!")
      return HttpResponseRedirect('/on_demand')
  return render(request, 'IA/on_demand.html',{'context': context})

################################################################

def main(request):
  return render(request, 'IA/main_page.html',{})

################################################################

def index(request):
  return render(request, 'IA/main_page.html',)

################################################################

def contact_us(request):
  contact_form = ContactForm()
  context = {
    'contact_form': contact_form
  }
  if request.method == 'POST':
      
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        messages.success(request, "Your message has been sent. We once again thank you for the feedback!")
        contact_form.save()
        return HttpResponseRedirect('/contact_us')
    else:
      messages.warning(request, "Your message has not been sent because you have entered a one or multiple fields wrong, please try again.")
      return HttpResponseRedirect('/contact_us')
  return render(request, 'IA/contact_us.html', {'context': context})

################################################################

def add(request):

  add = Addhostels()
  context = { 'add': add }

  if request.method == 'POST': 
    add = Addhostels(request.POST, request.FILES)
    if add.is_valid():
        messages.success(request, "You have successfully added the hostel")
        add.save()
        return HttpResponseRedirect('/add')
    else:
        messages.warning(request, "You have inputed wrong information about the hostel, please try again.")
        return HttpResponseRedirect('/add')
  return render(request, 'IA/add.html', {'context': context})

################################################################

def update_hostels(request, hostel_id):
  hostel = hostels.objects.get(pk=hostel_id)
  form = Addhostels(request.POST or None, request.FILES or None, instance=hostel)
  if form.is_valid():
    form.save()
    return redirect('/list_hostels')
  return render(request, 'IA/update_hostels.html', { 'hostel': hostel, 'form':form })

################################################################

def admin_page(request):
  return render(request, 'IA/admin_page.html')

################################################################

def list_hostels(request):
  hostels_list = hostels.objects.all()
  return render(request, 'IA/hostels.html', {'hostels_list' : hostels_list})

################################################################

def delete_hostels(request, hostel_id):
  hostel = hostels.objects.get(pk=hostel_id)
  hostel.delete()
  return redirect('/list_hostels')

################################################################

def contact_forms(request, c_id):
  contactf = Customers.objects.get(pk=c_id)
  return render(request, 'IA/contact_forms.html', { 'contactf': contactf})

################################################################

def list_contacts(request):
  contact_list = Customers.objects.all()
  return render(request, 'IA/contact_list.html', {'contact_list' : contact_list})

################################################################

def demand_forms(request, d_id):
  demandf = OnDemand.objects.get(pk=d_id)
  return render(request, 'IA/demand_form.html', { 'demandf': demandf})

################################################################

def list_demands(request):
  demand_list = OnDemand.objects.all()
  return render(request, 'IA/demand_list.html', {'demand_list' : demand_list})