from src.nutribot import NutriBot
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
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
        self.root.geometry("600x850")
        self.root.configure(bg="#e6f2ff")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#e6f2ff", font=("Segoe UI", 15), foreground="#003366")
        style.configure("TButton", font=("Segoe UI", 15, "bold"), padding=8, relief="flat", background="#004080", foreground="white")
        style.configure("TCombobox", font=("Segoe UI", 20, "bold"))
        style.map("TButton",
                  background=[("active", "#0059b3")],
                  foreground=[("active", "white")])

        big_font = tkFont.Font(family="Segoe UI", size=15)
        style.configure("CustomCombobox.TCombobox", font=big_font)
        root.option_add("*TCombobox*Listbox*Font", big_font)

        # Notebook (pestañas)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        notebook.configure(style="Custom.TNotebook")

        # Estilo personalizado para el Notebook
        style.configure("Custom.TNotebook", background="#e6f2ff", borderwidth=0)
        style.configure("Custom.TNotebook.Tab", background="#e6f2ff", foreground="#003366", font=("Segoe UI", 15))
        style.map("Custom.TNotebook.Tab",
                  background=[("selected", "#cce6ff"), ("active", "#e6f2ff")],
                  foreground=[("selected", "#003366"), ("active", "#003366")])
        style.layout("Custom.TNotebook", [
            ('Notebook.client', {'sticky': 'nswe'})
        ])

        # Asegura que los frames de las pestañas tengan el mismo fondo
        self.tab_recomendar = ttk.Frame(notebook, style="Custom.TFrame")
        self.tab_historial = ttk.Frame(notebook, style="Custom.TFrame")
        self.tab_estadisticas = ttk.Frame(notebook, style="Custom.TFrame")
        style.configure("Custom.TFrame", background="#e6f2ff")

        notebook.add(self.tab_recomendar, text="🏋️ Recomendación")
        notebook.add(self.tab_historial, text="📜 Historial")
        notebook.add(self.tab_estadisticas, text="📊 Estadísticas")

        # ---------- PESTAÑA RECOMENDACIÓN ----------
        self.init_recomendacion_tab()
        self.init_historial_tab()
        self.init_estadisticas_tab()

        # ---------- BOTÓN SALIR (abajo fuera del notebook) ----------
        ttk.Separator(self.root, orient='horizontal').pack(fill='x', pady=(0, 5))
        self.btn_salir = ttk.Button(self.root, text="❌ Salir del programa", command=self.root.quit)
        self.btn_salir.pack(pady=(0, 10))

    def init_recomendacion_tab(self):
        logo_path = "assets/nutribot_logo.png"
        logo_img = Image.open(logo_path).resize((150, 90))
        self.logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(self.tab_recomendar, image=self.logo, bg="#e6f2ff")
        logo_label.pack(pady=(10, 5))

        frame = ttk.LabelFrame(self.tab_recomendar, text="💡 Tu Información", padding=10)
        frame.configure(style="Custom.TLabelframe")
        frame.pack(padx=10, pady=10, fill="both", expand=False)

        # Aplica el color de fondo al estilo del LabelFrame
        style = ttk.Style()
        style.configure("Custom.TLabelframe", background="#e6f2ff")
        style.configure("Custom.TLabelframe.Label", background="#e6f2ff")

        ttk.Label(frame, text="Objetivo nutricional:").pack(anchor="w", pady=(5, 0))
        self.objetivo_var = tk.StringVar()
        objetivos = ['[Seleccionar]','perder_grasa', 'subir_masa', 'mantener_peso', 'mejorar_salud_digestiva']
        self.objetivo_combo = ttk.Combobox(
            frame, textvariable=self.objetivo_var, values=objetivos, state="readonly", style="CustomCombobox.TCombobox"
        )
        self.objetivo_combo.pack(fill="x", pady=5)
        self.objetivo_combo.current(0)

        ttk.Label(frame, text="Nivel de actividad física:").pack(anchor="w", pady=(10, 0))
        self.actividad_var = tk.StringVar()
        actividades = ['[Seleccionar]','sedentario', 'moderado', 'activo', 'intermitente']
        self.actividad_combo = ttk.Combobox(
            frame, textvariable=self.actividad_var, values=actividades, state="readonly", style="CustomCombobox.TCombobox"
        )
        self.actividad_combo.pack(fill="x", pady=5)
        self.actividad_combo.current(0)

        ttk.Label(frame, text="Tipo de dieta preferido:").pack(anchor="w", pady=(10, 0))
        self.dieta_var = tk.StringVar()
        dietas = ['[Seleccionar]','omnivoro', 'vegetariano', 'vegano', 'ayuno_variable']
        self.dieta_combo = ttk.Combobox(
            frame, textvariable=self.dieta_var, values=dietas, state="readonly", style="CustomCombobox.TCombobox"
        )
        self.dieta_combo.pack(fill="x", pady=5)
        self.dieta_combo.current(0)

        self.btn_recomendar = ttk.Button(self.tab_recomendar, text="✅ Obtener recomendación", command=self.obtener_recomendacion)
        self.btn_recomendar.pack(pady=(10, 5))

        self.resultado_text = tk.Text(self.tab_recomendar, height=15, wrap="word", font=("Segoe UI", 15), bg="#ffffff", relief="solid", bd=1)
        self.resultado_text.pack(padx=15, pady=(5, 5), fill="both", expand=False)

        self.btn_limpiar = ttk.Button(self.tab_recomendar, text="🔄 Limpiar campos", command=self.limpiar_campos)
        self.btn_limpiar.pack(pady=(0, 10))

    def init_historial_tab(self):
        self.btn_historial = ttk.Button(self.tab_historial, text="📜 Ver Historial", command=self.mostrar_historial)
        self.btn_historial.pack(pady=(20, 10))

    def init_estadisticas_tab(self):
        self.btn_estadisticas = ttk.Button(self.tab_estadisticas, text="📊 Ver Estadísticas", command=self.mostrar_estadisticas)
        self.btn_estadisticas.pack(pady=(20, 10))

    def obtener_recomendacion(self):
        objetivo = self.objetivo_var.get()
        actividad = self.actividad_var.get()
        dieta = self.dieta_var.get()

        if (objetivo == '[Seleccionar]' or actividad == '[Seleccionar]' or dieta == '[Seleccionar]'):
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

        historial = []
        if os.path.exists(self.historial_path):
            with open(self.historial_path, 'r', encoding='utf-8') as f:
                historial = json.load(f)

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
        text_area = tk.Text(top, wrap="word", height=20, width=70)
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
