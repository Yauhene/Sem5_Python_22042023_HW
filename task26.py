#=======================================================================================
#Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) 
#для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def fact_and_triangle_fact(n):
    res_f = n
    count = n
    #print('res_f = ', res_f, ", " 'res_t = ', res_t)

    if n > 1 :
        #print('вошли в if +++++++++++++++++++++++++++++++')
        #print('n = ', n, ' ', 'count =', count, 'res_f = ', res_f)#, 'res_t = ', res_t)
        
        #print(f'res_f = {res_f}, n = {n} ')
        res_f = res_f * fact_and_triangle_fact(count-1)
        #res_t = res_t + fact_and_triangle_fact(count-1)
        #print(fact_and_triangle(n-1))
        #print(f'res_f = {res_f}')
        #input('жми...')
        #print(f'res_f = res_f * (n - 1) = {res_f}')
        #res_t = n + (n-1)
        #count += 1
        
        
        #print('res_f = ', res_f, 'res_t = ', res_t)
        return res_f
        #return res_t
    else:
        
        return res_f
        # return res_t
        #print(res_f)
        #print(res_t)

def fact_and_triangle_triangle(n):
    res_t = n
    count = n
    #n -= 1
    #print('res_t = ', res_t)

    if n > 0:
        #print('вошли в if +++++++++++++++++++++++++++++++')
        #print('n = ', n, ' ', 'count =', count,  'res_t = ', res_t)
        
        #print(f'res_f = {res_f}, n = {n} ')
        
        res_t = res_t + fact_and_triangle_triangle(count-1)
        #print(fact_and_triangle_triangle(n-1))
        #print(f'res_t = {res_t}')
        #input('жми...')
        #print(f'res_f = res_f * (n - 1) = {res_f}')
        #res_t = n + (n-1)
        #count += 1
        
        
        #print('res_t = ', res_t)
        return  res_t
    else:
        
        return  res_t
        # return res_t
        
        #print(res_t)

def fact_and_triangle(n):
    res_f = fact_and_triangle_fact(n)
    print(res_f)
    res_t = fact_and_triangle_triangle(n)
    res = [res_f, res_t]
    return res

    
print()
n = 5
print(f'Факториал числа {n}: {fact_and_triangle(n)[0]}')
print(f'Треугольное число числа {n}: {fact_and_triangle(n)[1]}')
print()