from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger

from modules.calcul import calcul_carre

app = FastAPI(title="FastIA API")

class InputData(BaseModel):
    value: int

@app.get("/")
def root():
    logger.info("Route / appelée")
    return {"message": "API FastIA opérationnelle"}

@app.get("/health")
def health():
    logger.info("Healthcheck OK")
    return {"status": "healthy"}

@app.post("/calcul")
def calcul(data: InputData):
    logger.info(f"Calcul demandé pour {data.value}")
    result = calcul_carre(data.value)
    return {"result": result}
