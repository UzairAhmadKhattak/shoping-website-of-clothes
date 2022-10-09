from django.shortcuts import render
from . models import home_table,gallery,about_us_table
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
# Create your views here.
#Class base view



#Function base view
# This is for home page
def index(request):

    dist = home_table.objects.all()
    # dist = distination.objects.get(id=46)

    comb=zip(dist,Rev())
    return render(request,'cloths templates/index.html',{'dists':comb})

# this is for reviews tags
def Rev():

    Reviews=[]

    items=home_table.objects.all()
    # iteration in list of object (items)
    for item in items:
        if item.title == "Shoes":
            Reviews.append(20)
        elif item.title=='Jacket':
            Reviews.append(22)

        elif item.title=='Cloths':
            Reviews.append(25)

        elif item.title=='Toy':
            Reviews.append(24)

        elif item.title=='Sweater':
            Reviews.append(23)

        else:
            Reviews.append(21)

    return Reviews
    # return render(request, 'cloths templates/index.html', {'my_dict': Reviews})


# this is for product page
def product(request):
    home = home_table.objects.all()

    comb = zip(home, Rev())
    return render(request,'cloths templates/products.html',{'dists':comb})

# this is for about us page
def about_us(request):

    about = about_us_table.objects.all()

    return render(request,'cloths templates/about.html',{'team':about})

# this is for contact us page

def contact_us(request):

    return render(request,'cloths templates/contact.html')