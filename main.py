from fastapi import FastAPI
from models import Clothes
from keras.models import load_model

from clothes_classifying import image_classifying
from dominant_color import dominant_color
app=FastAPI()

model=load_model("C:/Python/tensorflow/Model_6_h5.h5")

#uvicorn main:app --reload 
@app.post("/api/v1/clothes")
async def clothes_classifying(clothes:Clothes):
    clothes_type=image_classifying(model,clothes.url)
    print(clothes_type)
    dominant_color1=dominant_color(clothes.url)
    print(dominant_color)
    return {"clothes_type":clothes_type,
            "dominant_color":dominant_color1}