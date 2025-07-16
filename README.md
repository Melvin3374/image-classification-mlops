# Image Classification MLOps Project

## 🚀 Objectif

Créer un pipeline MLOps complet :
- Entraîner un modèle de classification d'images.
- Créer une API FastAPI permettant de servir le modèle.
- Conteneuriser avec Docker.
- Déployer sur une instance EC2 AWS.
- Rendre le service accessible publiquement.

---

## 📂 Structure du projet

app/ : API FastAPI

model/ : modèle entraîné fashion_mnist_mobilenetv2.keras

requirements.txt : dépendances

Dockerfile : image Docker de l'API

README.md : ce fichier

---

## 🧠 Modèle utilisé

Base : MobileNetV2 pré-entraîné sur ImageNet

Images redimensionnées : 224x224

Optimizer : Adam

Loss : SparseCategoricalCrossentropy

Epochs : 2 (pour CPU EC2 rapide)

Accuracy : ~85% entraînement, ~83% validation

---

## ⚙️ API FastAPI

Endpoint :

POST /predict : upload image (file) ➔ JSON avec class et confidence.

GET /docs : documentation Swagger.

---

## 🐳 Docker

Dockerfile :

```sh
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📦 Commandes Docker utilisées

```sh
docker build -t image-classification-api .
docker run -p 8000:8000 image-classification-api
docker push melvin3374/image-classification-api:latest

# Sur EC2
sudo docker pull melvin3374/image-classification-api:latest
sudo docker run -d -p 8000:8000 melvin3374/image-classification-api:latest
```

---


## 5️⃣ Contenu du Dockerfile et explications

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 📦 Commandes Docker utilisées

```sh
docker build -t image-classification-api .
docker run -p 8000:8000 image-classification-api
docker push melvin3374/image-classification-api:latest

# Sur EC2
sudo docker pull melvin3374/image-classification-api:latest
sudo docker run -d -p 8000:8000 melvin3374/image-classification-api:latest
```

---

## ☁️ Déploiement EC2

1️⃣ Créer une instance EC2 Ubuntu (t2.micro) avec clé SSH
2️⃣ Ouvrir le port 8000 (groupe de sécurité)
3️⃣ Installer Docker
4️⃣ Pull l'image et run

---

## 🛠️ Exemple de requête

```sh
curl -X POST "http://13.38.36.221:8000/predict" \
  -H "accept: application/json" \
  -F "file=@image.jpg"
```

---

## 🔗 Liens

API déployée : http://13.38.36.221:8000/docs

Image Docker : Docker Hub - melvin3374/image-classification-api
               https://hub.docker.com/repository/docker/melvin3374/image-classification-api/general

Repo GitHub : (https://github.com/Melvin3374/image-classification-mlops)


