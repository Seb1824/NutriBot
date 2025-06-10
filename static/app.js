function obtenerRecomendacion() {
    const objetivo = document.getElementById('objetivo').value;
    const actividad = document.getElementById('actividad').value;
    const dieta = document.getElementById('dieta').value;

    fetch("http://localhost:5000/recomendar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            objetivo: objetivo,
            actividad: actividad,
            dieta: dieta
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.recomendacion) {
            document.getElementById("resultado").textContent = data.recomendacion;
        } else {
            document.getElementById("resultado").textContent = "Error: No se recibió una recomendación.";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("resultado").textContent = "❌ Error al contactar con el servidor.";
    });
}
