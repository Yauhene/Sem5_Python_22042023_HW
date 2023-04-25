#=======================================================================================
#Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) 
#для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def fact_and_triangle(n):
    res_f = 1
    res_t = 0
    count = n
    #n -= 1
    print('res_f = ', res_f, ", " 'res_t = ', res_t)

    if count != 1:
        print('вошли в if +++++++++++++++++++++++++++++++')
        print('n = ', n, ' ', 'count =', count, 'res_f = ', res_f, 'res_t = ', res_t)
        
        #print(f'res_f = {res_f}, n = {n} ')
        res_f = res_f * count
        print(f'res_f = {res_f}')
        input('жми...')
        #print(f'res_f = res_f * (n - 1) = {res_f}')
        #res_t = n + (n-1)
        #count += 1
        fact_and_triangle(count-1)
        
        #print('res_f = ', res_f, 'res_t = ', res_t)
        return res_f, res_t
        #return res_t
    else:
        
        return res_f, res_t
        # return res_t
        print(res_f)
        print(res_t)
    
print()
n = 5
print(fact_and_triangle(n))
print()