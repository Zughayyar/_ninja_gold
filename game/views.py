from django.shortcuts import render, redirect
from random import randrange

# Create your views here.
def index(request):
    if 'score' not in request.session:
        request.session['score'] = 0
        request.session['message'] = []
        request.session['count'] = 0
    return render(request , "index.html")

def process_money(request):
    if request.POST['building'] == 'farm':
        rand_farm = randrange(10,20,1)
        request.session['score'] += rand_farm
        request.session['message'].insert(0,f'Earned {rand_farm} golds from the farm!')
        request.session['count'] += 1
        
    if request.POST['building'] == 'cave':
        rand_cave = randrange(5,10,1)
        request.session['score'] += rand_cave
        request.session['message'].insert(0,f'Earned {rand_cave} golds from the cave!')
        request.session['count'] += 1

    if request.POST['building'] == 'house':
        rand_house = randrange(2,5,1)
        request.session['score'] += rand_house
        request.session['message'].insert(0,f'Earned {rand_house} golds from the house!')
        request.session['count'] += 1

    if request.POST['building'] == 'casino':
        rand_casino = randrange(-50,50,1)
        request.session['score'] += rand_casino
        request.session['message'].insert(0,f'Earned {rand_casino} golds from the casino!')
        request.session['count'] += 1

    return redirect('/')

def destroy_session(request):
    request.session['score'] = 0
    request.session['message'] = []
    request.session['count'] = 0

    return redirect('/')
