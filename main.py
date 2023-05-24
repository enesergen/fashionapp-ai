from fastapi import FastAPI, File, UploadFile
from models import Clothes
from keras.models import load_model
from clothes_classifying import image_classifying
from dominant_color import dominant_color
from PIL import Image
import requests
from io import BytesIO
import shutil
app=FastAPI()

model=load_model("C:/Python/tensorflow/Model_6_h5.h5")

#uvicorn main:app --reload 
@app.post("/api/v1/clothes")
async def clothes_classifying(clothes:Clothes):
    res=requests.get(clothes.url,stream=True)
    if(res.status_code==200):
        with open("img.jpg",'wb') as f:
            shutil.copyfileobj(res.raw,f)
            print("dosya yazıldı")
    else:
        print("img coulnd not")
    img_path="./img.jpg"
    clothes_type=image_classifying(model,img_path)
    print(clothes_type)
    dominant_color1=dominant_color(img_path)
    print(dominant_color)
    return {"clothes_type":clothes_type,
            "dominant_color":dominant_color1}

