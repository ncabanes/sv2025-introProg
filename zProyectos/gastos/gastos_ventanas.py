import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

class GestorGastos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Gastos")
        self.root.geometry("700x450")
        self.root.config(padx=10, pady=10)

        # --- 1. Formulario para añadir gastos ---
        frame_form = tk.Frame(self.root)
        frame_form.pack(fill="x", pady=(0, 10))

        tk.Label(frame_form, text="Descripción:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_desc = tk.Entry(frame_form, width=20)
        self.entry_desc.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Fecha (AAAA-MM-DD):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_fecha = tk.Entry(frame_form, width=12)
        self.entry_fecha.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Importe:").grid(row=0, column=4, padx=5, pady=5)
        self.entry_importe = tk.Entry(frame_form, width=10)
        self.entry_importe.grid(row=0, column=5, padx=5, pady=5)

        btn_add = tk.Button(frame_form, text="Añadir", command=self.on_add_clicked)
        btn_add.grid(row=0, column=6, padx=10, pady=5)

        # --- 2. Tabla de gastos ---
        columnas = ("descripcion", "fecha", "importe")
        self.tree = ttk.Treeview(self.root, columns=columnas, show="headings")

        self.tree.heading("descripcion", text="Descripción")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("importe", text="Importe")

        self.tree.column("descripcion", width=250)
        self.tree.column("fecha", width=120, anchor="center")
        self.tree.column("importe", width=100, anchor="e")

        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        # Doble clic para editar
        self.tree.bind("<Double-1>", self.on_edit_requested)

        # --- 3. Panel inferior ---
        frame_bottom = tk.Frame(self.root)
        frame_bottom.pack(fill="x", pady=(10, 0))

        self.lbl_total = tk.Label(frame_bottom, text="Total de gastos: 0", font=("Arial", 11, "bold"))
        self.lbl_total.pack(side="left")

        btn_grafica = tk.Button(frame_bottom, text="Gráfica por Año", command=self.on_plot_year)
        btn_grafica.pack(side="right", padx=5)

        btn_search = tk.Button(frame_bottom, text="Buscar", command=self.on_search_clicked)
        btn_search.pack(side="right", padx=5)

        btn_delete = tk.Button(frame_bottom, text="Borrar Seleccionado", command=self.on_delete_clicked)
        btn_delete.pack(side="right", padx=5)

        # --- 4. Cargar datos ---
        self.cargar_datos()
        self.actualizar_total()

    # ---------------------------------------------------------
    # CARGA Y GUARDADO
    # ---------------------------------------------------------

    def cargar_datos(self):
        if os.path.exists("gastos.txt"):
            with open("gastos.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    if "¬" in linea:
                        desc, fecha, importe = linea.strip().split("¬")
                        self.tree.insert("", tk.END, values=(desc, fecha, importe))

    def guardar_datos(self):
        with open("gastos.txt", "w", encoding="utf-8") as f:
            for item in self.tree.get_children():
                valores = self.tree.item(item, "values")
                f.write(f"{valores[0]}¬{valores[1]}¬{valores[2]}\n")

    # ---------------------------------------------------------
    # FUNCIONES PRINCIPALES
    # ---------------------------------------------------------

    def actualizar_total(self):
        total = 0
        for item in self.tree.get_children():
            valores = self.tree.item(item, "values")
            try:
                total += float(valores[2])
            except:
                pass
        self.lbl_total.config(text=f"Total de gastos: {total:.2f}")

    def on_add_clicked(self):
        desc = self.entry_desc.get()
        fecha = self.entry_fecha.get()
        importe_str = self.entry_importe.get()

        try:
            importe_str = importe_str.replace(",", ".")
            float(importe_str)
        except ValueError:
            messagebox.showerror("Error", "El importe debe ser un número.")
            return

        if desc and fecha and importe_str:
            self.tree.insert("", tk.END, values=(desc, fecha, importe_str))
            self.actualizar_total()
            self.entry_desc.delete(0, tk.END)
            self.entry_fecha.delete(0, tk.END)
            self.entry_importe.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Rellena todos los campos.")

    def on_delete_clicked(self):
        seleccionados = self.tree.selection()
        if seleccionados:
            for item in seleccionados:
                self.tree.delete(item)
            self.actualizar_total()

    # ---------------------------------------------------------
    # EDITAR GASTO
    # ---------------------------------------------------------

    def on_edit_requested(self, event):
        seleccion = self.tree.selection()
        if not seleccion:
            return

        item = seleccion[0]
        desc, fecha, importe = self.tree.item(item, "values")

        win = tk.Toplevel(self.root)
        win.title("Editar gasto")
        win.geometry("300x200")
        win.grab_set()

        tk.Label(win, text="Descripción:").pack()
        entry_desc = tk.Entry(win)
        entry_desc.pack()
        entry_desc.insert(0, desc)

        tk.Label(win, text="Fecha:").pack()
        entry_fecha = tk.Entry(win)
        entry_fecha.pack()
        entry_fecha.insert(0, fecha)

        tk.Label(win, text="Importe:").pack()
        entry_importe = tk.Entry(win)
        entry_importe.pack()
        entry_importe.insert(0, importe)

        def guardar_cambios():
            nueva_desc = entry_desc.get()
            nueva_fecha = entry_fecha.get()
            nuevo_importe = entry_importe.get()

            try:
                float(nuevo_importe.replace(",", "."))
            except ValueError:
                messagebox.showerror("Error", "El importe debe ser numérico.")
                return

            self.tree.item(item, values=(nueva_desc, nueva_fecha, nuevo_importe))
            self.actualizar_total()
            win.destroy()

        tk.Button(win, text="Guardar", command=guardar_cambios).pack(pady=10)

    # ---------------------------------------------------------
    # BUSCAR GASTOS
    # ---------------------------------------------------------

    def on_search_clicked(self):
        win = tk.Toplevel(self.root)
        win.title("Buscar gastos")
        win.geometry("350x300")
        win.grab_set()

        tk.Label(win, text="Texto a buscar:").pack(pady=5)
        entry_buscar = tk.Entry(win, width=30)
        entry_buscar.pack(pady=5)

        lista = tk.Listbox(win)
        lista.pack(fill="both", expand=True, pady=10)

        def ejecutar_busqueda():
            texto = entry_buscar.get().lower().strip()
            lista.delete(0, tk.END)

            if not texto:
                return

            for item in self.tree.get_children():
                valores = self.tree.item(item, "values")
                linea = " | ".join(valores)

                if texto in linea.lower():
                    lista.insert(tk.END, linea)

        tk.Button(win, text="Buscar", command=ejecutar_busqueda).pack(pady=5)

    # ---------------------------------------------------------
    # GRÁFICA ANUAL (Canvas)
    # ---------------------------------------------------------

    def on_plot_year(self):
        win = tk.Toplevel(self.root)
        win.title("Seleccionar año")
        win.geometry("250x120")
        win.grab_set()

        tk.Label(win, text="Introduce un año (AAAA):").pack(pady=5)
        entry_year = tk.Entry(win, width=10)
        entry_year.pack(pady=5)

        def generar():
            year = entry_year.get().strip()
            if not (year.isdigit() and len(year) == 4):
                messagebox.showerror("Error", "Introduce un año válido.")
                return
            win.destroy()
            self.generar_grafica_canvas(year)

        tk.Button(win, text="Generar gráfica", command=generar).pack(pady=10)

    def generar_grafica_canvas(self, year):
        meses = [0] * 12

        for item in self.tree.get_children():
            desc, fecha, importe = self.tree.item(item, "values")
            if fecha.startswith(year):
                try:
                    mes = int(fecha[5:7])
                    valor = float(importe.replace(",", "."))
                    meses[mes - 1] += valor
                except:
                    pass

        win = tk.Toplevel(self.root)
        win.title(f"Gastos por mes en {year}")
        win.geometry("800x400")

        canvas = tk.Canvas(win, bg="white")
        canvas.pack(fill="both", expand=True)

        margen = 50
        ancho = 800
        alto = 400
        base_y = alto - margen
        max_valor = max(meses) if max(meses) > 0 else 1

        canvas.create_line(margen, margen, margen, base_y, width=2)
        canvas.create_line(margen, base_y, ancho - margen, base_y, width=2)

        nombres_meses = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
        espacio = (ancho - 2*margen) / 12

        for i, valor in enumerate(meses):
            x1 = margen + i * espacio + 10
            x2 = margen + (i+1) * espacio - 10

            altura = (valor / max_valor) * (base_y - margen)
            y1 = base_y - altura

            canvas.create_rectangle(x1, y1, x2, base_y, fill="skyblue")
            canvas.create_text((x1+x2)//2, base_y + 15, text=nombres_meses[i])

            if valor > 0:
                canvas.create_text((x1+x2)//2, y1 - 10, text=f"{valor:.2f}")

        canvas.create_text(margen - 20, margen, text=f"{max_valor:.2f}")

# ---------------------------------------------------------
# BLOQUE PRINCIPAL
# ---------------------------------------------------------

def al_cerrar_ventana():
    app.guardar_datos()
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorGastos(root)
    root.protocol("WM_DELETE_WINDOW", al_cerrar_ventana)
    root.mainloop()
