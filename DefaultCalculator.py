import tkinter as tk

#Выражение на дисплее (Постоянно меняется)
calculation = ""

#Дисплей над кнопками(Теперь не интерактивен для курсора)
def update_display():
    display_var.set(calculation)


#Ввод кнопок в выражение
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    update_display()


#Кнопка результата "="
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        update_display()
    except:
        calculation = ""
        display_var.set("Error")


#Кнопка очистки "C"
def clear_field():
    global calculation
    calculation = ""
    update_display()


#Параметры (Лучше не трогать ничего кроме цвета)
root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.resizable(False, False)
root.configure(bg="#1E1E1E")


#Оформление
display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Segoe UI", 28),
    justify="right",
    bd=0,
    bg="#252526",
    fg="white",
    readonlybackground="#252526",
)
display.configure(state="readonly")
display.pack(fill="x", padx=15, pady=15, ipady=20)

buttons_frame = tk.Frame(root, bg="#1E1E1E")
buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

for i in range(4):
    buttons_frame.columnconfigure(i, weight=1)

for i in range(6):
    buttons_frame.rowconfigure(i, weight=1)


def create_button(text, row, col, command,
                  bg="#333333", fg="white",
                  colspan=1):

    btn = tk.Button(
        buttons_frame,
        text=text,
        command=command,
        font=("Segoe UI", 18, "bold"),
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        bd=0,
        relief="flat",
        cursor="hand2"
    )

    btn.grid(
        row=row,
        column=col,
        columnspan=colspan,
        sticky="nsew",
        padx=4,
        pady=4
    )


# Строки
# Первая стр.
create_button("C", 0, 0, clear_field, bg="#C0392B")
create_button("(", 0, 1, lambda: add_to_calculation("("))
create_button(")", 0, 2, lambda: add_to_calculation(")"))
create_button("÷", 0, 3, lambda: add_to_calculation("/"), bg="#F39C12")

# Вторая стр.
create_button("7", 1, 0, lambda: add_to_calculation(7))
create_button("8", 1, 1, lambda: add_to_calculation(8))
create_button("9", 1, 2, lambda: add_to_calculation(9))
create_button("×", 1, 3, lambda: add_to_calculation("*"), bg="#F39C12")

# Третья стр.
create_button("4", 2, 0, lambda: add_to_calculation(4))
create_button("5", 2, 1, lambda: add_to_calculation(5))
create_button("6", 2, 2, lambda: add_to_calculation(6))
create_button("-", 2, 3, lambda: add_to_calculation("-"), bg="#F39C12")

# Четвёртая стр.
create_button("1", 3, 0, lambda: add_to_calculation(1))
create_button("2", 3, 1, lambda: add_to_calculation(2))
create_button("3", 3, 2, lambda: add_to_calculation(3))
create_button("+", 3, 3, lambda: add_to_calculation("+"), bg="#F39C12")

# Пятая стр.
create_button("0", 4, 0, lambda: add_to_calculation(0), colspan=2)
create_button(".", 4, 2, lambda: add_to_calculation("."))
create_button("=", 4, 3, evaluate_calculation, bg="#27AE60")

root.mainloop()