import tkinter as tk
from tkinter import messagebox

def calcular_suma():
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero positivo")
        entry_n.delete(0, tk.END)
        return

    numeros = list(range(1, n + 1))
    suma = sum(numeros)

    secuencia.set("Secuencia: " + " + ".join(map(str, numeros)))
    resultado.set(f"Suma total: {suma}")

ventana = tk.Tk()
ventana.title("Suma de los primeros n números")

secuencia = tk.StringVar()
resultado = tk.StringVar()

tk.Label(ventana, text="Ingrese un número positivo n:").pack()

entry_n = tk.Entry(ventana)
entry_n.pack()

tk.Button(ventana, text="Calcular", command=calcular_suma).pack()

tk.Label(ventana, textvariable=secuencia, fg="blue").pack()
tk.Label(ventana, textvariable=resultado, fg="green").pack()

ventana.mainloop()