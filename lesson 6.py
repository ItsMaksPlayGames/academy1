import tkinter
import inspect
# Tkinter provides classes which allow the display, positioning and
#     control of widgets. Toplevel widgets are Tk and Toplevel. Other
#     widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
#     Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
#     LabelFrame and PanedWindow.
#
#     Properties of the widgets are specified with keyword arguments.
#     Keyword arguments have the same name as the corresponding resource
#     under Tk.
#
#     Widgets are positioned with one of the geometry managers Place, Pack
#     or Grid. These managers can be called with methods place, pack, grid
#     available in every Widget.
#
#     Actions are bound to events by resources (e.g. keyword argument
#     command) or with the method bind.
help(tkinter.Tk)  # Справка о классе Tk
help(tkinter.Label)  # Справка о классе Label
help(tkinter.Button)  # Справка о классе Button
tkinter_attributes = dir(tkinter)
print("Атрибуты библиотеки tkinter:")
for attr in tkinter_attributes:
    print(attr)
print(inspect.ismodule(tkinter))
print(inspect.isclass(tkinter.Label))
print(inspect.isclass(tkinter.Frame))

print(inspect.isfunction(tkinter.Button))
help(tkinter.Tk)  # Пример для класса Tk
help(tkinter.Button)  # Пример для класса Button
print(f"tkinter is function: {inspect.isfunction(tkinter)}")
print(f"tkinter is class: {inspect.isclass(tkinter)}")
print(help(tkinter))
if inspect.isfunction(tkinter.Tk):
    print("Tk - это есть функция")
else:
    print("Tk - это не есть функция")

if inspect.isclass(tkinter.Label):
    print("Label - это есть класс")
else:
    print("Label - это не есть класс")



def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Функція {func.__name__} була викликана {wrapper.call_count} раз(ів)")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper
@count_calls
def call_me():
    print("Виконую функцію")

call_me()
call_me()
call_me()







