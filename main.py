#Простейший калькулятор c введёнными двумя числами вещественного типа.
#Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
#Обработать ошибку: “Деление на ноль”
#Ноль использовать в качестве завершения программы (сделать как отдельную операцию).


while True:
    n = input('exit - "0" ')
    if n == '0':
        break


    def kal():
        a = float(input('1 chislo: '))
        b = float(input('2 chiclo: '))
        c = input('+ - * /: ')

        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            try:
                print(a / b)
            except ZeroDivisionError:
                print('Delenie na "0" nevozmoshno!')
        else:
            print('ne verno')


    print(kal())








