\# M5 – Brief 2  

\## Automatiser le déploiement avec GitHub Actions et Docker Hub



---



\## 🎯 Objectif du brief



L’objectif de ce brief est de mettre en place un \*\*pipeline de déploiement continu (CD)\*\* permettant de \*\*publier automatiquement une image Docker\*\* sur Docker Hub à chaque mise à jour de la branche principale (`main`).



Ce pipeline s’appuie sur le projet du \*\*Brief 1\*\*, qui fournit déjà :

\- une architecture frontend / backend,

\- une chaîne d’intégration continue (CI) avec tests automatisés.



---



\## 🧭 Contexte technique



Le projet repose sur :

\- \*\*FastAPI\*\* pour l’API backend,

\- \*\*Docker\*\* pour la conteneurisation,

\- \*\*GitHub Actions\*\* pour l’automatisation CI/CD,

\- \*\*Docker Hub\*\* pour l’hébergement des images Docker.



Le déploiement continu est déclenché \*\*uniquement après validation des tests\*\*.



---



\## 🐳 Image Docker publiée



\### 📦 Nom de l’image



L’image publiée correspond au \*\*backend FastAPI\*\* :



<DOCKER\_USERNAME>/fastia-backend





---



\### 🏷️ Tags utilisés



Deux tags sont générés automatiquement :



\- \*\*`latest`\*\*  

&nbsp; → dernière version stable



\- \*\*`<git-sha>`\*\*  

&nbsp; → hash du commit Git correspondant à l’image



Ce mécanisme permet une \*\*traçabilité complète\*\* entre le code source et l’image déployée.



---



\## 🔁 Pipeline CI/CD



Le pipeline de déploiement suit les étapes suivantes :



Push sur main

↓

GitHub Actions

↓

Tests pytest (CI)

↓

Build image Docker

↓

Push sur Docker Hub (CD)



yaml

Copier le code



---



\## ⚙️ Workflow GitHub Actions



Le déploiement continu est implémenté via le workflow :



.github/workflows/docker-publish.yml



yaml

Copier le code



Fonctionnalités clés :

\- déclenchement sur `push` de la branche `main`,

\- authentification sécurisée à Docker Hub via \*\*Secrets GitHub\*\*,

\- build de l’image Docker backend,

\- publication automatique sur Docker Hub,

\- utilisation du cache Docker pour optimiser les builds.



---



\## 🔐 Gestion des secrets



Les identifiants Docker Hub sont stockés de manière sécurisée via les \*\*Secrets GitHub\*\* :



\- `DOCKER\_USERNAME`

\- `DOCKER\_PASSWORD`



Aucun identifiant n’est présent en clair dans le dépôt.



---



\## 📦 Utilisation de l’image Docker



\### ⬇️ Récupérer l’image



```bash

docker pull <DOCKER\_USERNAME>/fastia-backend:latest

▶️ Lancer le conteneur

bash

Copier le code

docker run -p 8000:8000 <DOCKER\_USERNAME>/fastia-backend:latest

L’API est accessible à l’adresse :



arduino

Copier le code

http://localhost:8000

Documentation Swagger :



bash

Copier le code

http://localhost:8000/docs

🧠 Version applicative

Un fichier .env est présent à la racine du projet :



env

Copier le code

APP\_VERSION=latest

Cette variable permet d’aligner la version applicative avec l’image Docker publiée.



✅ Critères du brief couverts

Déploiement automatique sur Docker Hub



Tags latest et hash Git



Secrets sécurisés



Cache Docker activé



CI et CD intégrés dans une chaîne fluide



Images traçables et reproductibles







