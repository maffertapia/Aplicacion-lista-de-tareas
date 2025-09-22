import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Label principal
        self.title_label = tk.Label(root, text="Mi Lista de Tareas", font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Entry para nueva tarea
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=1, column=0, padx=10, pady=5, sticky="we")

        # Botón añadir tarea
        self.add_button = tk.Button(root, text="Añadir", command=self.add_task, bg="#90ee90")
        self.add_button.grid(row=1, column=1, pady=5)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Botones de acción
        self.delete_button = tk.Button(root, text="Eliminar", command=self.delete_task, bg="#ff6961")
        self.delete_button.grid(row=3, column=0, pady=5)

        self.complete_button = tk.Button(root, text="Marcar completada", command=self.complete_task, bg="#87ceeb")
        self.complete_button.grid(row=3, column=1, pady=5)

        # Configuración responsive
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)

    def add_task(self):
        """Añadir nueva tarea a la lista"""
        task = self.task_entry.get()
        if task.strip():
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def delete_task(self):
        """Eliminar tarea seleccionada"""
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def complete_task(self):
        """Marcar tarea como completada (tachar texto)"""
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            if not task.startswith("✔ "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, "✔ " + task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()