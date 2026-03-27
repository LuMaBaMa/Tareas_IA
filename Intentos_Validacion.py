import tkinter as tk
from tkinter import messagebox

numeros_ingresados = []
intentos_incorrectos = 0

def validar_rango(numero):
    return 0 < numero < 20

def validar_numero():
    global intentos_incorrectos
    try:
        numero = int(entry_numero.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero válido")
        entry_numero.delete(0, tk.END)
        return

    numeros_ingresados.append(numero)

    if validar_rango(numero):
        resultado.set(f"Número válido: {numero}\nIntentos incorrectos: {intentos_incorrectos}")
        messagebox.showinfo("Correcto", "Número dentro del rango")
        entry_numero.delete(0, tk.END)
    else:
        intentos_incorrectos += 1
        messagebox.showerror("Error", "El número debe estar entre 0 y 20 (sin incluirlos)")
        entry_numero.delete(0, tk.END)

def mostrar_historial():
    ventana_historial = tk.Toplevel(ventana)
    ventana_historial.title("Historial de Intentos")

    texto = tk.Text(ventana_historial, width=40, height=15)
    texto.pack()

    if not numeros_ingresados:
        texto.insert(tk.END, "No hay intentos registrados\n")
    else:
        texto.insert(tk.END, f"Intentos totales: {len(numeros_ingresados)}\n")
        texto.insert(tk.END, f"Intentos incorrectos: {intentos_incorrectos}\n")
        texto.insert(tk.END, "Números ingresados:\n")
        for i, n in enumerate(numeros_ingresados, 1):
            texto.insert(tk.END, f"{i}: {n}\n")

ventana = tk.Tk()
ventana.title("Validación de Números con Historial")

resultado = tk.StringVar()

tk.Label(ventana, text="Ingrese un número entre 0 y 20:").pack()

entry_numero = tk.Entry(ventana)
entry_numero.pack()

tk.Button(ventana, text="Validar", command=validar_numero).pack()
tk.Button(ventana, text="Mostrar historial", command=mostrar_historial).pack()

tk.Label(ventana, textvariable=resultado, fg="blue").pack()

ventana.mainloop()