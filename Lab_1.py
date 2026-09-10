#Лабораторна 1

print("Hello World")

#Змінні різних типів

name="nazar"                                #str - рядок
age = 16                                    #int - ціле число
height = 1.80                               #float - дробове число
is_student = True                           #bool - логічний тип
lst = [1,2,3,4,5]                           #list - список
st = {1, 2, 3, 4, 5}                        #set - множина
dct = {"name":"Nazar", "age":16}            #dict - словник

#Виведення значення та їх типів

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(lst, type(lst))
print(st, type(st))
print(dct, type(dct))
print(is_student, type(is_student))

#Арифметичні оператори

a = 10
b = 3

print("додавання", a+b)
print("віднімання", a-b)
print("множення", a*b)
print("ділення", a/b)
print("цілочисельне ділення", a//b)
print("остача від ділення", a%b)
print("піднесеня до степеня", a**b)
