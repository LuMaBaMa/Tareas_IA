import tkinter as tk
from tkinter import messagebox

compras = []
total_vendido = 0

def validar_mes(mes):
    meses_validos = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    return mes.lower() in meses_validos

def calcular_descuento(mes, importe):
    mes = mes.lower()
    if mes == "octubre":
        return importe * 0.15
    elif mes == "diciembre":
        return importe * 0.20
    elif mes == "julio":
        return importe * 0.10
    else:
        return 0

def registrar_compra():
    global total_vendido

    nombre = entry_nombre.get()
    mes = entry_mes.get()

    try:
        importe = float(entry_importe.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese un importe válido")
        return

    if not validar_mes(mes):
        messagebox.showerror("Error", "Mes inválido")
        return

    descuento = calcular_descuento(mes, importe)
    total = importe - descuento

    compra = {
        "nombre": nombre,
        "mes": mes,
        "importe": importe,
        "descuento": descuento,
        "total": total
    }

    compras.append(compra)
    total_vendido += total

    resultado.set(f"Total a pagar: {total:.2f}")

    # Limpiar campos
    entry_nombre.delete(0, tk.END)
    entry_mes.delete(0, tk.END)
    entry_importe.delete(0, tk.END)

# Mostrar historial
def mostrar_historial():
    ventana_historial = tk.Toplevel(ventana)
    ventana_historial.title("Historial de compras")

    texto = tk.Text(ventana_historial, width=50, height=15)
    texto.pack()

    if not compras:
        texto.insert(tk.END, "No hay compras registradas\n")
    else:
        for c in compras:
            texto.insert(tk.END,
                f"Cliente: {c['nombre']}\n"
                f"Mes: {c['mes']}\n"
                f"Importe: {c['importe']}\n"
                f"Descuento: {c['descuento']}\n"
                f"Total pagado: {c['total']}\n"
                "-----------------------------\n"
            )

# Mostrar total vendido
def mostrar_total():
    messagebox.showinfo("Total vendido", f"Total del día: {total_vendido:.2f}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Compras")

resultado = tk.StringVar()

# Interfaz
tk.Label(ventana, text="Nombre del cliente:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Mes de la compra:").grid(row=1, column=0)
entry_mes = tk.Entry(ventana)
entry_mes.grid(row=1, column=1)

tk.Label(ventana, text="Importe de compra:").grid(row=2, column=0)
entry_importe = tk.Entry(ventana)
entry_importe.grid(row=2, column=1)

tk.Button(ventana, text="Registrar compra", command=registrar_compra).grid(row=3, column=0, columnspan=2)

tk.Label(ventana, textvariable=resultado, fg="blue").grid(row=4, column=0, columnspan=2)

tk.Button(ventana, text="Mostrar historial", command=mostrar_historial).grid(row=5, column=0, columnspan=2)

tk.Button(ventana, text="Total vendido", command=mostrar_total).grid(row=6, column=0, columnspan=2)

# Ejecutar
ventana.mainloop()