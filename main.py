import random

number = random.randint(0,5)
print('Попробуй угадать число от 1 до 5')
user_number = int(input('Введите число: '))
attemps = 1
while user_number != number and attemps < 3:
  
  print('Не угадал')
  user_number = int(input('Введите число: '))
  attemps += 1
  
if user_number == number:
  print(f'Это верно я загадал число {number} ')
else:
  print('Не угадал')
  