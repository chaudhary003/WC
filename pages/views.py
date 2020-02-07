from django.shortcuts import render
from listings.models import Listing
from realtor.models import Realtor
# Create your views here.
from listings.choices import state_choices,bedroom_choices,price_choices
def index(request):
    listings=Listing.objects.order_by('-listing_date').filter(is_published=True)[:6]
    context={'listings':listings,
            'state_choices':state_choices,
            'bedroom_choices':bedroom_choices,
            'price_choices':price_choices }
    return render(request,'pages/index.html',context)
def aboutus(request):
    realtors=Realtor.objects.order_by('-hire_date')
    som_realtors=Realtor.objects.all().filter(is_som=True)
    context={
    'realtors':realtors,
    'som_realtors':som_realtors
    }
    return render(request,'pages/aboutus.html',context)
