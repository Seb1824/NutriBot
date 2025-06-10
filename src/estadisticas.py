def calcular_estadisticas(historial):
    conteo_dietas = {}
    conteo_objetivos = {}
    conteo_actividad = {}

    for entrada in historial:
        conteo_dietas[entrada["dieta"]] = conteo_dietas.get(entrada["dieta"], 0) + 1
        conteo_objetivos[entrada["objetivo"]] = conteo_objetivos.get(entrada["objetivo"], 0) + 1
        conteo_actividad[entrada["actividad"]] = conteo_actividad.get(entrada["actividad"], 0) + 1

    return conteo_dietas, conteo_objetivos, conteo_actividad
