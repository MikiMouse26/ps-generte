import random
import tkinter as tk
from tkinter import messagebox

# Символы для генерации пароля
a = ['+', '-', '/', '*', '!', '&', '$', '#', '?', '=', '@',
     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z','а','б','в','г','д','е','ё',
     '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def generate_random_word(length=8):
    """Функция для генерации случайного пароля"""
    return ''.join(random.choice(a) for _ in range(length))

def on_generate_click():
    """Функция, вызываемая при нажатии кнопки 'Сгенерировать'"""
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Длина должна быть больше 0.")
        random_word = generate_random_word(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, random_word)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число для длины пароля.")

# Создание главного окна
root = tk.Tk()
root.title("Генератор паролей")
root.geometry("400x200")
root.resizable(False, False)

# Метки и поля ввода
tk.Label(root, text="Длина пароля:", font=("Arial", 12)).pack(pady=10)
entry_length = tk.Entry(root, font=("Arial", 12), justify="center")
entry_length.pack(pady=5)
entry_length.insert(0, "8")

# Поле для отображения пароля
tk.Label(root, text="Сгенерированный пароль:", font=("Arial", 12)).pack(pady=10)
entry_password = tk.Entry(root, font=("Arial", 12), justify="center", state="normal")
entry_password.pack(pady=5)

# Кнопка для генерации
tk.Button(root, text="Сгенерировать", font=("Arial", 12), command=on_generate_click).pack(pady=10)

# Запуск цикла обработки событий
root.mainloop()
