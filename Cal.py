import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Colorful Calculator")
root.configure(bg="#2c3e50")  # Background color

# Entry widget
entry = tk.Entry(root, width=20, font=('Arial', 20, 'bold'), borderwidth=5, relief="ridge", bg="#ecf0f1", fg="black", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button style helper
def create_button(text, row, col, bg_color, fg_color="white", action=None):
    if action is None:
        action = lambda x=text: click(x)
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 16, 'bold'),
              bg=bg_color, fg=fg_color, activebackground="#7f8c8d",
              command=action, relief="raised", bd=3).grid(row=row, column=col, padx=5, pady=5)

# Buttons
create_button('7', 1, 0, "#3498db")
create_button('8', 1, 1, "#3498db")
create_button('9', 1, 2, "#3498db")
create_button('/', 1, 3, "#e67e22")

create_button('4', 2, 0, "#3498db")
create_button('5', 2, 1, "#3498db")
create_button('6', 2, 2, "#3498db")
create_button('*', 2, 3, "#e67e22")

create_button('1', 3, 0, "#3498db")
create_button('2', 3, 1, "#3498db")
create_button('3', 3, 2, "#3498db")
create_button('-', 3, 3, "#e67e22")

create_button('0', 4, 0, "#3498db")
create_button('.', 4, 1, "#9b59b6")
create_button('+', 4, 2, "#e67e22")
create_button('=', 4, 3, "#27ae60", action=calculate)

# Clear button
create_button('C', 5, 0, "#c0392b", action=clear)
tk.Label(root, text="", bg="#2c3e50").grid(row=5, column=1)  # empty space

root.mainloop()
