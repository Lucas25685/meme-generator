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

## 🏗️ Configuration Serverless

```yaml
service: S3MemeStorage

provider:
  name: aws
  runtime: nodejs20.x
  stage: dev
  region: us-east-1
  environment:
    S3_BUCKET: ${self:service}-${opt:stage, self:provider.stage}
  iam:
    role:
      statements:
        - Effect: Allow
          Action:
            - s3:PutObject
          Resource:
            - "arn:aws:s3:::${self:provider.environment.S3_BUCKET}"

functions:
  MemeGenerator:
    handler: meme_generator.handler
    runtime: python3.11
    events:
      - http:
          path: upload
          method: post
          request:
            schemas:
              application/json:
                schema:
                  type: object
                  properties:
                    image:
                      type: string
                      description: "Base64 encoded image"
                    text-top:
                      type: string
                      description: "Texte en haut"
                    text-bottom:
                      type: string
                      description: "Texte en bas"
                  required:
                    - image
                    - text-top
                    - text-bottom

plugins:
  - serverless-offline
  - serverless-s3-local

custom:
  s3:
    host: localhost
    port: 4569
    directory: .s3
    accessKeyId: S3RVER
    secretAccessKey: S3RVER
    bucketName: ${self:provider.environment.S3_BUCKET}

resources:
  Resources:
    UrlStorage:
      Type: AWS::S3::Bucket
      Properties:
        BucketName: ${self:provider.environment.S3_BUCKET}
```

## 📄 Licence
MIT

