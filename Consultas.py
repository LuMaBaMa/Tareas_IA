import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class VentanaLogin(ctk.CTkFrame):
    def __init__(self, parent, on_login_exito):
        super().__init__(parent)
        self.parent = parent
        self.on_login_exito = on_login_exito
        self.cargar_usuarios()
        self.titulo = ctk.CTkLabel(
            self, 
            text="📷 SISTEMA DE ANÁLISIS DE CÁMARAS",
            font=("Arial", 28, "bold")
        )
        self.titulo.pack(pady=30)
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.pack(pady=50, padx=50, expand=True)
        
        ctk.CTkLabel(
            self.frame_form, 
            text="INICIAR SESIÓN", 
            font=("Arial", 20, "bold")
        ).pack(pady=20)
        
        ctk.CTkLabel(self.frame_form, text="Usuario:").pack(pady=5)
        self.entry_usuario = ctk.CTkEntry(self.frame_form, width=250, font=("Arial", 14))
        self.entry_usuario.pack(pady=5)
        
        ctk.CTkLabel(self.frame_form, text="Contraseña:").pack(pady=5)
        self.entry_password = ctk.CTkEntry(self.frame_form, width=250, show="*", font=("Arial", 14))
        self.entry_password.pack(pady=5)
        self.btn_login = ctk.CTkButton(
            self.frame_form,
            text="Ingresar",
            command=self.verificar_login,
            height=40,
            font=("Arial", 14, "bold"),
            fg_color="#2196F3"
        )
        self.btn_login.pack(pady=20)
        self.label_mensaje = ctk.CTkLabel(
            self.frame_form,
            text="",
            font=("Arial", 12)
        )
        self.label_mensaje.pack()
    
    def cargar_usuarios(self):
        try:
            if os.path.exists("C:\Users\Laptop\Documents\Python\usuarios.csv"):
                self.df_usuarios = pd.read_csv("C:\Users\Laptop\Documents\Python\usuarios.csv")
                print("✅ Usuarios cargados correctamente")
            else:
                datos_usuarios = pd.DataFrame({
                    "username": ["admin", "estudiante", "profe", "juan"],
                    "password": ["admin123", "123456", "clave123", "camaras2024"]
                })
                datos_usuarios.to_csv("C:\Users\Laptop\Documents\Python\usuarios.csv", index=False)
                self.df_usuarios = datos_usuarios
                print("📝 Archivo de usuarios creado automáticamente")
        except Exception as e:
            print(f"❌ Error al cargar usuarios: {e}")
            self.df_usuarios = pd.DataFrame(columns=["username", "password"])
    
    def verificar_login(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()
        
        if not usuario or not password:
            self.label_mensaje.configure(text="❌ Complete todos los campos", text_color="red")
            return
        
        usuario_valido = self.df_usuarios[
            (self.df_usuarios["username"] == usuario) & 
            (self.df_usuarios["password"] == password)
        ]
        
        if not usuario_valido.empty:
            self.label_mensaje.configure(text="✅ Login exitoso", text_color="green")
            self.parent.after(1000, self.on_login_exito)
        else:
            self.label_mensaje.configure(text="❌ Usuario o contraseña incorrectos", text_color="red")

class AppAnalisisCamaras(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Análisis de Cámaras Digitales")
        self.geometry("1400x800")
        
        self.df_camaras = None
        self.df_actual = None
        
        self.cargar_datos_camaras()
        
        self.frame_login = VentanaLogin(self, self.mostrar_app_principal)
        self.frame_login.pack(fill="both", expand=True)
        
        self.frame_principal = None
    
    def cargar_datos_camaras(self):
        try:
            if os.path.exists("csv_camaras_2.csv"):
                self.df_camaras = pd.read_csv("csv_camaras_2.csv")
                print(f"✅ Cargadas {len(self.df_camaras)} cámaras")
            else:
                print("⚠️ No se encontró el archivo, creando datos de ejemplo...")
                datos_ejemplo = {
                    "Model": ["Canon PowerShot A70", "Sony DSC-F717", "Nikon Coolpix 5700", 
                              "Fujifilm FinePix S7000", "Olympus C-8080", "Panasonic Lumix DMC-FZ20"],
                    "Zoom tele (T)": [105, 190, 280, 210, 140, 432],
                    "Normal focus range": [46, 50, 50, 50, 80, 30],
                    "Macro focus range": [5, 2, 3, 1, 5, 5],
                    "Storage included": [16, 32, 32, 16, 32, 16],
                    "Weight (inc. batteries)": [315, 659, 512, 590, 724, 556],
                    "Dimensions": [101, 162, 108, 121, 124, 87],
                    "Price": [139, 149, 229, 229, 179, 149]
                }
                self.df_camaras = pd.DataFrame(datos_ejemplo)
            
            self.df_camaras["Marca"] = self.df_camaras["Model"].apply(lambda x: str(x).split()[0])
            
            self.df_camaras = self.df_camaras.fillna(0)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            messagebox.showerror("Error", f"No se pudieron cargar los datos: {e}")
            self.df_camaras = pd.DataFrame()
    
    def mostrar_app_principal(self):
        self.frame_login.pack_forget()
        
        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.pack(fill="both", expand=True)
        
        frame_superior = ctk.CTkFrame(self.frame_principal)
        frame_superior.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(
            frame_superior,
            text="📊 ANÁLISIS DE CÁMARAS DIGITALES",
            font=("Arial", 24, "bold")
        ).pack(side="left", padx=20)
        
        info_texto = f"Total: {len(self.df_camaras)} cámaras | Precio promedio: ${self.df_camaras['Price'].mean():.0f}"
        ctk.CTkLabel(
            frame_superior,
            text=info_texto,
            font=("Arial", 14)
        ).pack(side="right", padx=20)
        
        self.crear_panel_consultas()
        self.crear_panel_resultados()
    
    def crear_panel_consultas(self):
        frame_consultas = ctk.CTkScrollableFrame(self.frame_principal, width=450)
        frame_consultas.pack(side="left", fill="y", padx=10, pady=10)
        
        ctk.CTkLabel(
            frame_consultas,
            text="📋 CONSULTAS DISPONIBLES (12)",
            font=("Arial", 18, "bold")
        ).pack(pady=15)
        
        consultas = [
            ("1. Top 5 cámaras más pesadas", self.consulta_mas_pesadas),
            ("2. Top 10 cámaras con mejor zoom", self.consulta_mejor_zoom),
            ("3. Precio promedio por marca", self.consulta_precio_por_marca),
            ("4. Top 10 más económicas", self.consulta_mas_economicas),
            ("5. Mejor relación peso/zoom", self.consulta_relacion_peso_zoom),
            ("6. Distribución de almacenamiento (gráfico)", self.consulta_almacenamiento),
            ("7. Mejor enfoque macro", self.consulta_mejor_macro),
            ("8. Marcas más pesadas", self.consulta_marcas_pesadas),
            ("9. Ideales para viaje", self.consulta_viaje),
            ("10. Estadísticas generales", self.consulta_estadisticas),
            ("11. Correlación peso-precio (gráfico)", self.consulta_correlacion),
            ("12. Cámaras profesionales", self.consulta_profesionales)
        ]
        
        for texto, comando in consultas:
            btn = ctk.CTkButton(
                frame_consultas,
                text=texto,
                command=comando,
                height=45,
                font=("Arial", 13),
                fg_color="#1565C0"
            )
            btn.pack(pady=5, padx=10, fill="x")
        
        ctk.CTkButton(
            frame_consultas,
            text="📥 EXPORTAR RESULTADOS A CSV",
            command=self.exportar_resultados,
            height=45,
            font=("Arial", 13, "bold"),
            fg_color="#F57C00"
        ).pack(pady=10, padx=10, fill="x")
        
        ctk.CTkButton(
            frame_consultas,
            text="🚪 SALIR",
            command=self.quit,
            height=45,
            font=("Arial", 13, "bold"),
            fg_color="#D32F2F"
        ).pack(pady=5, padx=10, fill="x")
    
    def crear_panel_resultados(self):
        
        self.frame_resultados = ctk.CTkFrame(self.frame_principal)
        self.frame_resultados.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        self.label_titulo_resultados = ctk.CTkLabel(
            self.frame_resultados,
            text="RESULTADOS",
            font=("Arial", 20, "bold")
        )
        self.label_titulo_resultados.pack(pady=10)
        
        self.frame_tabla = ctk.CTkFrame(self.frame_resultados)
        self.frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.frame_grafico = ctk.CTkFrame(self.frame_resultados)
    
    def limpiar_resultados(self):
        for widget in self.frame_tabla.winfo_children():
            widget.destroy()
        self.frame_grafico.pack_forget()
        self.frame_tabla.pack(fill="both", expand=True)
    
    def mostrar_tabla(self, df, titulo):
        self.limpiar_resultados()
        self.label_titulo_resultados.configure(text=titulo)
        self.df_actual = df
        
        if df.empty:
            ctk.CTkLabel(
                self.frame_tabla,
                text="No se encontraron resultados",
                font=("Arial", 14)
            ).pack(pady=50)
            return
        
        from tkinter import ttk
        tree = ttk.Treeview(self.frame_tabla)
        
        vsb = ttk.Scrollbar(self.frame_tabla, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(self.frame_tabla, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        columnas = list(df.columns)
        tree["columns"] = columnas
        tree["show"] = "headings"
        
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=120, minwidth=80)
        
        for _, row in df.iterrows():
            valores = [str(row[col]) for col in columnas]
            tree.insert("", "end", values=valores)
        
        tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
    
    def mostrar_grafico(self, figura, titulo):
        self.limpiar_resultados()
        self.label_titulo_resultados.configure(text=titulo)
        
        self.frame_tabla.pack_forget()
        self.frame_grafico.pack(fill="both", expand=True)
        
        for widget in self.frame_grafico.winfo_children():
            widget.destroy()
        
        canvas = FigureCanvasTkAgg(figura, master=self.frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
        self.df_actual = None
    
    def consulta_mas_pesadas(self):
        resultado = self.df_camaras.nlargest(5, "Weight (inc. batteries)")[["Model", "Weight (inc. batteries)", "Price", "Marca"]]
        resultado.columns = ["Modelo", "Peso (g)", "Precio (USD)", "Marca"]
        self.mostrar_tabla(resultado, "🏋️ TOP 5 CÁMARAS MÁS PESADAS")
    
    def consulta_mejor_zoom(self):
        resultado = self.df_camaras.nlargest(10, "Zoom tele (T)")[["Model", "Zoom tele (T)", "Price", "Marca"]]
        resultado.columns = ["Modelo", "Zoom óptico", "Precio (USD)", "Marca"]
        self.mostrar_tabla(resultado, "🔍 TOP 10 CÁMARAS CON MEJOR ZOOM")
    
    def consulta_precio_por_marca(self):
        resultado = self.df_camaras.groupby("Marca")["Price"].mean().round(2).sort_values(ascending=False).reset_index()
        resultado.columns = ["Marca", "Precio Promedio (USD)"]
        self.mostrar_tabla(resultado, "💰 PRECIO PROMEDIO POR MARCA")
    
    def consulta_mas_economicas(self):
        resultado = self.df_camaras.nsmallest(10, "Price")[["Model", "Price", "Zoom tele (T)", "Marca"]]
        resultado.columns = ["Modelo", "Precio (USD)", "Zoom", "Marca"]
        self.mostrar_tabla(resultado, "💵 TOP 10 CÁMARAS MÁS ECONÓMICAS")
    
    def consulta_relacion_peso_zoom(self):
        self.df_camaras["Relacion"] = self.df_camaras["Weight (inc. batteries)"] / (self.df_camaras["Zoom tele (T)"] + 1)
        resultado = self.df_camaras.nsmallest(10, "Relacion")[["Model", "Weight (inc. batteries)", "Zoom tele (T)", "Relacion", "Price"]]
        resultado.columns = ["Modelo", "Peso (g)", "Zoom", "Relación P/Z", "Precio (USD)"]
        resultado["Relación P/Z"] = resultado["Relación P/Z"].round(2)
        self.mostrar_tabla(resultado, "⚖️ MEJOR RELACIÓN PESO/ZOOM")
    
    def consulta_almacenamiento(self):
        almacenamiento_counts = self.df_camaras["Storage included"].value_counts().head(15)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        almacenamiento_counts.plot(kind="bar", ax=ax, color="skyblue")
        ax.set_title("Distribución de Almacenamiento Incluido", fontsize=14, fontweight="bold")
        ax.set_xlabel("Almacenamiento (MB)", fontsize=12)
        ax.set_ylabel("Cantidad de modelos", fontsize=12)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.grid(True, alpha=0.3)
        
        self.mostrar_grafico(fig, "💾 DISTRIBUCIÓN DE ALMACENAMIENTO")
    
    def consulta_mejor_macro(self):
        macro_filtro = self.df_camaras[self.df_camaras["Macro focus range"] > 20]
        resultado = macro_filtro.nlargest(10, "Macro focus range")[["Model", "Macro focus range", "Price", "Marca"]]
        resultado.columns = ["Modelo", "Enfoque Macro (mm)", "Precio (USD)", "Marca"]
        self.mostrar_tabla(resultado, "🔬 MEJOR ENFOQUE MACRO (>20mm)")
    
    def consulta_marcas_pesadas(self):
        resultado = self.df_camaras.groupby("Marca")["Weight (inc. batteries)"].mean().round(2).nlargest(10).reset_index()
        resultado.columns = ["Marca", "Peso Promedio (g)"]
        self.mostrar_tabla(resultado, "🏋️ MARCAS CON MAYOR PESO PROMEDIO")
    
    def consulta_viaje(self):
        viaje = self.df_camaras[
            (self.df_camaras["Weight (inc. batteries)"] < 250) & 
            (self.df_camaras["Zoom tele (T)"] > 100)
        ]
        
        if viaje.empty:
            viaje = self.df_camaras.nsmallest(10, "Weight (inc. batteries)")
        
        resultado = viaje.nlargest(10, "Zoom tele (T)")[["Model", "Weight (inc. batteries)", "Zoom tele (T)", "Price", "Marca"]]
        resultado.columns = ["Modelo", "Peso (g)", "Zoom", "Precio (USD)", "Marca"]
        self.mostrar_tabla(resultado, "✈️ CÁMARAS IDEALES PARA VIAJE")
    
    def consulta_estadisticas(self):
        stats = pd.DataFrame({
            "Métrica": [
                "Total de modelos", "Precio promedio", "Peso promedio", 
                "Zoom promedio", "Precio máximo", "Precio mínimo",
                "Cámara más cara", "Cámara más ligera"
            ],
            "Valor": [
                len(self.df_camaras),
                f"${self.df_camaras['Price'].mean():.2f}",
                f"{self.df_camaras['Weight (inc. batteries)'].mean():.1f} g",
                f"{self.df_camaras['Zoom tele (T)'].mean():.1f}x",
                f"${self.df_camaras['Price'].max():.2f}",
                f"${self.df_camaras['Price'].min():.2f}",
                self.df_camaras.loc[self.df_camaras['Price'].idxmax(), 'Model'],
                self.df_camaras.loc[self.df_camaras['Weight (inc. batteries)'].idxmin(), 'Model']
            ]
        })
        self.mostrar_tabla(stats, "📈 ESTADÍSTICAS GENERALES")
    
    def consulta_correlacion(self):
        correlacion = self.df_camaras["Weight (inc. batteries)"].corr(self.df_camaras["Price"])
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.scatter(self.df_camaras["Weight (inc. batteries)"], self.df_camaras["Price"], 
                  alpha=0.6, c="blue", s=50)
        
        coefs = np.polyfit(self.df_camaras["Weight (inc. batteries)"], self.df_camaras["Price"], 1)
        tendencia = np.poly1d(coefs)
        
        x_ordenado = np.sort(self.df_camaras["Weight (inc. batteries)"])
        ax.plot(x_ordenado, tendencia(x_ordenado), "r--", linewidth=2, 
               label=f"Tendencia (r={correlacion:.3f})")
        
        ax.set_xlabel("Peso (gramos)", fontsize=12)
        ax.set_ylabel("Precio (USD)", fontsize=12)
        ax.set_title(f"Correlación Peso vs Precio: {correlacion:.3f}", fontsize=14, fontweight="bold")
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        self.mostrar_grafico(fig, "📊 CORRELACIÓN PESO VS PRECIO")
    
    def consulta_profesionales(self):
        profesionales = self.df_camaras[
            (self.df_camaras["Zoom tele (T)"] == 0) & 
            (self.df_camaras["Weight (inc. batteries)"] > 500)
        ]
        
        if profesionales.empty:
            profesionales = self.df_camaras.nlargest(10, "Weight (inc. batteries)")
        
        resultado = profesionales[["Model", "Weight (inc. batteries)", "Price", "Marca"]]
        resultado.columns = ["Modelo", "Peso (g)", "Precio (USD)", "Marca"]
        self.mostrar_tabla(resultado, "🎯 CÁMARAS PROFESIONALES (DSLR/SLR)")
    
    def exportar_resultados(self):
        if self.df_actual is not None and not self.df_actual.empty:
            archivo = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
            )
            if archivo:
                self.df_actual.to_csv(archivo, index=False, encoding="utf-8-sig")
                messagebox.showinfo("Éxito", f"✅ Archivo guardado:\n{archivo}")
        else:
            messagebox.showwarning("Sin datos", "Primero ejecute una consulta")

if __name__ == "__main__":
    print("="*50)
    print("INICIANDO SISTEMA DE ANÁLISIS DE CÁMARAS")
    print("="*50)
    
    app = AppAnalisisCamaras()
    app.mainloop()
    
    print("\n" + "="*50)
    print("SISTEMA CERRADO")
    print("="*50)