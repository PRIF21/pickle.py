import random

ch1k=random.randint(1,10) #число казино
ch2k=random.randint(1,2) # цвет казино
pop=0 # кол-во попыток
ch1=0 # число  введенное
ch2=0 # цвет введенный
print(ch1k, ch2k)
while pop<5 :
    ch1=int(input('Введите число от 1 до 10 '))
    if ch1>11:
        print('Вы ввели недопустимые данные ')
        break
    ch2=str(input('Введите цвет(красный, черный) '))
   
    pop += 1
    if ch2=='Красный'or ch2=='красный':
        ch2=1
    elif ch2=='Черный'or ch2=='черный':
        ch2=2
    if ch1==ch1k and ch2==ch2k :
        print('Bingo!!!!')
        break
    else:
        print('Введите ещё раз')

else:
    print('удача сегодня не на вашей стороне')
if ch2k == 1:
    ch2k = str('Красный')
elif ch2k == 2:
     ch2k = str('Черный')
print('Верная комбинация: ',ch1k, ch2k)
