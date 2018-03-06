from django.shortcuts import render
from collection.models import Thing


# Create your views here.
def index(request):

    """ Initially: when the index page is viewed, display this template and pass along these 2 variables

    # defining the variable
    number = 3
    thing = "Thing name"

    # passing the variable to the view
    return render(request, 'index.html', {
        'number': number,
        'thing': thing,
    })
    """

    """ Update this to: when the index page is viewed, find all things in our db, display this template 
    and pass those things along to the template. -> querying for all Things is inefficient 
    => .get() to retrieve the one exact object that matches the query; .filter() for a bunch of things"""

    # correct_thing = Thing.objects.get(name='Thing one')
    # things = Thing.objects.filter(name='Thing one').order_by('name')
    # things = Thing.objects.filter(name__contains='Thing') # .order_by('?') for random order

    things = Thing.objects.all()
    return render(request, 'index.html', {
        'things': things,
    })


def thing_detail(request, slug):
    # grab the object
    thing = Thing.objects.get(slug=slug)
    # and pass to the template; now on top of the view we have slug passed from urls.py
    return render(request, 'things/thing_detail.html', {
        'things': thing,
    })

