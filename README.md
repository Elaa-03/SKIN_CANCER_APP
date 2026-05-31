# 🔬 SkinAI — Application Web de Diagnostic du Cancer de la Peau

> Application web IA développée dans le cadre du module **Introduction à l'IA** — ENSTAB 2025/2026  
> Enseignante : Dr. Amira Echtioui

---

## 📌 Description

**SkinAI** est une application web complète développée avec **Python Flask** intégrant un modèle de Deep Learning (**VGG16**) pour le diagnostic automatique des lésions cutanées.

L'application permet à un professionnel de santé de :
- Se connecter via un système d'authentification sécurisé
- Soumettre l'image d'une lésion cutanée avec les informations du patient
- Obtenir un diagnostic IA : **Bénin** ou **Malin** avec un taux de confiance
- Consulter l'historique complet des diagnostics enregistrés

---

## 🖼️ Captures d'écran

### Page de connexion
![Login](screenshots/login.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Analyse d'une image
![Predict](screenshots/predict.png)

### Résultat du diagnostic
![Result](screenshots/result.png)

### Historique des patients
![Patients](screenshots/patients.png)

---

## 🗂️ Structure du projet

```
SKIN_CANCER_APP/
├── model/
│   └── vgg16_malignant_vs_benign.h5   # Modèle entraîné
├── static/
│   ├── style.css                       # Feuille de style personnalisée
│   └── uploads/                        # Images soumises par les utilisateurs
├── templates/
│   ├── login.html                      # Page de connexion
│   ├── dashboard.html                  # Tableau de bord
│   ├── predict.html                    # Formulaire d'analyse
│   ├── result.html                     # Affichage du résultat
│   └── patients.html                   # Historique des patients
├── app.py                              # Application Flask principale
├── database.sql                        # Script de création de la base MySQL
└── README.md
```

---

## ⚙️ Technologies utilisées

| Technologie | Rôle |
|---|---|
| Python 3.x | Langage principal |
| Flask | Framework web |
| TensorFlow / Keras | Modèle Deep Learning (VGG16) |
| MySQL | Base de données |
| Bootstrap 5 | Interface utilisateur |
| HTML/CSS | Templates Jinja2 |

---

## 🚀 Installation & Lancement

### 1. Prérequis
- Python 3.x
- XAMPP (MySQL)
- pip

### 2. Installer les dépendances
```bash
pip install flask tensorflow numpy mysql-connector-python werkzeug
```

### 3. Configurer la base de données
1. Démarrer XAMPP → lancer Apache + MySQL
2. Ouvrir **phpMyAdmin** → Onglet SQL
3. Coller et exécuter le contenu de `database.sql`

### 4. Placer le modèle
Copier `vgg16_malignant_vs_benign.h5` dans le dossier `model/`

### 5. Lancer l'application
```bash
python app.py
```
Ouvrir : [http://localhost:5000](http://localhost:5000)

---

## 🔐 Identifiants par défaut

| Champ | Valeur |
|---|---|
| Nom d'utilisateur | `admin` |
| Mot de passe | `1234` |

---

## 🧠 Modèle IA

- **Architecture** : VGG16 (Transfer Learning, poids ImageNet)
- **Dataset** : Images de lésions cutanées (Bénin / Malin)
- **Entraînement** : Google Colab, 10 époques
- **Résultats** : ~85% de précision sur le jeu de test
- **Classes** : `Benign` (0) / `Malignant` (1)

---

## 👩‍💻 Auteure

Projet réalisé par **[Votre Prénom Nom]**  
1ère année ingénieur — Technologies Avancées (1TA)  
ENSTAB — 2025/2026
