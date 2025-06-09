from src.nutribot import NutriBot
import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import os
import matplotlib.pyplot as plt
from PIL import Image, ImageTk 

class NutriBotGUI:
    def __init__(self, root):
        self.bot = NutriBot()
        self.historial_path = "historial.json"

        self.root = root
        self.root.title("NutriBot – Asistente Nutricional Inteligente")
        self.root.geometry("450x550")
        self.root.configure(bg="#f5f5f5")

        # Estilos
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#f5f5f5", font=("Segoe UI", 10), foreground="#333")
        style.configure("TButton", font=("Segoe UI", 10))
        style.configure("TCombobox", font=("Segoe UI", 10))

        # Logo
        logo_path = "assets/nutribot_logo.png"
        logo_img = Image.open(logo_path).resize((100, 100))
        self.logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(root, image=self.logo, bg="#f5f5f5")
        logo_label.pack(pady=(10, 5))

        # Interfaz
        ttk.Label(root, text="Selecciona tu objetivo:").pack(pady=(5, 0))
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

        self.btn_recomendar = ttk.Button(root, text="✅ Obtener recomendación", command=self.obtener_recomendacion)
        self.btn_recomendar.pack(pady=15)

        self.resultado_text = tk.Text(root, height=6, width=55, wrap="word", font=("Segoe UI", 9))
        self.resultado_text.pack(padx=10)

        self.btn_historial = ttk.Button(root, text="📜 Ver Historial", command=self.mostrar_historial)
        self.btn_historial.pack(pady=(10, 5))

        self.btn_estadisticas = ttk.Button(root, text="📊 Ver Estadísticas", command=self.mostrar_estadisticas)
        self.btn_estadisticas.pack(pady=(0, 10))

    def obtener_recomendacion(self):
        objetivo = self.objetivo_var.get()
        actividad = self.actividad_var.get()
        dieta = self.dieta_var.get()

        recomendacion = self.bot.obtener_recomendacion(objetivo, actividad, dieta)

        self.resultado_text.delete(1.0, tk.END)

        if recomendacion:
            self.resultado_text.insert(tk.END, f"Recomendación para:\n- Objetivo: {objetivo}\n- Actividad: {actividad}\n- Dieta: {dieta}\n\n{recomendacion}")
            self.guardar_en_historial(objetivo, actividad, dieta, recomendacion)
        else:
            self.resultado_text.insert(tk.END, "❌ No se encontró una recomendación para esa combinación.")

    def guardar_en_historial(self, objetivo, actividad, dieta, recomendacion):
        entrada = {
            "fecha": datetime.now().isoformat(),
            "objetivo": objetivo,
            "actividad": actividad,
            "dieta": dieta,
            "recomendacion": recomendacion
        }

        if os.path.exists(self.historial_path):
            with open(self.historial_path, 'r', encoding='utf-8') as f:
                historial = json.load(f)
        else:
            historial = []

        historial.append(entrada)

        with open(self.historial_path, 'w', encoding='utf-8') as f:
            json.dump(historial, f, indent=4, ensure_ascii=False)

    def mostrar_historial(self):
        if not os.path.exists(self.historial_path):
            messagebox.showinfo("Historial", "No hay historial aún.")
            return

        with open(self.historial_path, 'r', encoding='utf-8') as f:
            historial = json.load(f)

        historial_text = "\n\n".join([
            f"[{datetime.fromisoformat(item['fecha']).strftime('%d-%m-%Y %H:%M')}]\nObjetivo: {item['objetivo']}\nActividad: {item['actividad']}\nDieta: {item['dieta']}\nRecomendación: {item['recomendacion']}"
            for item in historial[-10:]
        ])

        top = tk.Toplevel(self.root)
        top.title("Historial de Recomendaciones")
        text_area = tk.Text(top, wrap="word", height=20, width=60)
        text_area.pack(padx=10, pady=10)
        text_area.insert(tk.END, historial_text)
        text_area.config(state=tk.DISABLED)

    def mostrar_estadisticas(self):
        if not os.path.exists(self.historial_path):
            messagebox.showinfo("Estadísticas", "No hay datos suficientes.")
            return

        with open(self.historial_path, 'r', encoding='utf-8') as f:
            historial = json.load(f)

        conteo_dietas = {}
        for entrada in historial:
            dieta = entrada["dieta"]
            conteo_dietas[dieta] = conteo_dietas.get(dieta, 0) + 1

        plt.bar(conteo_dietas.keys(), conteo_dietas.values(), color='skyblue')
        plt.title("Tipos de dieta más consultados")
        plt.ylabel("Número de consultas")
        plt.xlabel("Tipo de dieta")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = NutriBotGUI(root)
    root.mainloop()
