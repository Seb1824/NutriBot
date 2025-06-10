import json
import os
from datetime import datetime

HISTORIAL_PATH = "historial.json"

def cargar_historial():
    if os.path.exists(HISTORIAL_PATH):
        with open(HISTORIAL_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_en_historial(objetivo, actividad, dieta, recomendacion):
    historial = cargar_historial()
    entrada = {
        "fecha": datetime.now().isoformat(),
        "objetivo": objetivo,
        "actividad": actividad,
        "dieta": dieta,
        "recomendacion": recomendacion
    }
    historial.append(entrada)
    with open(HISTORIAL_PATH, 'w', encoding='utf-8') as f:
        json.dump(historial, f, indent=4, ensure_ascii=False)

def limpiar_historial():
    with open(HISTORIAL_PATH, 'w', encoding='utf-8') as f:
        json.dump([], f)
