from src.nutribot import NutriBot
import tkinter as tk
from tkinter import ttk

class NutriBotGUI:
    def __init__(self, root):
        self.bot = NutriBot()

        self.root = root
        self.root.title("NutriBot – Asistente Nutricional Inteligente")
        self.root.geometry("400x350")

        ttk.Label(root, text="Selecciona tu objetivo:").pack(pady=(10, 0))
        self.objetivo_var = tk.StringVar()
        objetivos = ['perder_grasa', 'subir_masa', 'mantener_peso']
        self.objetivo_combo = ttk.Combobox(root, textvariable=self.objetivo_var, values=objetivos, state="readonly")
        self.objetivo_combo.pack(pady=5)
        self.objetivo_combo.current(0)

        ttk.Label(root, text="Selecciona tu nivel de actividad:").pack(pady=(10, 0))
        self.actividad_var = tk.StringVar()
        actividades = ['sedentario', 'moderado', 'activo']
        self.actividad_combo = ttk.Combobox(root, textvariable=self.actividad_var, values=actividades, state="readonly")
        self.actividad_combo.pack(pady=5)
        self.actividad_combo.current(0)

        ttk.Label(root, text="Selecciona tu tipo de dieta:").pack(pady=(10, 0))
        self.dieta_var = tk.StringVar()
        dietas = ['omnivoro', 'vegetariano', 'vegano']
        self.dieta_combo = ttk.Combobox(root, textvariable=self.dieta_var, values=dietas, state="readonly")
        self.dieta_combo.pack(pady=5)
        self.dieta_combo.current(0)

        self.btn_recomendar = ttk.Button(root, text="Obtener recomendación", command=self.obtener_recomendacion)
        self.btn_recomendar.pack(pady=20)

        self.resultado_text = tk.Text(root, height=5, width=45, wrap="word")
        self.resultado_text.pack(padx=10)

    def obtener_recomendacion(self):
        objetivo = self.objetivo_var.get()
        actividad = self.actividad_var.get()
        dieta = self.dieta_var.get()

        recomendacion = self.bot.obtener_recomendacion(objetivo, actividad, dieta)

        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, f"Recomendación para:\n- Objetivo: {objetivo}\n- Actividad: {actividad}\n- Dieta: {dieta}\n\n{recomendacion}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NutriBotGUI(root)
    root.mainloop()
