# 🎓 Django Formation Manager

Application web **Django** de gestion de **formations universitaires** et de leurs **unités d'enseignement (UE)**. Le détail d'une formation n'est accessible qu'à l'**enseignant responsable** de cette formation.

> Projet réalisé dans le cadre du module *Framework Web 1* — Master Informatique, Université d'Orléans (2024-2025).

---

## ✨ Fonctionnalités

- 📚 **Gestion des formations** — liste, détail, consultation
- 🧩 **Gestion des UE** — ajout, affichage, suppression, rattachées aux formations
- 👨‍🏫 **Enseignants** — comptes utilisateurs responsables de formations
- 🔐 **Accès restreint** — le détail d'une formation (`/details/<id>`) n'est visible que si l'utilisateur connecté en est le **responsable**
- 🛠️ **Interface d'administration** Django

---

## 🏗️ Structure du projet

```
django-formation-manager/
├── ct/                     # Configuration du projet Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── uo/                     # Application principale (Université d'Orléans)
│   ├── models.py           # Formation, UE, (enseignant = User)
│   ├── views.py            # Logique métier + contrôle d'accès responsable
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   ├── fixtures/           # Données de démo : enseignant, formation, ue
│   └── templates/          # Pages HTML (index, détail, ajout, login…)
└── manage.py
```

---

## 🛠️ Stack technique

| | |
|---|---|
| **Framework** | Django (Python) |
| **Base de données** | SQLite |
| **Templates** | Django Templates (HTML) |
| **Auth** | Système d'authentification Django |
| **Conteneurisation** | Docker |

---

## 🚀 Installation & lancement

### Avec Python (local)

```bash
# 1. Environnement virtuel
python -m venv venv
venv\Scripts\activate         # Windows
# source venv/bin/activate    # macOS / Linux

# 2. Dépendances
pip install django

# 3. Configurer le SECRET_KEY (voir section ci-dessous)

# 4. Base de données + données de démo
python manage.py migrate
python manage.py loaddata enseignant formation ue

# 5. (optionnel) compte administrateur
python manage.py createsuperuser

# 6. Lancer le serveur
python manage.py runserver
```

Application accessible sur `http://localhost:8000`.

### Avec Docker

```bash
docker build . -f Dockerfile --tag ct
docker run -ti -p 8080:8000 -v $PWD:/home/user/workspace ct
python manage.py runserver 0.0.0.0:8000
```

---

## 🔑 Configuration du SECRET_KEY

Par sécurité, la vraie clé n'est **pas** versionnée. Dans `ct/settings.py`, la valeur est un placeholder (`django-insecure-change-me`). Génère ta propre clé :

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

puis remplace la valeur de `SECRET_KEY` (idéalement via une variable d'environnement en production).

---

## 👥 Auteurs

Projet de groupe — Master Informatique, Université d'Orléans :

- **Gahlas Aicha** — [github.com/GahlasAicha](https://github.com/GahlasAicha)
- **Seffar Nordine**
- **Mimoun Ali**
- **Aissat Fatima**