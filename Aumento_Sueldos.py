import tkinter as tk
from tkinter import messagebox

trabajadores = []

def calcular_aumento(sueldo):
    if sueldo < 4000:
        return sueldo * 0.15
    elif sueldo <= 7000:
        return sueldo * 0.10
    else:
        return sueldo * 0.08

def registrar_trabajador():
    nombre_val = nombre.get()
    try:
        sueldo_val = float(sueldo.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese un sueldo válido")
        return

    aumento = calcular_aumento(sueldo_val)
    nuevo_sueldo = sueldo_val + aumento

    trabajador = {
        "nombre": nombre_val,
        "sueldo": sueldo_val,
        "aumento": aumento,
        "nuevo_sueldo": nuevo_sueldo
    }

    trabajadores.append(trabajador)

    resultado.set(f"Nuevo sueldo de {nombre_val}: {nuevo_sueldo:.2f}")

    nombre.delete(0, tk.END)
    sueldo.delete(0, tk.END)

def mostrar_historial():
    ventana_historial = tk.Toplevel(ventana)
    ventana_historial.title("Historial de trabajadores")

    texto = tk.Text(ventana_historial, width=50, height=15)
    texto.pack()

    if not trabajadores:
        texto.insert(tk.END, "No hay trabajadores registrados.\n")
    else:
        for t in trabajadores:
            texto.insert(tk.END,
                f"Nombre: {t['nombre']}\n"
                f"Sueldo original: {t['sueldo']}\n"
                f"Aumento: {t['aumento']}\n"
                f"Nuevo sueldo: {t['nuevo_sueldo']}\n"
                "-----------------------------\n"
            )

ventana = tk.Tk()
ventana.title("Registro de Trabajadores")

resultado = tk.StringVar()

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
nombre = tk.Entry(ventana)
nombre.grid(row=0, column=1)

tk.Label(ventana, text="Sueldo básico:").grid(row=1, column=0)
sueldo = tk.Entry(ventana)
sueldo.grid(row=1, column=1)

tk.Button(ventana, text="Registrar", command=registrar_trabajador).grid(row=2, column=0, columnspan=2)

tk.Label(ventana, textvariable=resultado, fg="blue").grid(row=3, column=0, columnspan=2)

tk.Button(ventana, text="Mostrar historial", command=mostrar_historial).grid(row=4, column=0, columnspan=2)

ventana.mainloop()