from django.forms import ModelForm
from .models import UE, Formation

class UEPost(ModelForm):
    class Meta:
        model = UE
        fields = ["titre", "description", "cm", "td", "tp", "credits", "formations", "responsables"]

        labels = {
            "titre" : "Titre",
            "description" : "Description",
            "cm" : "Nombre d'heure de CM",
            "td" : "Nombre d'heure de TD",
            "tp" : "Nombre d'heure de TP",
            "credits" : "Nombre de crédits",
            "formations" : "Formations",
            "responsables" : "Responsable",
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            user = getattr(self, 'user', None)

            if user:
                self.fields['formations'].queryset = Formation.objects.filter(responsable=user)