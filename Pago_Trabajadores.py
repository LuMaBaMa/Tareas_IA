import tkinter as tk
from tkinter import messagebox

trabajadores = []

def calcular_pagos(nombre, horas_normales, pago_hora, horas_extras, hijos):
    pago_normal = horas_normales * pago_hora
    pago_extra = horas_extras * (pago_hora * 1.5)
    bonificacion_hijos = hijos * 0.5
    total = pago_normal + pago_extra + bonificacion_hijos
    return pago_normal, pago_extra, bonificacion_hijos, total

def registrar_trabajador():
    nombre = entry_nombre.get()
    try:
        horas_normales = float(entry_horas_normales.get())
        pago_hora = float(entry_pago_hora.get())
        horas_extras = float(entry_horas_extras.get())
        hijos = int(entry_hijos.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos")
        return

    pago_normal, pago_extra, bonificacion_hijos, total = calcular_pagos(
        nombre, horas_normales, pago_hora, horas_extras, hijos
    )

    trabajador = {
        "nombre": nombre,
        "pago_normal": pago_normal,
        "pago_extra": pago_extra,
        "bonificacion_hijos": bonificacion_hijos,
        "total": total
    }

    trabajadores.append(trabajador)

    resultado.set(f"Pago total de {nombre}: {total:.2f}")

    entry_nombre.delete(0, tk.END)
    entry_horas_normales.delete(0, tk.END)
    entry_pago_hora.delete(0, tk.END)
    entry_horas_extras.delete(0, tk.END)
    entry_hijos.delete(0, tk.END)

def mostrar_reporte():
    ventana_reporte = tk.Toplevel(ventana)
    ventana_reporte.title("Reporte de Pagos")

    texto = tk.Text(ventana_reporte, width=60, height=20)
    texto.pack()

    if not trabajadores:
        texto.insert(tk.END, "No hay trabajadores registrados\n")
    else:
        for t in trabajadores:
            texto.insert(tk.END,
                f"Nombre: {t['nombre']}\n"
                f"Pago horas normales: {t['pago_normal']}\n"
                f"Pago horas extras: {t['pago_extra']}\n"
                f"Bonificación hijos: {t['bonificacion_hijos']}\n"
                f"Pago total: {t['total']}\n"
                "-----------------------------\n"
            )

ventana = tk.Tk()
ventana.title("Cálculo de Pago de Trabajadores")

resultado = tk.StringVar()

tk.Label(ventana, text="Nombre del trabajador:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Horas normales trabajadas:").grid(row=1, column=0)
entry_horas_normales = tk.Entry(ventana)
entry_horas_normales.grid(row=1, column=1)

tk.Label(ventana, text="Pago por hora normal:").grid(row=2, column=0)
entry_pago_hora = tk.Entry(ventana)
entry_pago_hora.grid(row=2, column=1)

tk.Label(ventana, text="Horas extras trabajadas:").grid(row=3, column=0)
entry_horas_extras = tk.Entry(ventana)
entry_horas_extras.grid(row=3, column=1)

tk.Label(ventana, text="Número de hijos:").grid(row=4, column=0)
entry_hijos = tk.Entry(ventana)
entry_hijos.grid(row=4, column=1)

tk.Button(ventana, text="Registrar trabajador", command=registrar_trabajador).grid(row=5, column=0, columnspan=2)

tk.Label(ventana, textvariable=resultado, fg="blue").grid(row=6, column=0, columnspan=2)

tk.Button(ventana, text="Mostrar reporte", command=mostrar_reporte).grid(row=7, column=0, columnspan=2)

ventana.mainloop()