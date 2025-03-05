# S3MemeStorage

S3MemeStorage est un service permettant de stocker et de générer des memes en utilisant AWS S3 et une fonction serverless en Python.

## 🛠️ Technologies utilisées

- **AWS S3** pour le stockage des images
- **AWS Lambda** avec Python 3.11 pour le traitement des images
- **Serverless Framework** pour la gestion du déploiement
- **serverless-offline** et **serverless-s3-local** pour le développement local

## 🚀 Installation et configuration

### 1️⃣ Prérequis

Assurez-vous d'avoir installé :
- [Node.js](https://nodejs.org/)
- [Serverless Framework](https://www.serverless.com/)
- [AWS CLI](https://aws.amazon.com/cli/)

### 2️⃣ Configuration AWS (local)

Configurer les identifiants AWS pour le mode local :
```sh
aws configure set aws_access_key_id S3RVER
aws configure set aws_secret_access_key S3RVER
aws configure set region us-east-1
```
Création du bucket S3 :
```sh
aws --endpoint-url=http://localhost:4569 s3 mb s3://s3memestorage-dev
```
### 3️⃣ Installation des dépendances

```sh
npm install
```

### 4️⃣ Lancer le projet en local

Démarrer le service avec Serverless Offline et S3 local :
```sh
serverless offline 
```

## 📤 API Endpoint

### **Upload d'un meme**
- **Méthode :** `POST`
- **Endpoint :** `/upload`
- **Payload (JSON) :**
  ```json
  {
    "image": "Base64 encoded image",
    "text-top": "Texte en haut",
    "text-bottom": "Texte en bas"
  }
  ```

