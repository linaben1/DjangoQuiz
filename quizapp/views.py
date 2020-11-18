from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from quizapp.models import Question, image, Answer
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserLoginForm, RegistrationForm
from .filters import imageFilter
from .models import *

#init du score
s = 0

def home(request):
    global s
    context = {'s':s}
    return render(request, 'home.html', context=context)


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/user_home')
    return render(request, 'login.html', {"form": form, "title": title})


def register(request):

    title = "Create account"
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()

    context = {'form': form, 'title': title}
    return render(request, 'registration.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required()
def user_home(request):
    global s
    context = {'s':s}
    return render(request, 'user_home.html', context=context)


def Image_Table(request):

    all_info = image.objects.all()
    myFilter = imageFilter()
    fil = request.GET.get('filter') 
    print(fil)

    if fil != '' and fil is not None:
        all_info = all_info.filter(celltype = fil)

    context={ 'all':all_info, 'myFilter':myFilter}
    return render(request, 'Image_Table.html', context)


def image_galery(request):
    all_info = image.objects.all()
    context={ 'all':all_info,}
    return render(request, 'image_galery.html', context)




def quiz_micro(request):

    global s

    qst = Question.objects.filter(questionid=1)
    ans = Answer.objects.filter(questionid=1)

    #choix de la bonne réponse
    bonne_rep = ans[:]
    bonne_rep = random.choice(bonne_rep).answer

    #choix des bonne images
    img = image.objects.filter(mode = bonne_rep)
    nb_img = qst[0].n_image
    list_image = []
    for i in range(nb_img):
        list_image.append(img[random.randint(0,len(img)-1)].name)

    #request pour recuperer la réponse
    # via une requete POST du bouton avec le name = "system"
    system = request.POST.get('system', None)

    #Test du score
    rep_message = ""

    if request.method == 'POST':
        if system == bonne_rep:
            s += qst[0].point
            rep_message = "Bonne réponse "+"+"+str(qst[0].point)
        else:
            s -= qst[0].point
            rep_message = "Mauvaise réponse "+"-"+str(qst[0].point)

    context = {'qst':qst , 'ans':ans , 'bonne_rep':bonne_rep, 'list_image':list_image, 's':s , 'system':system , 'rep_message':rep_message}
    return render(request, 'quiz_micro.html', context=context)


def quiz_component(request):

    global s

    qst = Question.objects.filter(questionid=2)
    ans = Answer.objects.filter(questionid=2)

    #choix des reponses
    #bonne_rep = ans[:]
    ans_f = ans.order_by('?')[:4]
    bonne_rep = random.choice(ans_f).answer


    #choix des bonne images
    img = image.objects.filter(component = bonne_rep)
    nb_img = qst[0].n_image
    list_image = []
    for i in range(nb_img):
        list_image.append(img[random.randint(0,len(img)-1)].name)

    #request pour recuperer la réponse
    system = request.POST.get('system', None)

    #Test du score
    rep_message = ""
    if request.method == 'POST':
        if system == bonne_rep:
            s += qst[0].point
            rep_message = "Bonne réponse "+"+"+str(qst[0].point)
        else:
            s -= qst[0].point
            rep_message = "Mauvaise réponse "+"-"+str(qst[0].point)


    context = {'qst':qst , 'ans_f':ans_f , 'bonne_rep':bonne_rep, 'list_image':list_image, 's':s ,'system':system , 'rep_message':rep_message  }
    return render(request, 'quiz_component.html', context=context)
