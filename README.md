multilang_site
Description du Projet

multilang_site est une application web Django conçue pour gérer et afficher des articles de blog avec prise en charge multilingue. Le projet inclut les fonctionnalités suivantes :

    Gestion des articles de blog avec les champs title, content et publication_date.
    Vue pour afficher une liste d'articles.
    Support pour l'internationalisation (i18n) avec au moins deux langues (français et anglais).
    Interface utilisateur permettant de changer la langue.
    Intégration d'un chatbot utilisant la bibliothéque Chatterbot.

Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

    Python 3.8
    Git
    Virtualenv
    les dépendences sur requirements.txt

Installation et Configuration:
Clonez le dépôt:
    git clone https://github.com/ZahryAkram-13/multilang_site.git
    cd multilang_site

Créez et activez un environnement virtuel :
    python -m venv django_multilang
    source venv/bin/activate
    
Installez les dépendances :
    pip install -r requirements.txt
    
Appliquez les migrations :
    python manage.py migrate

Créez un superutilisateur :
    python manage.py createsuperuser

Lancez le serveur de développement :
    python manage.py runserver

Accédez à l'application dans votre navigateur :
    Ouvrez http://127.0.0.1:8000 dans votre navigateur.

Internationalisation (i18n): (ne pas faire)
    django-admin makemessages -l fr
    django-admin makemessages -l en
    django-admin compilemessages














