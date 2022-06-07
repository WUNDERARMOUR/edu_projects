import string
import random
import re
import bisect
# name=input('kak tebya zovut?')
# print('privet', name)
# a = int(input())
# b = int(input())
# с = int(input())
# print(a + b + с)
# print(9-3/(1/3)+1)# Продолжите код
# Числа b и h можно считывать так:
# b = int(input())
# h = int(input())
# print(b*h/2)
# # Выводите результат через print()
# name=(input())#вставьте текст
# print('Hello, '+name+'!')
# count=0
# count+=2
# print(count)
# count-=2
# print(count)
# count+= 2
# count*=4
# print(count)
# count**=4
# print(count)
# count/=4
# print(count)
# r = int(input())
# y = int(input())
# n = int(input())
# g = r + y
# print((r + g) * n)
# a = int(input())
# b = int(input())
# print(a + b)
# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(math.sqrt(b))
# str='A'
# print(str*100)
# a=float(input())
# b=float(input())
# c=float(input())
# d=float(input())
# res=((a+b+c+d) / 4)
# # print(res)
# n = int(input())
# print ('The next number for the number', n,'is',str(n+1)+'.')
# print ('The previous number for the number', n,'is',str(n-1)+'.')
# print(5!=1*2*3*4*5)
# from math import factorial, pow
#
#
# def calc(data):
#     return pow((factorial(data) / pow(data, 3)), 10)
#
#
# print(calc(10))
# n = int(input())
#
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
#
# print(factorial)
# число, факториал которого нужно вычислить
# num = 10
# # начальное значение факториала
# factorial = 1
#
# # Если num является натуральным, то
# if (num % 1 == 0 and num >= 0):
#     # Вычисляем факториал числа num
#     for i in range(1, num + 1):
#         factorial = i * factorial
#     # Выводим результат на экран
#     print(factorial)


# print(type(None))
# print(type(True))
# print(type(False))
# print(type(1))
# print(type(5.3))
# print(type(5 + 4j))
# print(type([1, 5.3, False, 4]))
# print(type((1, True, 3, 5+4j)))
# print(type(range(5)))
# print(type('Hello'))
# print(type(b'a'))
# print(type(bytearray([1,2,3])))
# print(type(memoryview(bytearray('XYZ', 'utf-8'))))
# print(type({'a', 3, True}) )
# print(type(frozenset({1, 2, 3})) )
# print(type({'a' : 32}))


# print("Addition of two complex numbers : ",(4+3j)+(3-7j))
# print("Subtraction of two complex numbers : ",(4+3j)-(3-7j))
# print("Multiplication of two complex numbers : ",(4+3j)*(3-7j))
# print("Division of two complex numbers : ",(4+3j)/(3-7j))


# a=int(input())
# b=int(input())
# g=float((a**2)+(b**2))
# g=g**(0.5)
# print(g)


# a=int(input())
# a=a%10
# print(a)


# num = int(input())
# sum = 0
# while (num != 0):
#     sum = sum + num % 10
#     num = num // 10
# print(sum)


# shkolniki = int(input())
# yabloki = int(input())
# a = yabloki // shkolniki
# print(a)


# a = int(input())
# b = int(input())
# c = int(input())
# sumpart = ((a+b+c)/2)
# print(math.ceil(sumpart + 0.5))

# a = int(input())
# b = int(input())
# c = int(input())
# a = (math.ceil(a/2))
# b = (math.ceil(b/2))
# c = (math.ceil(c/2))
# sumpart = (a+b+c)
# print(sumpart)


# shkolniki = int(input())
# yabloki = int(input())
# a = yabloki % shkolniki
# print(a)


# num = int(input())
# sum = 0
# while (num != 0):
#     sum = sum + num % 10
#     num = num // 10
# print(sum)

# PIROZHKI
# rub = int(input())
# kop = int(input())
# pirozhki = int(input())
# stoimostrub = rub * pirozhki
# stoimostkop = kop * pirozhki
# if (stoimostkop >= 100):
#     stoimostkop = stoimostkop//100
#     stoimostrub = (math.ceil(stoimostrub + stoimostkop))
#     stoimostkop = (math.ceil(stoimostkop % stoimostrub))
# print(stoimostrub, stoimostkop)


# PIROZHKI RESHENIE
# a = int(input())
# b = int(input())
# n = int(input())
# cost = n * (100 * a + b) узнаем полную цену в копейках
# print(cost // 100, cost % 100) отделяем копейки от рублей


# RASSTOYANIE TURISTOV
# tur1 = int(input())
# tur2 = int(input())
# vrem = int(input())
# rast = (tur1 * vrem) + (tur2 * vrem)
# print(rast)


# TREHZNACHOE
# x = int(input())
# if(x/100 < 10 and x/100 >= 1):
#     print('YES')
# else:
#     print('NO')


# MKAD
# v = int(input())
# t = int(input())
# a = v * t
# n = a // 109
# print(-(109 * n - a))


# считать колво символов LEN
# a=len('ccc22222')
# b=len('bbb22')
#
# print(a>b)
#


# a = int(input())
# a = str(a)
# print(int(a[0]),int(a[1]),int(a[2]))


# print('Python'*100)


# a = int(input())
# b = int(input())
# c = int(input())
# res = (a+b+c)/3
# print(f"{a}+{b}+{c}={a+b+c}")
# print(f"{a}*{b}*{c}={a*b*c}")
# print(f"({a}+{b}+{c})/3=",round(res,3), sep="")


# a, b, c = int(input()), int(input()), int(input())
# print(a, "+", b, "+", c, "=", a + b + c)
# print(a, "*", b, "*", c, "=", a * b * c)
# print("(", a, "+", b, "+", c, ")" "/3"  "=",a * b)


# KOORDINATI TOCHEK
# x1, y1 = map(float,input().split())
# x2, y2 = map(float,input().split())
# res = math.sqrt((x2-x1)**2+(y2-y1)**2)
# print('{:.3f}'.format(res), sep='')


# x = float(input())
# res = x**10
# print('{:.3f}'.format(res))

# a = input('форма оплаты(почасовая\оклад)').lower()
# name=input('ФИО')
# if a=='почасовая':
#     num1=int(input('Введите количство часов'))
#     num2=int(input('Стоимость часа'))
#     print(num1*num2)
# else:
#     num3=int(input('Стаж'))
#     num4=int(input('Ставка'))
#     if num3< 10:
#         print(num3*num4)
#     else:
#         print(num3*num4 *1,5)

