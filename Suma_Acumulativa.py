import tkinter as tk
from tkinter import messagebox

numeros = []
suma_acumulada = 0

def agregar_numero():
    global suma_acumulada
    try:
        numero = int(entry_numero.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero válido")
        entry_numero.delete(0, tk.END)
        return

    if numero == 0:
        mostrar_resultados()
        return

    numeros.append(numero)
    suma_acumulada += numero
    suma_var.set(f"Suma acumulada: {suma_acumulada}")
    entry_numero.delete(0, tk.END)

def mostrar_resultados():
    if not numeros:
        messagebox.showinfo("Resultados", "No se ingresaron números")
        return

    total_numeros = len(numeros)
    suma_total = sum(numeros)

    resultados = (
        f"Números ingresados: {numeros}\n"
        f"Cantidad de números: {total_numeros}\n"
        f"Suma total: {suma_total}"
    )

    messagebox.showinfo("Resultados finales", resultados)

ventana = tk.Tk()
ventana.title("Ingreso continuo de números")

suma_var = tk.StringVar()

tk.Label(ventana, text="Ingrese números enteros (0 para terminar):").pack()
entry_numero = tk.Entry(ventana)
entry_numero.pack()

tk.Button(ventana, text="Agregar número", command=agregar_numero).pack()
tk.Label(ventana, textvariable=suma_var, fg="blue").pack()

ventana.mainloop()