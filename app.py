from flask import Flask, render_template, request, jsonify
from src.nutribot import NutriBot

app = Flask(__name__)
bot = NutriBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recomendar', methods=['POST'])
def recomendar():
    data = request.json
    objetivo = data.get('objetivo')
    actividad = data.get('actividad')
    dieta = data.get('dieta')

    if not all([objetivo, actividad, dieta]):
        return jsonify({"error": "Faltan datos"}), 400

    recomendacion = bot.obtener_recomendacion(objetivo, actividad, dieta)
    return jsonify({"recomendacion": recomendacion})

if __name__ == "__main__":
    app.run(debug=True)
