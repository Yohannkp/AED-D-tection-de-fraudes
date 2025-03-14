# 📊 Projet : Analyse Exploratoire des Données - Détection de Fraude Bancaire

Application : https://aed-d-tection-de-fraudes-vdlxape8rcmrnbbbvedjcb.streamlit.app/

## 🎯 Objectif
Ce projet vise à analyser un dataset de transactions bancaires afin d'identifier les transactions frauduleuses à l'aide d'une **Analyse Exploratoire des Données (AED)**. Une application **Streamlit interactive** a été développée pour visualiser les tendances et distributions des données.

## 📂 Contenu du projet
- **app.py** : Code principal de l'application Streamlit.
- **creditcard.csv** : Dataset contenant les transactions bancaires.
- **README.md** : Ce fichier de documentation.

## 🛠️ Installation & Exécution
### 1️⃣ Prérequis
Assurez-vous d'avoir **Python 3.7+** installé ainsi que les dépendances suivantes :
```bash
pip install streamlit pandas matplotlib seaborn
```

### 2️⃣ Lancer l'application Streamlit
Exécutez la commande suivante pour démarrer l'interface interactive :
```bash
streamlit run application.py
```

## 📌 Fonctionnalités de l'application
✅ **Aperçu des données** : Affichage des premières lignes et dimensions du dataset.
✅ **Visualisation des transactions normales vs frauduleuses**.
✅ **Distribution des montants des transactions**.
✅ **Boxplot des montants pour détecter les valeurs aberrantes**.
✅ **Matrice de corrélation des variables**.
✅ **Navigation interactive via la barre latérale**.

## 📊 Dataset utilisé
Le dataset **creditcard.csv** contient **284 807 transactions** avec **31 variables** :
- `Time` : Temps écoulé depuis la première transaction.
- `V1` à `V28` : Variables transformées par **PCA** pour préserver l'anonymat.
- `Amount` : Montant de la transaction.
- `Class` : 0 = transaction normale, 1 = transaction frauduleuse.

## 🔍 Résultats clés de l'analyse exploratoire
- **Dataset fortement déséquilibré** (très peu de fraudes).
- **Valeurs aberrantes détectées sur le montant des transactions**.
- **Corrélation faible entre les variables PCA**.
- **Les transactions frauduleuses ont tendance à avoir des montants plus élevés**.

## 🚀 Améliorations possibles
🔹 Appliquer un **rééquilibrage des classes** (ex: SMOTE, sous-échantillonnage).  
🔹 Tester des **modèles de machine learning** pour détecter la fraude.  
🔹 Ajouter des **filtres interactifs** dans l'application Streamlit.  

---
✨ **Auteur** : [Yendi]  
📅 **Date** : [12/03/2025]  
