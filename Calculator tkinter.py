from tkinter import * #Ткинтер очень хорошая библиотка которая делает графический интерфейс (GUI), схему создания самого примитивного "гуи" пропишу выше.
import math #Библиотка из которой я взял корень и квадрат, подпишу их снизу.

root = Tk()
root.geometry("265x400")
root.title("Калькулятор")
root.config(background="lightblue") #Цвет заднего фона гуишки.

expression = "" #Отвечает за пустоту в поле.

result = StringVar() #Делает поле ввода.
expression_field = Entry(textvariable=result)
expression_field.grid(columnspan=4, ipadx=70) #Поле ввода

def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression = total
    except: 
        result.set("error")
        expression = ""

def converter(): #Кнопка конвертации валюты которая подвязана к значениям в coins.
    actual_coin = list_of_coins.get(list_of_coins.curselection())
    umn = 1
    if actual_coin == "Rub to Dollar":
        umn = 50
    elif actual_coin == "Dollar to Rub":
        umn = 0.02
    elif actual_coin == "Rub to Euro":
        umn = 60
    elif actual_coin == "Euro to Rub":
        umn = 0.015
    global expression
    total = str(eval(expression) * umn)
    result.set(total)
    expression = total

def sqrt_exp(): #Корень берет sqrt (корень) из библиотеки math, и вычисляет значение.
    global expression
    total = str(math.sqrt(eval(expression)))
    result.set(total)
    expression = total

def sqr_exp(): #Квадрат берет число и умножает его на себя.
    global expression
    total = str((eval(expression)) * (eval(expression)))
    result.set(total)
    expression = total
    
def reset(): #Ресет кнопка действует по аналогии пустой клетки, она просто ничего не ставит, тем самым очищает строчку.
    global expression
    total = ""
    result.set(total)
    expression = total

    

button1 = Button(text = "1", height=1, width=7, command=lambda: press_num(1)) #Кнопка с цифрой один, по аналогии другие кнопки ниже тоже с цифрами.
button1.grid(row=2, column=0) #Метод grid() позволяет поместить виджет в определенную ячейку условной сетки или грида.
                              #column: номер столбца, отсчет начинается с нуля.
                              #row: номер строки, отсчет начинается с нуля.

button2 = Button(text = "2", height=1, width=7, command=lambda: press_num(2)) #
button2.grid(row=2, column=1)

button3 = Button(text = "3", height=1, width=7, command=lambda: press_num(3)) #
button3.grid(row=2, column=2)

button4 = Button(text = "4", height=1, width=7, command=lambda: press_num(4)) #
button4.grid(row=3, column=0)

button5 = Button(text = "5", height=1, width=7, command=lambda: press_num(5)) #
button5.grid(row=3, column=1)

button6 = Button(text = "6", height=1, width=7, command=lambda: press_num(6)) #
button6.grid(row=3, column=2)

button7 = Button(text = "7", height=1, width=7, command=lambda: press_num(7)) #
button7.grid(row=4, column=0)

button8 = Button(text = "8", height=1, width=7, command=lambda: press_num(8)) #
button8.grid(row=4, column=1)

button9 = Button(text = "9", height=1, width=7, command=lambda: press_num(9)) #
button9.grid(row=4, column=2)

plus = Button(text = "+", height=1, width=7, command=lambda: press_num("+")) #Отвечает за кнопку + и выполняет его свойства.
plus.grid(row=5, column=0)

button0 = Button(text = "0", height=1, width=7, command=lambda: press_num(0)) #Отвечает за 0 который находиться в цифрах.
button0.grid(row=5, column=1)

minus = Button(text = "-", height=1, width=7, command=lambda: press_num("-")) #Отвечает за кнопку - и выполняет его свойства.
minus.grid(row=5, column=2)

equal = Button(text = "=", height=1, width=7, command=equalpress) #Отвечает за кнопку = и выполняет его свойства.
equal.grid(row=6, column=1)

umn = Button(text = "*", height=1, width=7, command=lambda: press_num("*")) #Отвечает за кнопку * и выполняет его свойства.
umn.grid(row=6, column=2)

dele = Button(text = "/", height=1, width=7, command=lambda: press_num("/")) #Отвечает за кнопку / и выполняет его свойства (тоесть деление).
dele.grid(row=6, column=0)

#Прототип конвертера валют через кнопки, дальше была сделана небольшая табличка coins которая конвертируют валюту, а это просто закоментированно ковычками "".
"""rub_to_dol = Button(text = "RTD", height=1, width=7, command=lambda: converter(0.02))
rub_to_dol.grid(row=7, column=0)

dol_to_rub = Button(text = "DTR", height=1, width=7, command=lambda: converter(50))
dol_to_rub.grid(row=7, column=1)"""

#База coins в которой находяться кликабельные кнопки перевода валюты, их 4.
coins = ["Rub to Dollar", "Dollar to Rub", "Rub to Euro", "Euro to Rub"]
list_of_coins = Listbox(width=15, height=5)
list_of_coins.grid(row=7, column=1)
for coin in coins:
    list_of_coins.insert(0, coin)


convert = Button(text = "Convert", height=1, width=7, command=converter) #Кнопка конвертации валюты.
convert.grid(row=8, column=1)

sqrt = Button(text = "sqrt", height=1, width=7, command=sqrt_exp) #Кнопка корня, которая его выводит.
sqrt.grid(row=9, column=0)

sqr = Button(text = "sqr", height=1, width=7, command=sqr_exp) #Кнопка квадрата, которая его выводит.
sqr.grid(row=9, column=1)

reset = Button(text = "RESET", height=1, width=7, command=reset) #Кнопка которая сбрасывает все значения в выводе, сделана не сложно.
reset.grid(row=9, column=2)

root.mainloop() #Цикличный процесс который держит гуи открытой, благодаря ей он не закрывается сразу и запускается до того момента пока пользователь сам его не закроет.

