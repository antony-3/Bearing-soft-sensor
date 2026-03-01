import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from model import train_model, predict

app = FastAPI()

class BearingInput(BaseModel):
    vib_x: float
    vib_y: float
    vib_z: float

@app.on_event("startup")
def startup():
    train_model()

@app.post("/predict")
async def get_prediction(data:BearingInput):
    result = predict(data.vib_x, data.vib_y, data.vib_z)
    return {'predicted_wear': round(result, 2)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
