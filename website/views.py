from django.shortcuts import render, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didn't submitted")
    form = ContactForm()

    context = {'form':form}
    return render(request, 'website/contact.html', context)

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your email submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, "Your email didn't submitted")
            
    form = NewsletterForm()

    return HttpResponseRedirect('/')

def error_view(request):
    return render(request, '404.html')
