import math

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

# tu jest interface do dodawania i mnożenia
if (operation == "1") or (operation == "3"):
  elements = input("Podaj liczbę elementów działania: ")
  number_of_elements = {}
  for i in range(1, int(elements)+1):
    number_of_elements.setdefault(i, int(input("Podaj liczbę :")))
else:
#  a tu do odejmowania i dzielenia
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

# tu się zaczynają operacje matematyczne:
if operation == '1':
    product = sum(number_of_elements.values())
elif operation == '2':
    product = (number1_int - number2_int)
    print("Odejmuję", number1_int, "od", number2_int)
elif operation == '3':
    product = math.prod(number_of_elements.values())
elif operation == '4':
    product = (number1_int // number2_int)
    print("Dzielę", number1_int, "przez", number2_int)
print("Wynik działania to:", product)
