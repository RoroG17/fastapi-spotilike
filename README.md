# Spotilike

Une application de streaming musical construite avec FastAPI (backend) et Quasar/Vue 3 (frontend).

## Configuration du projet

### Backend (FastAPI)

1. Accédez au dossier backend :
```bash
cd backend
```

2. Installez les dépendances Python requises :
```bash
pip install fastapi uvicorn sqlmodel python-jose python-multipart
```

3. Créez et initialisez la base de données avec le jeu de données :
```bash
python seeder.py
```
Cette commande va :
- Créer la base de données SQLite (`spotilike.db`)
- Insérer des données de test (genres, artistes, albums, morceaux)
- Créer un utilisateur de test (username: "admin", password: "1234")

4. Lancez le serveur backend :
```bash
uvicorn main:app --reload --port 8000
```
Le serveur sera accessible à l'adresse : http://localhost:8000

### Frontend (Quasar/Vue 3)

1. Accédez au dossier frontend :
```bash
cd frontend
```

2. Installez les dépendances Node.js :
```bash
npm install
# ou si vous utilisez yarn :
yarn
```

3. Lancez le serveur de développement :
```bash
quasar dev

L'application sera accessible à l'adresse : http://localhost:9000

## Tester l'application

1. Lancez les deux serveurs (backend et frontend) comme indiqué ci-dessus
2. Accédez à http://localhost:9000 dans votre navigateur
3. Vous pouvez vous connecter avec les identifiants suivants :
   - Utilisateur : `admin`
   - Mot de passe : `1234`

## Structure du projet

- `backend/` : API FastAPI
  - `main.py` : Points d'entrée de l'API
  - `seeder.py` : Script pour générer les données de test
  - `models/` : Modèles de données SQLModel
  - `db/` : Configuration de la base de données

- `frontend/` : Application Quasar/Vue 3
  - `src/` : Code source
  - `src/pages/` : Pages de l'application
  - `src/components/` : Composants réutilisables
  - `src/boot/` : Configuration (axios, etc.)