from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from .models import Donations
from .models import Event
from .forms import DonationForm

def donate(request):
    """ A view to return the donation page """
    return render(request, 'charity/charity.html')

def makedonations(request):
    """ A view to return the donation page 
    and handle all donations"""


    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.user = request.user
            donor.save()
            messages.info(request, 'Successfully made a donation')
            return redirect(reverse('donate'))
        else:
            messages.error(request, 'Sorry we cannot add Product review. \
                                Please ensure all fields are completed.')
    else:
        form = DonationForm()

    template = 'charity/donate.html'
    context = {
        'form': form,
    }
    return render(request, template, context)