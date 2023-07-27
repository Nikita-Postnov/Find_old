import os
import tkinter as tk
from tkinter import filedialog


def search_files():
    search_query = entry_search.get()
    search_path = entry_path.get()
    results.delete(1.0, tk.END)

    for root, dirs, files in os.walk(search_path):
        for file in files:
            if search_query.lower() in file.lower():
                file_path = os.path.join(root, file)
                results.insert(tk.END, file_path + "\n")


def browse_path():
    path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(tk.END, path)


app = tk.Tk()
app.title("Поиск файлов")
app.geometry("400x300")

label_search = tk.Label(app, text="Введите имя файла:")
label_search.pack()

entry_search = tk.Entry(app)
entry_search.pack()

label_path = tk.Label(app, text="Выберите папку для поиска:")
label_path.pack()

entry_path = tk.Entry(app)
entry_path.pack()

browse_button = tk.Button(app, text="Обзор", command=browse_path)
browse_button.pack()

search_button = tk.Button(app, text="Поиск", command=search_files)
search_button.pack()

results = tk.Text(app, wrap=tk.WORD)
results.pack()

app.mainloop()
