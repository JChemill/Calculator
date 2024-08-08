import tkinter as tk
import math

''' ROOT AND FRAMES '''

root = tk.Tk()
root.title('Calculator')
root.config(bg='#282c35')

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_inputbg = tk.Frame(root, bg='#3E153D', width=34)
frame_inputbg.grid(row=0, column=0, sticky='nsew')

frame_border = tk.Frame(frame_inputbg, bg='#FCD0F9', width=30)
frame_border.grid(row=0, column=0, sticky='nsew', pady=20, padx=20)

frame_cent_buttons = tk.Frame(root, bg='#FCB0E0')
frame_cent_buttons.grid(row=1, column=0, sticky='nsew')
frame_cent_buttons.grid_columnconfigure(0, weight=0)
frame_cent_buttons.grid_rowconfigure(0, weight=1)

frame_buttons = tk.Frame(frame_cent_buttons, bg='#FCB0E0')
frame_buttons.grid(row=0, column=0, sticky='nsew', padx=15, pady=15)
frame_buttons.grid_columnconfigure(0, weight=1)

''' CREATE METHODS '''


def button_click(value):
    if value != '=':
        current = user_input.get()
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, current + str(value))
    else:
        evaluate()


def clear_entry():
    user_input.delete(0, tk.END)


def backspace():
    current = user_input.get()
    user_input.delete(0, tk.END)
    user_input.insert(tk.END, current[:-1])


def evaluate():
    try:
        expression = user_input.get()
        result = eval(expression)
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, str(result))
    except Exception as e:
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, 'Error')


def square():
    number = user_input.get()
    try:
        result = float(number) * float(number)
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, str(result))
    except Exception as e:
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, 'Error')


def square_root():
    number = user_input.get()
    try:
        result = math.sqrt(float(number))
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, str(result))
    except Exception as e:
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, 'Error')


def percentage():
    expression = user_input.get()
    try:
        a, b = expression.split('*')
        a, b = float(a), float(b)
        result = a * b / 100
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, str(result))
    except Exception as e:
        user_input.delete(0, tk.END)
        user_input.insert(tk.END, 'Error')


''' CREATE BUTTONS '''

user_input = tk.Entry(frame_border,
                      bg='#8B73BC',
                      fg='#3B0756',
                      bd=4,
                      width=34,
                      font=('Courier Prime', 19, 'bold'),
                      justify=tk.RIGHT)
user_input.grid(row=0, columnspan=4, ipady=20, sticky='nsew', pady=7, padx=7)

tk.Button(frame_buttons,
          bg='#AC1755',
          fg='#3B0756',
          bd=2,
          text='C',
          width=10,
          padx=20,
          pady=20,
          command=clear_entry,
          font=('Courier Prime', 19, 'bold')
          ).grid(row=1, columnspan=2, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AC1755',
          fg='#3B0756',
          bd=2,
          text='⌫',
          width=10,
          padx=20,
          pady=20,
          command=backspace,
          font=('Courier Prime', 19, 'bold')
          ).grid(row=1, columnspan=2, column=2, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#F99BDB',
          fg='#3B0756',
          bd=2,
          text='^2',
          width=5,
          padx=20,
          pady=20,
          command=square,
          font=('Courier Prime', 19, 'bold')
          ).grid(row=2, column=0, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#F99BDB',
          fg='#3B0756',
          bd=2,
          text='√x',
          width=5,
          padx=20,
          pady=20,
          command=square_root,
          font=('Courier Prime', 19, 'bold')
          ).grid(row=2, column=1, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#F99BDB',
          fg='#3B0756',
          bd=2,
          text='%',
          width=5,
          padx=20,
          pady=20,
          command=percentage,
          font=('Courier Prime', 19, 'bold')
          ).grid(row=2, column=2, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#F99BDB',
          fg='#3B0756',
          bd=2,
          text='÷',
          width=5,
          padx=20,
          pady=20,
          command=lambda: button_click('/'),
          font=('Courier Prime', 19, 'bold')
          ).grid(row=2, column=3, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#F99BDB',
          fg='#3B0756',
          bd=2,
          text='+',
          padx=20,
          pady=20,
          command=lambda: button_click('+'),
          font=('Courier Prime', 19, 'bold')
          ).grid(row=5, column=3, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#F99BDB',
          fg='#3B0756',
          bd=2,
          text='-',
          padx=20,
          pady=20,
          command=lambda: button_click('-'),
          font=('Courier Prime', 19, 'bold')
          ).grid(row=4, column=3, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#F99BDB',
          fg='#3B0756',
          bd=2,
          text='*',
          padx=20,
          pady=20,
          command=lambda: button_click('*'),
          font=('Courier Prime', 19, 'bold')
          ).grid(row=3, column=3, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#BB75E8',
          fg='#3B0756',
          bd=2,
          text='=',
          padx=20,
          pady=20,
          command=lambda: button_click('='),
          font=('Courier Prime', 19, 'bold')
          ).grid(row=6, sticky='nsew', columnspan=2, column=2, padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='7',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(7)
          ).grid(row=3, column=0, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='8',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(8)
          ).grid(row=3, column=1, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='9',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(9)
          ).grid(row=3, column=2, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='4',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(4)
          ).grid(row=4, column=0, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='5',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(5)
          ).grid(row=4, column=1, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='6',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(6)
          ).grid(row=4, column=2, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='1',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(1)
          ).grid(row=5, column=0, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='2',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(2)
          ).grid(row=5, column=1, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='3',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(3)
          ).grid(row=5, column=2, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='0',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click(0)
          ).grid(row=6, column=0, sticky='nsew', padx=3, pady=3)

tk.Button(frame_buttons,
          bg='#AE56AA',
          fg='#3B0756',
          bd=2,
          text='.',
          padx=20,
          pady=20,
          font=('Courier Prime', 19, 'bold'),
          command=lambda: button_click('.')
          ).grid(row=6, column=1, sticky='nsew', padx=3, pady=3)


root.mainloop()
