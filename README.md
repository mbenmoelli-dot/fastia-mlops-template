\# FastIA – Template MLOps (FastAPI / Streamlit / Docker / CI)



\## 🎯 Objectif du projet



Ce projet met en place une \*\*architecture MLOps minimale et reproductible\*\*, destinée à servir de \*\*template de base\*\* pour les futurs projets IA de FastIA.



L’objectif est de démontrer :

\- la séparation frontend / backend,

\- la conteneurisation avec Docker,

\- l’automatisation des tests via une chaîne CI/CD,

\- et le respect des bonnes pratiques d’ingénierie logicielle.



---



\## 🏗️ Architecture générale



L’architecture repose sur \*\*deux services indépendants\*\* orchestrés via Docker Compose :



\[ Utilisateur ]

|

v

\[ Frontend Streamlit ]

|

v

\[ API FastAPI ]

|

v

\[ Logique métier (modules/calcul.py) ]





\### 🧩 Composants



\- \*\*Frontend\*\* :  

&nbsp; - Streamlit  

&nbsp; - Interface simple permettant de saisir un entier  

&nbsp; - Appelle l’API backend via HTTP



\- \*\*Backend\*\* :  

&nbsp; - FastAPI + Pydantic  

&nbsp; - Validation des données d’entrée  

&nbsp; - Logique métier isolée dans un module dédié  

&nbsp; - Logs gérés avec Loguru



\- \*\*Tests\*\* :  

&nbsp; - pytest  

&nbsp; - Tests unitaires de la logique métier



\- \*\*CI/CD\*\* :  

&nbsp; - GitHub Actions  

&nbsp; - Exécution automatique des tests à chaque push



---



\## 📁 Structure du projet



fastia-mlops-template/

│

├── frontend/

│ ├── app.py # Application Streamlit

│ └── Dockerfile

│

├── backend/

│ ├── main.py # API FastAPI

│ ├── Dockerfile

│ ├── init.py

│ ├── modules/

│ │ ├── calcul.py # Logique métier

│ │ └── init.py

│ └── tests/

│ └── test\_calcul.py # Tests unitaires

│

├── docker-compose.yml

├── .github/workflows/test.yml

└── README.md







---



\## 🔌 Routes de l’API



| Méthode | Route     | Description |

|-------|-----------|------------|

| GET   | `/`       | Test de disponibilité de l’API |

| GET   | `/health` | Healthcheck |

| POST  | `/calcul` | Retourne le carré d’un entier |



\### Exemple de requête `/calcul`



```json

{

&nbsp; "value": 4

}

Réponse attendue

json

Copier le code

{

&nbsp; "result": 16

}

▶️ Lancer le projet en local (Docker)

Prérequis

Docker



Docker Compose



Lancement

À la racine du projet :



bash

Copier le code

docker compose up --build

Accès aux services

Frontend Streamlit :

👉 http://localhost:8501



API FastAPI (Swagger) :

👉 http://localhost:8000/docs



🧪 Tests unitaires

Lancer les tests en local

bash

Copier le code

pytest backend/tests

Intégration continue

Les tests sont exécutés automatiquement via GitHub Actions à chaque :



push



pull request



Le détail des tests exécutés est consultable dans l’onglet Actions du dépôt GitHub.



🔁 CI/CD – GitHub Actions

Le workflow CI :



Récupère le code



Installe Python et les dépendances



Configure le PYTHONPATH



Exécute les tests pytest



Objectif :



détecter automatiquement les régressions



garantir la stabilité avant déploiement





