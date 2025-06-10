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
        self.root.geometry("500x800")
        self.root.configure(bg="#f5f5f5")

        # Estilo
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#f5f5f5", font=("Segoe UI", 10), foreground="#333")
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("TCombobox", font=("Segoe UI", 10))

        # Notebook (pestañas)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_recomendar = ttk.Frame(notebook)
        self.tab_historial = ttk.Frame(notebook)
        self.tab_estadisticas = ttk.Frame(notebook)

        notebook.add(self.tab_recomendar, text="🏋️ Recomendación")
        notebook.add(self.tab_historial, text="📜 Historial")
        notebook.add(self.tab_estadisticas, text="📊 Estadísticas")

        # ---------- PESTAÑA RECOMENDACIÓN ----------
        logo_path = "assets/nutribot_logo.png"
        logo_img = Image.open(logo_path).resize((100, 100))
        self.logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(self.tab_recomendar, image=self.logo, bg="#f5f5f5")
        logo_label.pack(pady=(10, 5))

        ttk.Label(self.tab_recomendar, text="Selecciona tu objetivo:").pack(pady=(5, 0))
        self.objetivo_var = tk.StringVar()
        objetivos = ['perder_grasa', 'subir_masa', 'mantener_peso']
        self.objetivo_combo = ttk.Combobox(root, textvariable=self.objetivo_var, values=objetivos, state="readonly")
        self.objetivo_combo.pack(pady=5)
        self.objetivo_combo.current(0)

        ttk.Label(self.tab_recomendar, text="Selecciona tu nivel de actividad:").pack(pady=(10, 0))
        self.actividad_var = tk.StringVar()
        actividades = ['sedentario', 'moderado', 'activo']
        self.actividad_combo = ttk.Combobox(root, textvariable=self.actividad_var, values=actividades, state="readonly")
        self.actividad_combo.pack(pady=5)
        self.actividad_combo.current(0)

        ttk.Label(self.tab_recomendar, text="Selecciona tu tipo de dieta:").pack(pady=(10, 0))
        self.dieta_var = tk.StringVar()
        dietas = ['omnivoro', 'vegetariano', 'vegano']
        self.dieta_combo = ttk.Combobox(root, textvariable=self.dieta_var, values=dietas, state="readonly")
        self.dieta_combo.pack(pady=5)
        self.dieta_combo.current(0)

        self.btn_recomendar = ttk.Button(self.tab_recomendar, text="✅ Obtener recomendación", command=self.obtener_recomendacion)
        self.btn_recomendar.pack(pady=15)

        self.resultado_text = tk.Text(self.tab_recomendar, height=7, width=100, wrap="word", font=("Segoe UI", 9), bg="#ffffff", relief="solid", bd=1)
        self.resultado_text.pack(padx=10)

        self.btn_limpiar = ttk.Button(self.tab_recomendar, text="🔄 Limpiar", command=self.limpiar_campos)
        self.btn_limpiar.pack(pady=(5, 10))

        self.btn_salir = ttk.Button(self.root, text="❌ Salir", command=self.root.quit)
        self.btn_salir.pack(pady=(0, 10))

        # ---------- PESTAÑA HISTORIAL ----------
        self.btn_historial = ttk.Button(self.tab_historial, text="📜 Ver Historial", command=self.mostrar_historial)
        self.btn_historial.pack(pady=(20, 10))

        # ---------- PESTAÑA ESTADÍSTICAS ----------
        self.btn_estadisticas = ttk.Button(self.tab_estadisticas, text="📊 Ver Estadísticas", command=self.mostrar_estadisticas)
        self.btn_estadisticas.pack(pady=(20, 10))

        # ---------- BOTÓN SALIR (fuera del notebook) ----------
        self.btn_salir = ttk.Button(self.root, text="❌ Salir", command=self.root.quit)
        self.btn_salir.pack(pady=(5, 10))

    def obtener_recomendacion(self):
        objetivo = self.objetivo_var.get()
        actividad = self.actividad_var.get()
        dieta = self.dieta_var.get()

        if not (objetivo and actividad and dieta):
            messagebox.showwarning("Faltan datos", "Por favor, selecciona todas las opciones.")
            return

        recomendacion = self.bot.obtener_recomendacion(objetivo, actividad, dieta)

        self.resultado_text.delete(1.0, tk.END)

        if recomendacion:
            self.resultado_text.insert(tk.END, f"Recomendación para:\n- Objetivo: {objetivo}\n- Actividad: {actividad}\n- Dieta: {dieta}\n\n{recomendacion}")
            self.guardar_en_historial(objetivo, actividad, dieta, recomendacion)
        else:
            self.resultado_text.insert(tk.END, "❌ No se encontró una recomendación para esa combinación.\n\nTe recomendamos consultar con un nutricionista profesional o ajustar tu objetivo.")

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
        conteo_objetivos = {}
        conteo_actividad = {}

        for entrada in historial:
            conteo_dietas[entrada["dieta"]] = conteo_dietas.get(entrada["dieta"], 0) + 1
            conteo_objetivos[entrada["objetivo"]] = conteo_objetivos.get(entrada["objetivo"], 0) + 1
            conteo_actividad[entrada["actividad"]] = conteo_actividad.get(entrada["actividad"], 0) + 1

        _, ax = plt.subplots(1, 3, figsize=(20, 4))

        ax[0].bar(conteo_dietas.keys(), conteo_dietas.values(), color='skyblue')
        ax[0].set_title("Tipos de dieta más consultados")
        ax[0].tick_params(axis='x', rotation=30)

        ax[1].bar(conteo_objetivos.keys(), conteo_objetivos.values(), color='salmon')
        ax[1].set_title("Objetivos más comunes")
        ax[1].tick_params(axis='x', rotation=30)

        ax[2].bar(conteo_actividad.keys(), conteo_actividad.values(), color='lightgreen')
        ax[2].set_title("Nivel de actividad")
        ax[2].tick_params(axis='x', rotation=30)

        plt.tight_layout()
        plt.show()

    def limpiar_campos(self):
        self.objetivo_combo.current(0)
        self.actividad_combo.current(0)
        self.dieta_combo.current(0)
        self.resultado_text.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = NutriBotGUI(root)
    root.mainloop()