#


# name, age = "Simon", 19
# address = "Bangalore, Karnataka, India"
# print("Name:{}\nAge:{}\nAddress:{}".format(name, age, address, sep=""))


# MAX
# num1=int(input())
# num2=int(input())
# if num1 >= num2:
#     print(num1)
# else:
#     print(num2)


# VISOKOSNII ILI NET
# num1=int(input())
# if ((num1 % 4 == 0) and (num1 % 100 != 0)) or (num1 % 400 == 0):
#     print('YES')
# else:
#     print('NO')


# POLOZHTELNOE
# x = int(input())
# if x > 0:
#     print(1)
# elif x == 0:
#     print(0)
# else:
#     print(-1)


# ODINAKOVIE CHISLA
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b and b == c:
#     print(3)
# elif a == b or a == c or b ==c:
#     print(2)
# else:
#     print(0)


# SKOLKO DNEY V MESYACE
# n = int(input())
# if n ==0 or n > 12:
#     print(0)
# elif n == 4 or n == 6 or n == 9 or n == 11:
#     print(30)
# elif n == 2:
#     print(28)
# else:
#     print(31)


# VREMYA GODA
# n = int(input())
# if n == 0 or n > 12:
#     print('NO')
# elif n == 1 or n == 2 or n == 12:
#     print('winter')
# elif n == 3 or n == 4 or n == 5:
#     print('spring')
# elif n == 6 or n == 7 or n == 8:
#     print('summer')
# else:
#     print('autumn')


# # объявление переменных
# name = "Pythonru"
# type_of_site = "Блог"
#
# # заключите переменную в {}, чтобы отобразить ее значение в выводе
# print(f"{name} это {type_of_site}.")
#
#


# # объявление переменных
# name = "Pythonru"
# type_of_site = "Блог"
#
# # заключите переменную в {}, чтобы отобразить ее значение в выводе
# print(F"{name} это {type_of_site}?")
#
# # объявление переменных
# print(f"{2 * 2}")  # вывод: 4
#
#
# def greet(name):
#     return "Привет, " + name
# # вызов функции с использованием f-строки
# name = "Олег"
# print(f"{greet(name)}")
#
#
# # метод title, делает первую букву каждого слова заглавной
# string = "pythonru это блог."
# print(f"{string.title()}")


# import cmath
# cn = complex(3,4)
# # получение значений полярных координат
# print("Polar Coordinates: ",cmath.polar(cn))
# cn1 = cmath.rect(2, cmath.pi)
# print("Polar to rectangular: ",cn1)


# f1 = fractions.Fraction(2, 3)
# f2 = fractions.Fraction(3, 7)
# print('{} + {} = {}'.format(f1, f2, f1 + f2))
# print('{} - {} = {}'.format(f1, f2, f1 - f2))
# print('{} * {} = {}'.format(f1, f2, f1 * f2))
# print('{} / {} = {}'.format(f1, f2, f1 / f2))


#
# import cmath
# print(math.pi)


# PAROL
# password=input('Введите пароль')
# p1=0
# p2=0
# p3=0
# p4=0
#
# if len(password)>8 and len(password)<50:
# p1=1
# else:
# print('Пароль слишком короткий')
#
# if password ==password.lower():
# print('Не хватает больших букв')
# else:
# p2=1
#
# if '#' in password or '*' in password or '-' in password:
# p3=1
# else:
# print('Не зватает специальных символов')
#
# if '1' in password or '2' in password or '3' in password:
# p4=1
# else:
# print('Не хвататет цифр')
#
# if p1+p2+p3+p4=4:
# print('пароль идеальный')


# b=3
# while b<3:
#     print('Вы дали неправильыйн ответ')
# b+=1


# #zadacha 1
# promo = str(input('Vvedite promokod').lower())
# if promo == 'leto':
#     print("activate")
# else:
#     print('oshibka')


# b=input('Введите промокод').lower()
# while b!='лето':
#     print('Ошибка!')
#     b=input('Введите промокод').lower()
#
# print('Промокод активирован!')


# zadacha2
# promo = int(input('Vvedite nomer karti'))
# if promo == 45626:
#     print("Vi viigrali")
# else:
#     print('Povezet v drugoi raz')


# zadacha3
# b=input('Введите otziv')
# while b!='off':
#     print('spasibo')
#     b=input('Введите OTZIV')
#
# print('dosvidaniya sps')


# zadacha4
# summ=0
# a=int(input('Введите покупку'))
# while a!=0:
#      summ=summ+a
#      a=int(input('Введите покупку'))
#
# print(summ*0.9)


# for i in range(3,8):
#           print(i)

# a='boks.'
# print(a[4])
# for i in range(len(a)):
#     print(i, '-', a[i])

# d=[123,13,131,231,31,3,123,13]
# max=0
# for i in d:
#     if max < i:
#         max=i
# print(max)


# 1)Напишите программу ,которая 3 раза спросит у пользователя ответ на вопрос "Сколько ног у сороконожки"
# for i in range(3):
#     input('skolko nog')


# Написать программу для создания группового чата. Количество человек вводится с клавиатуры. Затем по очереди вводятся имена пользователей, добавляемых в чат. В ответ на каждое имя печатается: «Добро пожаловать, <имя>!». После ввода всех имён выводится сообщение: «Групповой чат создан!»
# a=int(input())
# for i in range(a):
#     name=input()
#     print("Добро пожаловать",name)
# print("Gрупповой чат создан!")


# factorial
# res = 1
# n = int(input())
# for i in range(1, n + 1):
#         res *= i
# print(res)

# simbol=['=','?',"^","$","№",'@',"_"]
# login=input()
#
# for i in login:
#     if i in simbol:
#         print('У вас запрещенный символ',i)
#         login=input()
#
# print('Ваш логин идеален')


# simbol=['=','?',"^","$","№",'@',"_"]
# login=input()
# while True:
#     s=0
#     for l in login:
#         if l in simbol:
#             print('У вас запрещенный символ',l)
#             s+=1
#
#
#     if s==0:
#         print('индеальный')
#         break
#     else:
#         login=input()


