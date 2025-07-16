from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import tensorflow as tf
import io
from contextlib import asynccontextmanager

class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Chargement du modèle au démarrage
    app.state.model = tf.keras.models.load_model("model/fashion_mnist_mobilenetv2.keras")
    print("✅ Modèle chargé avec succès.")
    yield
    # Ici tu peux ajouter du code de nettoyage si besoin

app = FastAPI(lifespan=lifespan)

# Endpoint de prédiction
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        image = image.resize((224, 224))
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # batch

        predictions = app.state.model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0]))

        return JSONResponse(content={
            "class": predicted_class,
            "confidence": confidence
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)