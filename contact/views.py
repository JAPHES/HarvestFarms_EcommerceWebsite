from django.shortcuts import render, redirect


from .forms import ContactForm
def index(request):
    return render(request, 'index.html')

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})
def success(request):
    return render(request, 'contact/success.html')


def contact_view(request):
    return render(request, 'contact/contact.html')

def success_view(request):
    return render(request, 'contact/success.html')

