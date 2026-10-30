Membres du groupe :
SEFFAR Nordine nordine.seffar@etu.univ-orleans.fr
GAHLAS Aicha aicha.gahlas@etu.univ-orleans.fr
MIMOUN Ali ali.mimoun@etu.univ-orleans.fr
AISSAT Fatima fatima.aissat@etu.univ-orleans.fr

Commandes :


quesiton1 :

docker build . -f Dockerfile --build-arg USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) --build-arg USERID=$(id -u) --tag ct

docker run -ti -p 8080:8000 -v $PWD:/home/user/workspace ct

(Dans vscode ->)

django-admin startproject ct

cd ct

python manage.py startapp uo

python manage.py runserver 0.0.0.0:8000 &

question 2 :

question 3 :

python manage.py migrate

python manage.py createsuperuser

admin

admin@gmail.com

admin

admin

y

question 4 :

python manage.py dumpdata auth.User --indent 2 > uo/fixtures/enseignant.json

python manage.py loaddata enseignant

question 5 :

python manage.py makemigrations uo

python manage.py migrate

question 6 :

python manage.py dumpdata uo.Formation --indent 4 > uo/fixtures/formation.json

python manage.py loaddata formation

question 7 :

python manage.py makemigrations uo

python manage.py migrate

question 8 :

python manage.py dumpdata uo.UE --indent 4 > uo/fixtures/ue.json

python manage.py loaddata ue

question 9 :

question 10 :

question 11 :

question 12 :

question 13 :

question 14 :

question 15 :

question 16 :

question 17 :

question 18 :

question 19 :

question 20 :