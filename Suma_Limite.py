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

    numeros.append(numero)
    suma_acumulada += numero
    suma_var.set(f"Suma parcial: {suma_acumulada}")
    entry_numero.delete(0, tk.END)

    if suma_acumulada > 100:
        mostrar_resultados()

def mostrar_resultados():
    total_numeros = len(numeros)
    suma_total = suma_acumulada

    resultados = (
        f"Cantidad de números ingresados: {total_numeros}\n"
        f"Números ingresados: {numeros}\n"
        f"Suma final: {suma_total}"
    )

    messagebox.showinfo("Resultados finales", resultados)

ventana = tk.Tk()
ventana.title("Suma acumulada hasta superar 100")

suma_var = tk.StringVar()

tk.Label(ventana, text="Ingrese números enteros:").pack()
entry_numero = tk.Entry(ventana)
entry_numero.pack()

tk.Button(ventana, text="Agregar número", command=agregar_numero).pack()
tk.Label(ventana, textvariable=suma_var, fg="blue").pack()

ventana.mainloop()