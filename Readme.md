# 🚀 FastAPI-CRUD

API REST moderne construite avec **FastAPI**, **Pydantic v2** et **SQLAlchemy 2**, connectée à une base de données **MySQL**.

Ce projet sert de base propre et professionnelle pour :

* APIs backend avec FastAPI
* microservices
* intégration avec des apps frontend ou mobiles

---

## 🧱 Stack technique

* **Python** 3.10+
* **FastAPI** — framework web rapide et moderne
* **Uvicorn** — serveur ASGI
* **Pydantic v2** — validation et sérialisation des données
* **SQLAlchemy 2.x** — ORM
* **MySQL** — base de données relationnelle
* **PyMySQL** — driver MySQL

---

## 📁 Structure du projet

```text
.
├── app/
│   ├── main.py            # Point d'entrée de l'API
│   ├── database.py        # Connexion DB et session
│   ├── models.py          # Modèles Pydantic
│   ├── database_models.py # Modèles SQLAlchemy
├── requirements.txt       # Dependecies
├── .env.example
├── README.md
└── .venv/
```

---

## ⚙️ Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/branGitfox/FastAPI-CRUD.git
cd FastAPI-CRUD
```

---

### 2️⃣ Créer et activer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# .venv\\Scripts\\activate  # Windows
```

---

### 3️⃣ Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

---



## 🗄️ Base de données

### URL SQLAlchemy

```python
mysql+pymysql://USER:PASSWORD@HOST:PORT/DB_NAME
```

### Création automatique des tables

Dans `database.py` ou `main.py` :

```python
Base.metadata.create_all(bind=engine)
```

---

## ▶️ Lancer l'application

⚠️ Toujours lancer avec le bon environnement Python :

```bash
python -m uvicorn app.main:app --reload
```

📍 API disponible sur :

```
http://127.0.0.1:8000
```

---

## 📚 Documentation automatique

FastAPI génère automatiquement la documentation :

* Swagger UI 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc 👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