# '''3)Дано 10 целых чисел. Вычислите их сумму.
# Напишите программу, использующую наименьшее число переменных'''
#
# summ=0
# for i in range(10):
#     a=int(input('Введите цифру '))
#     summ=summ+a
#
#
# print(summ)


'''Напиши программу, запрашивающую ввод трёх музыкальных предпочтений.
После получения каждого предпочтения программа должна печатать:
«Предпочтение учтено». После ввода всех предпочтений,
программа печатает:
«Система рекомендаций настроена!» и завершает работу.'''

# for i in range(3):
#     s=input('Введите предпочтение')
#     print('Предпочтение учтено')
#
# print('Система рекомендаций настроена!')


# Nechetnie chisla
# a = int(input())
# b = int(input())
# for i in range(a,b-1, -1):
#     if i%2!=0:
#         print(i, end=" ")

# reversiya strok
# for i in reversed('bereg'):
#     print(i, end="")

# BEZ YMNOZHENIYA
# x = int(input())
# y = int(input())
# result = 0
# z = 0
# while z != (abs(y)):
#     result = result + (abs(x))
#     z = z + 1
# if (x > 0 and y < 0):
#     result = -result
# elif(x < 0 and y > 0):
#     result = -result
# print(result)


# KVADRATI NA OTREZKE
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#    i**=0.5
#    s=i//1
#    if i==s:
#        print(math.ceil(i**2))


# factorial
# res = 1
# n = int(input())
# for i in range(1, n + 1):
#         res *= i
# print(res)


# skolko nuley
# n = 0 #ob'yavili schetcik
# for i in range(int(input())): #zapusk cikla skolko cifr
#     if int(input()) == 0:
#         n += 1 #esli vstrechaetsya 0 to yvelichivaem schetchik na 1
# print(n)


# chislo = int(input())
# for i in range(1, chislo+1):
#     if chislo % i == 0:
#         i+=1
#         print(i-1, end = " ")


# SUMMA CHISLA
# chislo = int(input())
# sum = 0
# while(chislo > 0):
#     i = chislo % 10
#     sum = sum + i
#     chislo = chislo//10
# print(sum)


# n = int(input())
# tot = 0
# while(n > 0):
#     dig = n % 10
#     tot = tot + dig
#     n = n//10
# print(tot)


# sum = 0
# n = 1
# while n != 0:
#     n = int(input())
#     sum = sum + n
# print(sum)


# n = 1
# max = 0
# while n != 0 and n <= 109:
#     n = int(input())
#     if n > max:
#         max = n
# print(max)


# n = int(input())
# fib = 0
# while n != 0:
#     if n > max:
#         max = n
# print(max)


# #FIBONACCI
# a = int(input())
# f1 = 1
# f2 = 1
# for i in range(2, a):
#    f1, f2 = f2, f1 + f2
# print(f2)


# skolkobolshe = 0
# n = int(input())
# while n != 0:
#     next = int(input())
#     if next != 0 and n < next:
#         skolkobolshe += 1
#     n = next
# print(skolkobolshe)


#
# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# z = int(input("Input third number: "))
# a1 = min(x, y, z)
# a3 = max(x, y, z)
# a2 = (x + y + z) - a1 - a3
# print("Numbers in sorted order: ", a1, a2, a3)

# KWADRATNOE POLE
# x = int(input("vvedite razmer kvadrata"))
# a = '*'
# n = 1
# while n <= x:
#     print(a * x)
#     n+=1


# SUMMA KWADRATOV
# x = int(input())
# s=0
# for i in range(0, x+1):
#     s = s+i*i
# print(s)

# TABLICA UMNOZHENIYA
# s1 = 9
# for i in range(1, s1+1):
#      for j in range(i, i*s1+1, i):
#          print(j, end='\t')
#      print()


# TABLICA SLOZHENIYA
# s1 = 10
# for i in range(2, s1+1, 1):
#      for j in range(i, i+s1-1, 1):
#          print(j, end=' ')
#      print()

# s1 = 5
# for i in range(1, s1+1):
#      for j in range(i, i**s1+1, i):
#          print(j, end=' ')
#      print()


# x = int(input())
# for i in range(0, x):
#     for j in range(0, x):
#         print(j, end=' ')
#     print()


# name=[5,1,4,2,3]
# name.sort()
# print(name)
# name.reverse()
# print(name)


# d='Кот+Осел+Собака Лошадь'
# f=d.split('+')
# print(f)


# '''В конце турнира анализируются результаты
# всех команд. Группа аналитиков должна:
# подсчитать и напечатать средний результат турнира;
# определить результат команды-победителя.'''
# s=0
# d=0
# f=list()
# a=int(input())
# while a!=0:
#     d+=a
#     f.append(a)
# if a>s:
#     s=a
# a=int(input())
# print(s)
# print(d/len(f))


'''Написать программу, которая запрашивает
ввод произвольного числа результатов раунда,
сохраняет их в архив (списком) и печатает
количество команд, получивших больше 200 очков.'''

# a=int(input())
# num=[]
# d=0
# while a!=0:
#     num.append(a)
# if a>=200:
#     d+=1
# print(num)
# print(d)


# SREDNEE ARIFMETICHESKOE
# a=input('Введите все баллы через пролбел')
# a=a.split(' ')
# print(a)
# summ=0
# for i in a:
#     summ+=int(i)
# print(summ / len(a))


# PERVAYA
# niki=['Ivan', 'Petya', 'Sasha', 'Lol', 'lox']
# niki.sort()
# print('KOLICHESTVO:', len(niki))
# for i in range(int(len(niki))):
#     print('{} {}'.format(i+1, niki[i]))


# SPISOK KNIG
# knigi=['qwe', 'qwer', 'qwerty', 'asd']
# novaya=input()
# if novaya in knigi:
#     print('Takaya yzhe est"')
# else:
#     knigi.append(novaya)#append dobavlyaet novii element v konec spiska
#     print('predlozhenie ychteno')
#     print(knigi)


# #2a
# kru=[]
# fam=input('vvedi familiy')
# kru.append(fam)
# print(kru)


# 3
# a=[]
# igra=input('nazvan')
# while igra != '0':
#     if igra in a:
#         print('yzhe est')
#         igra = input('nazvan2')
#     else:
#         a.append(igra)
#         igra = input('nazvan3')
#
# a.sort()
# print(a)


