import tkinter as tk
from tkinter import messagebox

intentos = 0

def validar_numero():
    global intentos
    intentos += 1

    try:
        numero = int(entry_numero.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero válido")
        entry_numero.delete(0, tk.END)
        return

    if numero < 10:
        resultado.set(f"Número correcto: {numero} | Intentos: {intentos}")
        messagebox.showinfo("Correcto", "Número válido ingresado")
    else:
        messagebox.showerror("Error", "El número debe ser menor que 10")
        entry_numero.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Validación de Número")

resultado = tk.StringVar()

tk.Label(ventana, text="Ingrese un número entero menor que 10:").pack()

entry_numero = tk.Entry(ventana)
entry_numero.pack()

tk.Button(ventana, text="Validar", command=validar_numero).pack()

tk.Label(ventana, textvariable=resultado, fg="blue").pack()

ventana.mainloop()