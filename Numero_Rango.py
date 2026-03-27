import tkinter as tk
from tkinter import messagebox

intentos = 0

def validar_rango(numero):
    return 0 < numero < 20

def validar_numero():
    global intentos
    intentos += 1

    try:
        numero = int(entry_numero.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero válido")
        entry_numero.delete(0, tk.END)
        return

    if validar_rango(numero):
        resultado.set(f"Número válido: {numero} | Intentos: {intentos}")
        messagebox.showinfo("Correcto", "Número dentro del rango")
    else:
        messagebox.showerror("Error", "El número debe estar entre 0 y 20 (sin incluirlos)")
        entry_numero.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Validación de Rango (0,20)")

resultado = tk.StringVar()

tk.Label(ventana, text="Ingrese un número entre 0 y 20:").pack()

entry_numero = tk.Entry(ventana)
entry_numero.pack()

tk.Button(ventana, text="Validar", command=validar_numero).pack()

tk.Label(ventana, textvariable=resultado, fg="blue").pack()

ventana.mainloop()