# 4SREDNII BALL PO OCENKAM
# bal = []
# summa = 0
# b = 0
# a = int(input('Ocenca'))
# while a!=0:
#     summa=summa+a
#     b+=1
#     a = int(input('Ocenca'))
# print(summa/b)


# 5
# a = [140, 142, 124, 143, 125, 150]
# a.sort()
# a.reverse()
# b = 0
# summa = 0
# for i in a:
#     b = b+1
#     summa += 1
# print(summa/b)
# print(a[0])


# #4
# spisok=[]
# summ=0
# a=int(input('vvedite cifru'))
# while a!=0:
#     summ+=a
#     spisok.append(a)
#     a = int(input('vvedite cifru'))
# print('srednii ball', summ/len(spisok))


# 5
# a = input()
# a = a.split(' ')
# print(a)
# d = 0
# # for i in a:
# #     if int(i) == 5:
# #         d += 1
# d=a.count('5')
# print(d/len(a)*100)
# a=input()
# a=a.split(' ')
# print(a)
# d=0
# '''for i in a:
# if i=='5':
# d+=1'''
# d=a.count('5')
# print(d/len(a)*100)


# 5
# surname=input()
# dolgnost=input()
# group=input()
# t=[]
# d=[]
# while group!=0:
#     d.append(group)
#     t.append(surname)
#     t.append(dolgnost)
#     t.append(d)
# print(t)


# '''8)Дан список чисел.
# Превратите его в список квадратов этих чисел.'''
#
#
# num=[1,2,5,6,8]
# for i in range(len(num)):
#     num[i]=num[i]**2
#
#
# print(num)


# s = list(map(int, input().split(" ")))
# s2 = []
# for i in range(len(s)):
#     if i%2 == 0:
#         s2.append(s[i])
# print(' '.join(map(str, s2)))


# s = list(map(int, input().split(" ")))#vvod chisel cherez probel
# count = 0
# for i in s:
#     if i / 100 < 10 and s / 100 >= 1 :
# print(' '.join(map(str, s2)))
# nums=list(map(int,input().split()))
# count = 0#schetchik
# for num in nums:
#     if num%5 != 0 and num/100 >= 1:
#         count = count + 1
# print(count)


# number = list(map(int, input().split(" ")))
# number[2], number[4] = number[4], number[2]
# print(' '.join(map(str, number)))


# s = list(map(int, input().split(" ")))
# max = 0
# a = []
# for num in range(len(s)):
#       if num %2 == 0:
#           a.append(s)
# print(' '.join(map(str, a)))


# maksimum v massive
# lst=input().split(' ')
# mn=10e10
# mx=0; p=-1
# for i in range(len(lst)):
#    if (int(lst[i])>0 and int(lst[i]) % 2==0):
#        if (int(lst[i])<mn):
#              mn=int(lst[i])
#        if (int(lst[i])>mx):
#              mx=int(lst[i])
#        p=1
# if (p<0): print('-1')
# else: print(mx)


# CHASTOE CHISLO
# s = list(map(int, input().split()))
# max = s[0]
# mcount = s.count(max)
# for l in s:
#     if s.count(l)>mcount:
#         max = l
# mcount = s.count(l)
# print(max)


# PERESTANOVKA CHETNIH NECHETNIH
# a = [int(i) for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(' '.join([str(i) for i in a]))
# print(*a)

from random import *

# a = [randint(1,10) for i in range(10)]
# shuffle(a)
# print(*a)
# b = sample(a, 5)
# print(*b)
# x = choice(['red', 'green', 'blue'])
# print(x)


# a = ['Merc', 'Ven', 'Zem', 'Mar']
# a = a[::2] #chetnie
# print(a)
# a = a[::-1]#obrantnii poryadok
# print(a)
# a = [[1, 2], [3, 4, 5]]
# a[0]


# ZAPOLNENIE SPISKA
# n = int(input())
# spis = [i for i in range(1, n + 1)]
# print(*spis)


# n = int(input())
# spis = [i for i in range(n, 0, -1)]
# #spis.reverse()
# print(*spis)

# ZAPOLNENIE
# n, m = map(int, input().split())
# lst = (range(n, m + n))
# print(*lst)


# n = int(input())
# print(*[i * i for i in range(1, n + 1)])


# n = int(input())
# spis = [2 ** i for i in range(1, n + 1)]
# spis.reverse()
# print(*spis)


# a=[]#VLOZHENIE SPISKI
# n=int(input())
# for i in range(n):
#     a.append(list(map(int,input().split())))
# print(a)


# a=[]
# n=int(input())
# for i in range(n):
#     a.append(list(map(int,input().split())))
# if a[0][2] == a[2][0]:
#     print('yes')
# else:
#     print('no')


# n, m = map(int, input().split())#vvodim razmer matrici
# maxi = -9999999#ykazivaem maksimum
# for i in range(n):#zapusk cikla
#     a = list(map(int, input().split()))#schitivaem vlozhenie massivi
#     for j in range(m):#zapusk cikla v cikle
#         if a[j] > maxi:#esli a[0][0]>-99999 to max i
#             stroka = i
#             stolbec = j
#             maxi = a[j]
# print(stroka, stolbec)


# SUMMA CHISEL V MASSIVE
# s = sum([10,20,30])
# print("\nSum of the container: ", s)
# print()


# s=input()
# s1=""
# i=0
# for c in s:
#     if c=='a' or c =='A':
#         c='b'
#         i+=1
#     s1+=c
# print(s1)
# print(i)


# KOLICHESTVO SLOV CHEREZ PROBEL
# s=input()
# print(s.count(' ')+1)


# YDALENIE ILI ZAMENA SIMVOLA
# s=input()
# s=s.replace('@','')
# print(s)

# str = input()
# print(str.translate({ord(i): None for i in '@'}))


# s = [int(i) for i in input().split(' ')]#DOBAVLYAEM V SPISOK CHISLOVIE ZNACHENIYA S KLAVIATURI
# m = max(s)#ISPOLZUEM FUNKCIU MAX
# print(m, s.index(m))#PECHATAEM MAX I INDEX ELEMENTA V STROKE


# s=input().split()#SCHITIVAEM CHEREZ PROBEL
# s.sort()#OT MIN DO MAX
# print(*s)
# s.reverse()#OT MAX DO MIN
# print(*s)


