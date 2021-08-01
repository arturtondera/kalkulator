import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
number1 = int(input("Podaj składnik 1.:"))
number2 = int(input("Podaj składnik 2.:"))
product = None
if operation == '1':
    product = (number1 + number2)
    logging.info("Dodaję", number1, "do", number2)
elif operation == '2':
    product = (number1 - number2)
    logging.info('Odejmuję', number2, "od", number1)
elif operation == '3':
    product = (number1 * number2)
    logging.info("Mnożę", number1, "przez", number2)
elif operation == '4':
    product = (number1 // number2)
    logging.info("Dzielę", number1, "przez", number2)
print("Wynik działania to:", product)
