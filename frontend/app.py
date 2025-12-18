import streamlit as st
import requests
from loguru import logger

API_URL = "http://backend:8000/calcul"

st.title("FastIA - Calcul du carré")

value = st.number_input("Entrez un entier", step=1)

if st.button("Calculer"):
    try:
        response = requests.post(API_URL, json={"value": int(value)})
        result = response.json()["result"]
        st.success(f"Résultat : {result}")
        logger.info(f"Calcul frontend OK pour {value}")
    except Exception as e:
        logger.error(e)
        st.error("Erreur API")