# s=input()
# s=s.count(' ')+1
# print(s)


# a = input()#PERVOE SLOVO
# for i in range(len(a)):
#   if a[i] == ' ':
#       break
#   else:
#       print(a[i], end="")

# a=input()#TRETE SLOVO S KONCA
# s2=a.split()
# print(s2[-3])


# s = input()
# s = s.split()
# print(max(s, key=len))

# FAMILIYA IMYA OTCHESTVO
# a=input().split()
# print(a[2], a[0][0]+"."+a[1][0]+".")
# # Roman Eduardovich Fedoreev
# # Fedoreev R.E.

# PUT K FAILU
# s=input()
# for i in s.split('\\'):
#     print(i)


# # Основная строка
# main_string = 'Hello world'
# print("<<< %s >>>" % (main_string))
#
# # Третий символ этой строки
# string2 = main_string[2]
# print(string2)  # l
#
# # Первые пять символов этой строки
# string3 = main_string[0:5]
# print(string3)  # Hello
#
# # Вся строкеа, кроме последних двух символов
# string4 = main_string[0:len(main_string) - 2]
# print(string4)  # Hello wor
#
# # Все символы с четными индексами...
# string5 = main_string[::2]
# print(string5)  # Hlowrd
#
# # Все символы с нечетными индеками
# string6 = main_string[1::2]
# print(string6)  # el ol
#
# string7 = main_string[::-1]
# print(string7)  # dlrow olleH
#
# string8 = main_string[::-2]
# print(string8)  # drwolH
#
# string9 = len(main_string)
# print(string9)  # 11

# a=input().split()
# print(a[0][2])
# print(a[0][-2])
# print(a[0][0:5])
# print(a[0][0:-2])
# print(a[0][::2])
# print(a[0][1::2])
# print(a[0][::-1])
# print(a[0][::-2])
# print(len(a[0]))


# PALINDROM
# slovo = str(input())
# a = slovo[::-1]
# if slovo == a:
#   print("yes")
# else:
#   print("no")


# a=input().split()
# print(*a[-1::6], *a[0::5])


# '''Написать программу, запрашивающую
# название книги и печатающую её расположение
# в хранилище библиотеки. Если указанной книги нет,
# то напечатать: «Такой книги нет!»'''
#
# title = input('Введите название книги:')
# title = title.lower()
# if title == 'карлик нос':
#   print('ряд 7 полка 6')
# elif title == 'волшебное кольцо':
#   print('ряд 1 полка 2')
# elif title == 'васюткино озеро':
#   print('ряд 10 полка 3')
# # ...
# else:
#   print('Такой книги нет!')


# '''Написать программу, запрашивающую
# название книги и печатающую её расположение
# в хранилище библиотеки. Если указанной книги нет,
# то напечатать: «Такой книги нет!»'''
# title = input('Введите название книги:')
# title = title.lower()
# books = ['васюткино озеро', 'волшебное кольцо']
# addresses = ['ряд 10 полка 3', 'ряд 1 полка 2']
# if title in books:
# for i in range(len(books)):
# if books[i] == title:
#   print('Расположение книги:', addresses[i])
# else:
#   print('Такой книги нет!')


# '''Написать программу, запрашивающую
# название книги и печатающую её расположение
# в хранилище библиотеки. Если указанной книги нет,
# то напечатать: «Такой книги нет!»'''
# title = input('Введите название книги:')
# title = title.lower()
# а=['волшебное кольцо']
# book={
# 'волшебное кольцо':"Ряд 10 полка 3",
# "пиковая дама":"Ряд 30 полка 1",
# "идиот":"РЯд 4 полка 6"
# }


# '''Написать программу, запрашивающую
# название книги и печатающую её расположение
# в хранилище библиотеки. Если указанной книги нет,
# то напечатать: «Такой книги нет!»'''
#
# а=['волшебное кольцо']
# book={
# 'Волшебное кольцо':
# {
# 'Ряд':"10",
# "Полка":"3"
# },
# 'Пиковая дама':[5,9]
#
#
# }
#
# print(book['Пиковая дама'][0])


# book={
#   'Volshebnoe kalco':8,
#   'pikovaya':5
# }
# print(*book.keys())
# a=input()
# if a in book:
#   print(book[a])
# else:
#   print('Oshibka')


# '''Дополнить предыдущую программу возможностью
# взять книгу из хранилища. В дополнение программа
# должна:
# Запрашивать ввод ответа на вопрос: «Хотите взять?».
# Если да — уменьшать количество имеющихся книг.'''
#
#
# book={
# 'Волшебное кольцо':8,
# 'Пиковая дама':5
# }
#
# print(book.keys())
# a=input()
# if a in book:
#   f=input('Хотите взять?')
#   if f=='да':
#     book[a]=book[a]-1
#     print(book)
#   else:
#     print('Ну и не надо ')
#
#
# else:
#     print("ОШибка")


# books = {
#    'Гарсиа Маркес': 'Сто лет одиночества',
#    'Лондон': 'Белый клык',
#    'Кинг': 'Зеленая миля',
#    'Достоевский': 'Идиот'}
# books['Bulgakov'] = 'Master and margarita'
# print(books)
# del books['Лондон']
# print(books)


# books = {
#    'Гарсиа Маркес': 'rodilsya v kieve v 1577',
#    'Лондон': 'rodilsya v moskve v 1587',
#    'Кинг': 'rodilsya v xarkove v 1570',
#    'Достоевский': 'rodilsya v berline v 1517'
# }
# a=input('kogo ishesh?')
# if a in books:
#    print(books[a], end=',')
# else:
#    print('Takih net')
#    b=input('Hotite dobavit?(da ili net)')
#    if b == 'da':
#       books['Bulgakov'] = 'Master and margarita'
#       print(books, end=',')

##3
# stud={
#    'stud1' : 'gruppa1',
#    'stud2' : 'gruppa2',
#    'stud3' : 'gruppa3'
# }
# a = input('stud kakoi?')
# if a in stud:
#    print(stud[a])

# #4.2
# tovar = {
#    'pleer' : 3,
#    'telefon' : 2,
#    'pilesos' : 1
# }
# print(*tovar, sep = ',')
# a = input('Chto nyzhno?')
# if a in tovar:
#    print('Kolvo na sklade:', tovar[a])
#    b = input('Kupite?(+ -)')
#    if b == '+':
#       tovar[a] = tovar[a] - 1
#       print(tovar, 'sps za pokupku')
#    else:
#       print('dosvidos')
# else:
#    print('takogo net tovara')

