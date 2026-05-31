# SkinAI — Application Web de Diagnostic du Cancer de la Peau

Application web de diagnostic du cancer de la peau basée sur l'Intelligence Artificielle.
Réalisée par : Elaa Cherif

---

## Description

SkinAI est une application web developpee avec Python Flask integrant un modele de Deep Learning (VGG16) pour le diagnostic automatique des lesions cutanees.

L'application permet a un professionnel de sante de :
- Se connecter via un systeme d'authentification securise
- Soumettre l'image d'une lesion cutanee avec les informations du patient
- Obtenir un diagnostic IA : Benin ou Malin avec un taux de confiance
- Consulter l'historique complet des diagnostics enregistres

---

## Captures d'ecran

### Page de connexion
Interface de login securisee avec un design medical professionnel. L'utilisateur entre son nom d'utilisateur et mot de passe pour acceder a la plateforme.

![Login](screenshots/login.png)

### Tableau de bord
Vue d'ensemble affichant les statistiques globales : nombre total de patients, cas malins detectes, cas benins, et la precision du modele IA.

![Dashboard](screenshots/dashboard.png)

### Analyse d'une image
Formulaire permettant de saisir les informations du patient (nom, age) et de telecharger une image de lesion cutanee pour analyse.

![Predict](screenshots/predict.png)

### Resultat du diagnostic : Cas malin
Affichage du resultat avec le diagnostic (Malin), le taux de confiance en pourcentage, l'image analysee et une recommandation medicale.

![Result Malin](screenshots/result_malin.png)

### Resultat du diagnostic : Cas benin
Affichage du resultat avec le diagnostic (Benin), le taux de confiance en pourcentage, l'image analysee et une recommandation de surveillance.

![Result Benin](screenshots/result_benin.png)

### Historique des patients
Tableau recapitulatif de tous les diagnostics enregistres avec le nom, l'age, le resultat, la probabilite, l'image et la date de chaque analyse.

![Patients](screenshots/patients.png)

---

## Structure du projet

```
SKIN_CANCER_APP/
├── model/
│   └── vgg16_malignant_vs_benign.h5
├── static/
│   ├── style.css
│   └── uploads/
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── predict.html
│   ├── result.html
│   └── patients.html
├── screenshots/
├── app.py
├── database.sql
├── requirements.txt
└── README.md
```

---

## Technologies utilisees

- Python 3.x — Langage principal
- Flask — Framework web
- TensorFlow / Keras — Modele Deep Learning VGG16
- MySQL — Base de donnees
- Bootstrap 5 — Interface utilisateur
- HTML / CSS — Templates Jinja2

---

## Installation et lancement

### 1. Installer les dependances
```bash
pip install flask tensorflow numpy mysql-connector-python werkzeug
```

### 2. Configurer la base de donnees
Lancer XAMPP, ouvrir phpMyAdmin et executer le fichier database.sql

### 3. Placer le modele
Copier vgg16_malignant_vs_benign.h5 dans le dossier model/

### 4. Lancer l'application
```bash
python app.py
```

Ouvrir : http://localhost:5000

---

## Identifiants par defaut

- Nom d'utilisateur : admin
- Mot de passe : 1234

---

## Modele IA

- Architecture : VGG16 (Transfer Learning, poids ImageNet)
- Dataset : Images de lesions cutanees (Benin / Malin)
- Entrainement : Google Colab, 10 epoques
- Classes : Benign (0) / Malignant (1)
