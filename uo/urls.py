from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.vue_about, name="vue_about"),
    path("formation/<int:n>", views.afficher_formation, name="afficher_formation"),
    path("ue/<int:n>", views.afficher_ue, name="afficher_ue"),
    path("index_formation/", views.index_formation, name="index_formation"),
    path("index_ue/", views.index_ue, name="index_ue"),
    path("ue/ajouter/", views.ajouter_ue, name="ajouter_ue"),
    path("", views.menu, name="menu"),
    path("ue/modifier/<int:n>", views.modifier_ue, name="modifier_ue"),
    path("ue/supprimer/<int:n>", views.supprimer_ue, name="supprimer_ue"),
    path("details/<int:n>", views.info_pour_responsable, name="info_pour_responsable"),
]