# #5
# students = {}
# a = input('Vvedite studenta1')
# b = input('Vvedite studenta2')
# c = input('Vvedite studenta3')
# students[a] = 10
# students[b] = 15
# students[c] = 100
#
# print(students, sep=',')


# # 5.1
# s = {
#     'zharko': 'znoino',
#     'mokro': 'suro'
# }
# a = input('vvedite slovo')
# if a in s:
#     print(s[a])
# else:
#     print('Takih net')
#     b=input('Hotite dobavit?(da || net)')
#     if b == 'da':
#         slovo = input('Vvedite slovo')
#         sinonnew = input('Vvedite sinonim')
#         s[slovo] = sinonnew
#         print('Vashi sinonimi dobaleni')
#         for key, value in s.items():
#             print('Spisok sinonimov:', key, ':', value)
#     else:
#         print('Zhalko, poka')


# sinonim = {
#     'радость': 'веселье',
#     'говорить': "беседовать",
#     "худой": "тощий"
# }
#
# s = input('Введите слово к которому нужен синоним')
# if s in sinonim:
#     print('Синоним к слову', s, "это слово", sinonim[s])
# else:
#     d = input('Введите синоним')
# sinonim[s] = d
# print(sinonim)


#SKOLKO ODINAKOVIH SLOV
# counter = {}
# for word in input().split():
#     counter[word] = counter.get(word, 0) + 1
#     print(counter[word] - 1, end=' ')

# #KALKULYATOR
# # The user's inputs for the numbers and the operators
# num1 = float(input('Enter your first number: '))
# Operator = input('Enter operator: ')
# num2 = float(input('Enter your second number: '))
#
# # if Operator is (+ | - | * | /) then  print out number 1 (+ | - | * | /) number 2
# if Operator == '+':
#     print(num1 + num2)
# elif Operator == '-':
#     print(num1 - num2)
# elif Operator == '/':
#     print(num1 / num2)
# elif Operator == '*':
#     print(num1 * num2)
#
# # if the user didn't put an operator
# else:
#     print('Not a valid operator')

# sinonim = {
#     'радость': 'веселье',
#     'говорить': "беседовать",
#     "худой": "тощий"
# }
#
# s = input('Введите слово к которому нужен синоним')
# if s in sinonim:
#     print('Синоним к слову', s, "это слово", sinonim[s])
# else:
#     d = input('Введите синоним')
# sinonim[s] = d
# print(sinonim)

# a = set('Hi, guys!')
# print(type(a))
# print(len(a))



# a = set(input())
# b = {'.', ',', ';', ':', '!', '?'}
# c = (a & b)
# print(len(c))


# a = set(input())
# b = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
# e = (a & b)
# if e == set():
#     print('NO')
#
# else:
#     c = (a & b)
#     d = list(c)
#     d.sort()
#     print(*d, sep = '')



# a = set(input())
# b = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
# c = (b ^ a)
# print(c)


# a = set(input())
# b = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
# e = (a & b)
# if 'a' in a:
#     print('NO')
#
# else:
#     c = (a & b)
#     d = list(c)
#     d.sort()
#     print('YES')

# lst = input()
# out = []
# for x in lst:
#     if not x in out:
#         out.append(x)
# print(*out, sep = '')



# a = set(input())
# b = len(a)
# print(b)

# def a(x, y):
#     # x, y = map(float, input().split())
#     x = x ** y
#     print(x)
#     return x
# x, y = map(float, input().split())
# a(x, y)


# def a(x, y, b, c):
#     min = 99999999999
#     if x < min:
#        min = x
#     elif y < min:
#         min = y
#     elif b < min:
#         min = b
#     elif c < min:
#         min = c
#     print(min)
#     return min
# x, y, b, c = map(int,input().split())
# a(x, y, b, c)


# def xor(x, y):
#     if x != 0 ^ y != 0:
#         print(1)
#     elif x == 1 and y == 0:
#         print(1)
#     else:
#         print(0)
# x, y = map(int,input().split())
# xor(x, y)



#
# print(-(-int(input())//2))

# a = int(input())
# a = (a + 3) // 4
# print(a)


# a = int(input())
# ch = a // 60
# mi = a % 60
# print(a, 'мин - это', ch, 'час', mi, 'минут')


# num = int(input())
# x = [int(a) for a in str(num)]
# print(*x)

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print('Сумма цифр =', digit1 + digit2 + digit3)
# print('Произведение цифр =', digit1 * digit2 * digit3)


# Последняя цифра: (num % 10**1) // 10**0;
# Предпоследняя цифра: (num % 10**2) // 10**1;
# Предпредпоследняя цифра: (num % 10**3) // 10**2;
# .....
# Вторая цифра: (num % 10n-1) // 10n-2;
# Первая цифра: (num % 10n) // 10n-1.

#
# num = int(input())            # берем 5-ти значимое число к примеру "45826"
# digit1 = num // 10 ** 4            # получаем 1-е число "4"
# digit2 = (num // 10 ** 3) % 10     # получаем 2-е число "5"
# digit3 = (num // 10 ** 2) % 10     # получаем 3-е число "8"
# digit4 = (num // 10) % 10          # получаем 4-е число "2"
# digit5 = num % 10                  # получаем 5-е число "6"
# print(digit1, digit2, digit3, digit4, digit5,  sep='_')


# a = "Python"
# a = a[-2:]
# print(a)




# #GENERATOR_PAROLYA
# import string
# import random
#
#
# def password_generator(length):
#     """ Function that generates a password given a length """
#
#     uppercase_loc = random.randint(1,4)  # random location of lowercase
#     symbol_loc = random.randint(5, 6)  # random location of symbols
#     lowercase_loc = random.randint(7,12)  # random location of uppercase
#
#     password = ''  # empty string for password
#
#     pool = string.ascii_letters + string.punctuation  # the selection of characters used
#
#     for i in range(length):
#
#         if i == uppercase_loc:   # this is to ensure there is at least one uppercase
#             password += random.choice(string.ascii_uppercase)
#
#         elif i == lowercase_loc:  # this is to ensure there is at least one uppercase
#             password += random.choice(string.ascii_lowercase)
#
#         elif i == symbol_loc:  # this is to ensure there is at least one symbol
#             password += random.choice(string.punctuation)
#
#         else:  # adds a random character from pool
#             password += random.choice(pool)
#
#     return password  # returns the string
#
# print(password_generator(12))




