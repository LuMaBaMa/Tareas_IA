import tkinter as tk
from tkinter import messagebox

visitantes = []
total_recaudado = 0

def calcular_total(edad, juegos):
    precio_base = juegos * 50

    if edad < 10:
        descuento = precio_base * 0.25
    elif edad <= 17:
        descuento = precio_base * 0.10
    else:
        descuento = 0

    total = precio_base - descuento
    return precio_base, descuento, total

def registrar_visitante():
    global total_recaudado

    nombre = entry_nombre.get()

    try:
        edad = int(entry_edad.get())
        juegos = int(entry_juegos.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese datos válidos")
        return

    precio_base, descuento, total = calcular_total(edad, juegos)

    visitante = {
        "nombre": nombre,
        "edad": edad,
        "juegos": juegos,
        "total": total
    }

    visitantes.append(visitante)
    total_recaudado += total

    resultado.set(f"{nombre} debe pagar: {total:.2f} soles")

    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_juegos.delete(0, tk.END)

def mostrar_historial():
    ventana_historial = tk.Toplevel(ventana)
    ventana_historial.title("Historial de visitantes")

    texto = tk.Text(ventana_historial, width=50, height=15)
    texto.pack()

    if not visitantes:
        texto.insert(tk.END, "No hay visitantes registrados\n")
    else:
        for v in visitantes:
            texto.insert(tk.END,
                f"Nombre: {v['nombre']}\n"
                f"Edad: {v['edad']}\n"
                f"Juegos usados: {v['juegos']}\n"
                f"Total pagado: {v['total']}\n"
                "-----------------------------\n"
            )

def mostrar_total():
    messagebox.showinfo("Total recaudado", f"Total: {total_recaudado:.2f} soles")

ventana = tk.Tk()
ventana.title("Registro de Visitantes - Parque")

resultado = tk.StringVar()

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=1, column=0)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)

tk.Label(ventana, text="Cantidad de juegos:").grid(row=2, column=0)
entry_juegos = tk.Entry(ventana)
entry_juegos.grid(row=2, column=1)

tk.Button(ventana, text="Registrar", command=registrar_visitante).grid(row=3, column=0, columnspan=2)

tk.Label(ventana, textvariable=resultado, fg="blue").grid(row=4, column=0, columnspan=2)

tk.Button(ventana, text="Mostrar historial", command=mostrar_historial).grid(row=5, column=0, columnspan=2)

tk.Button(ventana, text="Total recaudado", command=mostrar_total).grid(row=6, column=0, columnspan=2)

ventana.mainloop()