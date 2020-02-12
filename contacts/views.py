from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        email=request.POST['email']
        name=request.POST['name']
        phone=request.POST['phone']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']
        message=request.POST['message']
        contact=Contact(listing_id=listing_id,listing=listing,email=email,name=name,
        phone=phone,message=message,user_id=user_id)
        #check for already request
        if request.user.is_authenticated:
            user_id=request.user.id
            has_conected=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_conected:
                messages.error(request,'you already made a request for this listing')
                return redirect('/listings/'+listing_id)
        contact.save()
        #send_mail(
                # 'this is subject field',
                 #'Here is the message. that we will send',
                # 'arvkumar.java@gmail.com',
                 #['chaudhary003.com'],
                 #fail_silently=False,)
        messages.success(request,'your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)
