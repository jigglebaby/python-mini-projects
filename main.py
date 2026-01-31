
from random import choice
from utils import add, is_even, c_to_f, roll_die

while True:
  print('\n--- Utility Toolkit ---')
  print('1) Add two numbers')
  print('2) Even or Odd')
  print('3) Celsius to Farenheit')
  print('4) Roll a die')
  print('5) Exit')

  choice = input('Choose: ')

  if choice == '1':
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    print ('Results:', add(a, b))
  elif choice == '2':
    n = int(input('Enter a number: '))
    print('Even' if is_even(n) else 'Odd')
  elif choice == '3':
    c = float(input('Celsius: '))
    print('Farenheight:', c_to_f(c))
  elif choice == '4':
   print('you rolled:', roll_die())
  elif choice == '5':
    print('Bye!')
    break
  else:
    print('Invalid Chocie')
  
