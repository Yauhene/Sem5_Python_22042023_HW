#=======================================================================================
#Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) 
#для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def fact_and_triangle_fact(n):
    res_f = n
    count = n

    if n > 1 :
        res_f = res_f * fact_and_triangle_fact(count-1)
        print('count = ', count)
        return res_f
    else:
        return res_f

def fact_and_triangle_triangle(n):
    res_t = n
    count = n

    if n > 0:
        res_t = res_t + fact_and_triangle_triangle(count-1)
        return  res_t
    else:
        return  res_t

def fact_and_triangle(n):
    res_f = fact_and_triangle_fact(n)
    res_t = fact_and_triangle_triangle(n)
    res = [res_f, res_t]
    return res

    
print()
n = int(input('Введите число: '))
print(f'Факториал числа {n}: {fact_and_triangle(n)[0]}')
print(f'Треугольное число числа {n}: {fact_and_triangle(n)[1]}')
print()