# import random
# def parol1():
#     parol = [1, 'A', 'a', '!', 2, 3, 4, 5, 6, 7, 8, 9]
#     random.shuffle(parol)
#     print('Vash parol: ',*parol, sep='')
#     novii = input('Hotine sgenerirovat novii parol? "+", esli hotite, "-", esli net')
#     if novii == '+':
#         parol = [1, 'A', 'a', '!', 2, 3, 4, 5, 6, 7, 8, 9]
#         random.shuffle(parol)
#         print('Vash novii parol: ', *parol, sep='')
#
#     else:
#         print('Dosvidaniya')
# parol1()

# RANDOM PAROL
# import random
# print(''.join([random.choice(list('123456789!"№;%:?*()qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)]))


# def rev():
#     x = input().split()
#     x.reverse()
#     print(*x)
# rev()


# def fun():
#     a=list(input())
#     print(len(a))
# fun()


# def distance():
#     x1 = int(input())
#     y1 = int(input())
#     x2 = int(input())
#     y2 = int(input())
#     dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#     print(dist)
# distance()

# f = open('build.txt')
# f.read()

# import math
# import string
# f = open('testinput.txt', 'w+')
# f.write('2\n2')
# t = map(int, f.read().split())
# # data = [map(sum(int, line.split()))for line in f]
# t = int(sum(t))
# a = open('testoutput.txt', 'w')
# a.write(str(t))
# print(type(t))
# print(f.read())
# print(t)
# f.close()
# a.close()

# VOZVEDENIE V STEPEN REKURSIYA
# def power(a, n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return a
#     if n != 1:
#         return (a * power(a, n - 1))
# a, n = int(input()), int(input())
# print(power(a, n))

#FIBONACCI REKURSIYA
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n -1) + fib(n - 2)
# print(fib(int(input())))


# print('Доступ запрещен' if int(input()) < 18 else 'Доступ разрешен')


# print(min(int(input()), int(input()), int(input()), int(input())))
#
# age = int(input())
# print("детство" if 0 <= age <= 13 else "молодость" if 14 <= age <= 24 else "зрелость" if 25 <= age <= 59 else "")
#
#


# x = int(input())
# if x > -30 and x <= -2 or x > 7 and x <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# x = int(input())
# if (1000 <= x <= 9999) and (x % 7 == 0 or x % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# a, b, c = int(input()), int(input()), int(input())
# if (a + b > c and a + c > b) and b + c > a:
#     print('YES')
# else:
#     print('NO')

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# res1 = x2 - x1
# res2 = y2 - y1
# if -1 <= res1 <=1 and -1 <= res2 <=1:
#     print('YES')
# else:
#     print('NO')

# import random
# from random import choice
# with open('FIO.txt', 'w') as fio:
#     while True:
#         vvodFIO = input('Vvedite FIO sotrudnikov: ')
#         fio.write(vvodFIO + '\n')
#         if not vvodFIO:
#             break
# skolkosotr = len(open('FIO.txt').readlines())
# pochta = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# with open('POCHTA.txt', 'w') as file:
#     for i in range(skolkosotr - 1):
#         random.shuffle(pochta)
#         str = ''.join(pochta)
#         file.write(f"{str}@prof.ru" + '\n')
#         # print(type(pochta))

# print('VVedite chislo:')
# x = int(input())


# x = int(input('Загадай любое целое число от 0 до 100!'))
# print('Спорим, я угадаю его за ? Я буду называть числа, а ты — отвечать, оно больше, меньше или равно загаданному.')
# zz = input()
# print('Спорим, угадаю!')
# zz = input()
# print('это 50')
# if x == 50:
#     print('Я же говорил')
# else:
#     z1 = input('Больше или меньше?')
#     if z1 == 'Больше':
#         z2 = input('Может быть 75?')
#         if z2 == 'меньше':
#             z3 = input()



# # импортируем модуль для работы со случайными числами
# import random
#
# # число попыток угадать
# guesses_made = 0
#
# # получаем имя пользователя из консольного ввода
# name = input('Привет! Как тебя зовут?\n')
#
# # получаем случайное число в диапазоне от 1 до 30
# number = random.randint(1, 30)
# print('Отлично, {0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))
#
# # пока пользователь не превысил число разрешенных попыток - 6
# while guesses_made < 6:
#
#     # получаем число от пользователя
#     guess = int(input('Введи число: '))
#
#     # увеличиваем счетчик числа попыток
#     guesses_made += 1
#
#     if guess < number:
#         print('Твое число меньше того, что я загадал.')
#
#     if guess > number:
#         print('Твое число больше загаданного мной.')
#
#     if guess == number:
#         break
#
# if guess == number:
#     print('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
# else:
#     print('А вот и не угадал! Я загадал число {0}'.format(number))



# m = input()
# a = map(int, input().split())
# x = int(input())
# if x in a:
#     print("YES")
# else:
#     print("NO")


# input()
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print('\n'.join(['NO' if bisect.bisect_left(a,c) - bisect.bisect_right(a,c) == 0 else 'YES' for c in b]))

# def func(**args):
#     return args
# print(func(a = 23, b = 45))
# add = lambda x, y: x * y
# print(add(2, 5))
# print(add('q', 5))
# print((lambda x, y: x * y)(2 ,6))
# fun = lambda *args: args
# print(sum(fun(int(input()), int(input()))))





# #PEREVOD MASSIVA V INT
# spis = input().split()
# for i in range(len(spis)):
#     spis[i] = int(spis[i])
# print(spis)

#BUBBLE_SORT
# def bubble_sort(arr):
#     def swap(i, j):
#         arr[i], arr[j] = arr[j], arr[i]
#     n = len(arr)
#     swapped = True
#     x = -1
#     while swapped:
#         swapped = False
#         x = x + 1
#         for i in range(1, n - x):
#             if arr[i - 1] > arr[i]:
#                 swap(i - 1, i)
#                 swapped = True
#     return arr
# arr = input().split()
# for i in range(len(arr)):
#     arr[i] = int(arr[i])
# print(bubble_sort(arr))

