from django.shortcuts import render,redirect
from .models import client
from .forms import clientForm

def index(request):
    return render(request, 'vizitka/index.html')


def about(request):
    return render(request, 'vizitka/about.html')


def works(request):
    return render(request, 'vizitka/works.html')

def thanks(request):
    return render(request, 'vizitka/thanks.html')


def to_call(request):
    error=''
    if request.method == 'POST':
        form = clientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            error = 'invalid text'


    form = clientForm()
    number = {
        'form': form,
        'error': error
    }
    return render(request, 'vizitka/to_call.html', number)
