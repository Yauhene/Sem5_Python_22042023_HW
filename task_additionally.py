#=======================================================================================
# ** Дополнительно **
# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

def fuck_fib(n, c = 0, list_1 = []):
    print()
    add = 0
    if c < n:
        if c < 2:
            add = 1
            list_1.append(add)
            
            fuck_fib(n, c+1)
            return list_1[-1]   
        else:
            add = list_1[c-2] + list_1[c-1]
            
            list_1.append(add)
            
        fuck_fib(n, c+1)  
        return list_1[-1]  
    else:
        print(list_1)
             
        return list_1[-1]   
        
    
n = int(input("Введите номер элемента по порядку: "))

print(n,'-й элемент последовательности Фибоначчи равен', fuck_fib(n))
print() 