# def bubble_sort(arr):
#     def swap(i, j):
#         arr[i], arr[j] = arr[j], arr[i]
#     n = len(arr)
#     swapped = True
#     x = -1
#     while swapped:
#         swapped = False
#         x = x + 1
#         for i in range(1, n - x):
#             if arr[i - 1] > arr[i]:
#                 swap(i - 1, i)
#                 swapped = True
#     return arr
# arr = input().split()
# bubble_sort(arr)
# arr.reverse()
# print(*arr)


# def bubble_sort(arr):
#     def swap(i, j):
#         arr[i], arr[j] = arr[j], arr[i]
#     n = len(arr)
#     swapped = True
#     x = -1
#     total = 0
#     while swapped:
#         swapped = False
#         x = x + 1
#         for i in range(1, n - x):
#             if arr[i - 1] > arr[i]:
#                 swap(i - 1, i)
#                 swapped = True
#                 total += 1
#     print(total)
#     return arr
#
# zzz = input()
# arr = input().split()
# bubble_sort(arr)
# arr.reverse()
# # print(*arr)



# def bubbleSort(nlist):
#     for passnum in range(len(nlist)-1,0,-1):
#         for i in range(passnum):
#             if nlist[i]>nlist[i+1]:
#                 temp = nlist[i]
#                 nlist[i] = nlist[i+1]
#                 nlist[i+1] = temp
#
# nlist = [14,46,43,27,57,41,45,21,70]
# bubbleSort(nlist)
# print(nlist)



# def selectionSort(A):
#    for fillslot in range(len(A) - 1, 0, -1):
#        maxpos=0
#        for location in range(1,fillslot+1):
#            if A[location]>A[maxpos]:
#                maxpos = location
#
#        temp = A[fillslot]
#        A[fillslot] = A[maxpos]
#        A[maxpos] = temp
#
# nlist = [14,46,43,27,57,41,45,21,70]
# selectionSort(nlist)
# print(*nlist, sep = '(っ◕‿◕)っ')



# def countsort (A, B):
#     c = [0] * (B + 1)
#     for i in range(len(A)):
#         c[A[i]] = c[A[i]] + 1
#
#     # Find the last index for each element
#     c[0] = c[0] - 1  # to decrement each element for zero-based indexing
#     for i in range(1, B + 1):
#         c[i] = c[i] + c[i - 1]
#
#     result = [None] * len(A)
#
#     # Though it is not required here,
#     # it becomes necessary to reverse the list
#     # when this function needs to be a stable sort
#     for x in reversed(A):
#         result[c[x]] = x
#         c[x] = c[x] - 1
#
#     return result
#
# alist = input().split()
# alist = [int(x) for x in alist]
# k = max(alist)
# sorted_list = countsort(alist, k)
# print(*sorted_list)


# def insertsort(A):
#     for i in range(1, len(A)):
#         for j in range(i, 0, -1):
#             if A[j] < A[j-1]:
#                 A[j], A[j-1] = A[j-1], A[j]
#             else:
#                 break
#     return A
# A = input().split()
# A  = insertsort(A)
# print(*A)
# A.append(([21, 34, 56]))
# print(*A)
# print(*A)


# n, m = map(int, input().split())
# p = [list(map(int, input().split())) for i in range(n)]
# a = [[0] * m for i in range(n)]
# a[0][0] = p[0][0]
#
# for j in range(1, m):
#     a[0][j] = a[0][j - 1] + p[0][j]
# for i in range(1, n):
#     a[i][0] = a[i - 1][0] + p[i][0]
# for i in range(1, n):
#     for j in range(1, m):
#         a[i][j] = max(a[i][j - 1], a[i - 1][j]) + p[i][j]
# print(a[-1][-1])


# n, m = map(int, input().split())
# p =[list(map(int, input().split())) for i in range(n)]
# a = [[0] * m for i in range(n)]
# b = [[''] * m for i in range(n)]
# a[0][0] = p[0][0]
# for j in range(1, m):
#     a[0][j] = a[0][j - 1] + p[0][j]
#     b[0][j] = b[0][j-1] + 'R '
# for i in range(1, n):
#     a[i][0] = a[i - 1][0] + p[i][0]
#     b[i][0] = b[i - 1][0] + 'D '
# for i in range(1, n):
#     for j in range(1, m):
#         if a[i][j -1] > a[i - 1][j] :
#             a[i][j] = a[i][j -1] + p[i][j]
#             b[i][j] = b[i][j -1] + 'R '
#         else :
#             a[i][j] = a[i-1][j] + p[i][j]
#             b[i][j] = b[i-1][j] + 'D '
# print(a[-1][-1])
# print(b[-1][-1])



#
# print('HELLO1')
# print('HELLO2')
# try:
#     print(int('dgfdg'))
# except ValueError:
#     print('nepravilnoe znachenie, nuzhno vvodit cifri')
# print('HELLO3')
# print('HELLO4')





# def tempkel():
#     print('(っ◕‿◕)っ---Переводчик градусов Кельвину в градусы Фарингейта приветствует Вас---(っ◕‿◕)っ\n')
#     kel = float(input('Введите температуру по Кельвину: '))
#     if kel < 0.0:
#         raise ValueError('ОООЧЕНЬ ХОЛОДНО')
#     else:
#         f = (kel - 273.15) * 1.8000 + 32.00
#         print('✌(◕‿-)✌\nТемпература в градусах Фаренгейта:', f)
#
# tempkel()

# n = int(input())
# counter_last = n % 10
# count3 = 0             #количество цифр 3 в нем;
# count_pos = 0          #сколько раз в нем встречается последняя цифра;
# count_chet = 0         #количество четных цифр;
# sub5 = 0               #сумму его цифр, больших пяти;
# proiz_b5 = 1           #произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра 
# count0_5 = 0           #сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
# while n != 0:
#     a = n % 10
#     if a == 3 :
#         count3 += 1
#     if a == counter_last:
#         count_pos += 1
#     if a % 2 == 0:
#         count_chet += 1
#     if a > 5:
#         sub5 += a
#     if a > 7:
#         proiz_b5 *= a
#     if a == 0 or a == 5:
#         count0_5 += 1
#     n //= 10      
# print(count3, count_pos, count_chet, sub5, proiz_b5, count0_5, sep = '\n')
