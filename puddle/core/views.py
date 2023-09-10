from django.shortcuts import render,redirect

from item.models import Item,Category

from .forms import SignUpForm

def index(request):
    item = Item.objects.filter(is_sold=False)[0:6]
    category = Category.objects.all()
    return render(request,'core/index.html',{
        'categories' : category,
        'items' : item
    })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request,'core/signup.html',{
        'form': form
    })
