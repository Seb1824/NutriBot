import os
from pyswip import Prolog

class NutriBot:
    def __init__(self):
        self.prolog = Prolog()
        base_path = os.path.dirname(os.path.abspath(__file__))
        ruta_relativa = os.path.join(base_path, "..", "prolog", "reglas.pl")
        ruta_absoluta = os.path.abspath(ruta_relativa).replace('\\', '/')
        print("Consultando reglas desde ruta absoluta:", ruta_absoluta)

        # Forma manual de consultar con la ruta entre comillas dobles
        consulta_str = f'consult("{ruta_absoluta}").'
        list(self.prolog.query(consulta_str))

    def obtener_recomendacion(self, objetivo, actividad, dieta):
        consulta = f"nutricion('{objetivo}', '{actividad}', '{dieta}', Recomendacion)."
        resultados = list(self.prolog.query(consulta))
        if resultados:
            return resultados[0]["Recomendacion"]
        else:
            return "❌ No se encontró una recomendación para esa combinación"