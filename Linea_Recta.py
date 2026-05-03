import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def graficar():
    try:
        m = float(entry_m.get())
        b = float(entry_b.get())

        x = np.linspace(-10, 10, 100)
        y = m * x + b

        plt.figure()
        plt.plot(x, y, label=f"f(x) = {m}x + {b}")
        plt.title("Gráfica de función lineal")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.legend()
        plt.grid()

        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos")

ventana = ctk.CTk()
ventana.title("Funciones lineales")
ventana.geometry("350x250")

titulo = ctk.CTkLabel(ventana, text="f(x) = mx + b", font=("Arial", 20))
titulo.pack(pady=10)

label_m = ctk.CTkLabel(ventana, text="Pendiente (m):")
label_m.pack()

entry_m = ctk.CTkEntry(ventana)
entry_m.pack(pady=5)

label_b = ctk.CTkLabel(ventana, text="Término independiente (b):")
label_b.pack()

entry_b = ctk.CTkEntry(ventana)
entry_b.pack(pady=5)

btn_graficar = ctk.CTkButton(ventana, text="Graficar", command=graficar)
btn_graficar.pack(pady=15)

ventana.mainloop()