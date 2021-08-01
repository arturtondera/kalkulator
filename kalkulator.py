import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
number1_int = None
while isinstance(number1_int, int) is False:
    number1 = input("Podaj składnik 1.:")
    try:
        number1_int = int(number1)
    except ValueError:
        print("To nie jest liczba")
number2_int = None
while isinstance(number2_int, int) is False:
number2 = input("Podaj składnik 2.:")
try:
    number2_int = int(number2)
except ValueError:
    print("To nie jest liczba")
product = None
if operation == '1':
    product = (number1_int + number2_int)
    print("Dodaję", number1_int, "do", number2_int)
elif operation == '2':
    product = (number1_int - number2_int)
    print('Odejmuję', number2_int, "od", number1_int)
elif operation == '3':
    product = (number1_int * number2_int)
    print("Mnożę", number1_int, "przez", number2_int)
elif operation == '4':
    product = (number1_int // number2_int)
    print("Dzielę", number1_int, "przez", number2_int)
print("Wynik działania to:", product)