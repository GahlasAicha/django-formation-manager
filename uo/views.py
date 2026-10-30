from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Formation, UE
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def vue_about(request):
    return render(request, 'uo/about.html')

@login_required
def afficher_formation(request, n):
    formation = get_object_or_404(Formation, id=n)
    responsable = formation.responsable

    ues = UE.objects.filter(formations=formation)
    return render(request, 'uo/affichage_formation.html', {'formation':formation, 'responsable':responsable, 'ue':ues})


@login_required
def afficher_ue(request, n):
    ue = get_object_or_404(UE, id=n)

    responsables = ue.responsables.all()
    formations = ue.formations.all()

    return render(request, 'uo/affichage_ue.html', {'ue':ue, 'responsables':responsables, 'formations':formations})



@login_required
def index_formation(request):
    formations = Formation.objects.order_by("id")
    return render(request, 'uo/index_formation.html', {'formations':formations})


@login_required
def index_ue(request):
    ues = UE.objects.order_by("id")
    return render(request, 'uo/index_ue.html', {'ues':ues})


@login_required
def check_save(form, request):
    if form.is_valid():
        ue = form.save(commit=False)
        ue.save()
        form._save_m2m()
    return ue.id



@login_required
def ajouter_ue(request):
    if request.method == "POST":
        form = UEPost(request.POST)
        form.user = request.user
        if form.is_valid():
            id = check_save(form, request)
            return redirect("afficher_ue", n=id)
    else:

        f_responsable = Formation.objects.filter(responsable=request.user)

        form = UEPost()
        form.user = request.user
        form.fields['formations'].queryset = f_responsable
    return render(
        request,
        "uo/ajouter_ue.html",
        {"form": form, "button_label": "Ajouter une UE"},
    )


@login_required
def menu(request):
    return render(request, "uo/menu.html")



@login_required
def modifier_ue(request, n):
    ue = get_object_or_404(UE, pk=n)


    set_responsables = set()
    set_responsables_ue = set()
    
    for formation in ue.formations.all():
        set_responsables.add(formation.responsable)
    
    for responsable in ue.responsables.all():
        set_responsables_ue.add(responsable)


    if request.user not in set_responsables and request.user not in set_responsables_ue:
            return HttpResponseForbidden("Vous n'avez pas le droit d'accèder à cette page")


    if request.method == "POST":
        form = UEPost(request.POST, instance=ue)
        form.user = request.user

        if form.is_valid():
            id = check_save(form, request)
            return redirect("afficher_ue", n=id)
    else:
        form = UEPost(instance=ue)
        form.user = request.user
    return render(
        request,
        "uo/ajouter_ue.html",
        {"form":form, "button_label":"Modifier"}
    )


@login_required
def supprimer_ue(request, n):
    ue = get_object_or_404(UE, pk=n)

    set_responsables = set()
    
    for formation in ue.formations.all():

        set_responsables.add(formation.responsable)


    if request.user not in set_responsables:
            return HttpResponseForbidden("Vous n'avez pas le droit d'accèder à cette page")
    
    
    responsables = ue.responsables.all()
    formations = ue.formations.all()

    if request.method == "POST":
        ue.delete()
        return redirect("index_ue")
    return render(request, "uo/supprimer_ue.html", {'ue':ue, 'responsables':responsables, 'formations':formations})

@login_required
def info_pour_responsable(request, n):
    formation = get_object_or_404(Formation, id=n)

    if request.user != formation.responsable:
         return HttpResponseForbidden("Vous n'avez pas le droit d'accèder à cette page")


    ues = UE.objects.filter(formations=formation)
    nbr_ue = ues.count()

    liste_responsable_ue = set()
    for ue in ues:
        liste_responsable_ue.update(ue.responsables.all())
        
    liste_responsable_ue = sorted(liste_responsable_ue, key=lambda user: user.username)
    print(liste_responsable_ue)
    
    
    total_cm = sum(ue.cm for ue in ues)
    total_td = sum(ue.td for ue in ues)
    total_tp = sum(ue.tp for ue in ues)

    total_hrs_equiv_td = total_cm * 1.5 + total_td + total_tp

    total_ects = sum(ue.credits for ue in ues)

    context = {
        'formation': formation,
        'nbr_ue': nbr_ue,
        'liste_responsable_ue': liste_responsable_ue,
        'total_cm': total_cm,
        'total_td': total_td,
        'total_tp': total_tp,
        'total_hrs_equiv_td': total_hrs_equiv_td,
        'total_ects': total_ects,
    }

    return render(
        request,
        'uo/details_formation.html',
        context
    )
