# Python Implementation for simpsons one third integration (1/3)
def simpsons_one_third_integration(func, a, b, n):

    h = (b - a) / n  
    x = [a + i * h for i in range(n+1)]  
    y = [func(x_i) for x_i in x]  

    result = y[0] + y[-1]  
    for i in range(1, n, 2):
        result += 4 * y[i]  
    for i in range(2, n-1, 2):
        result += 2 * y[i]  
    result *= h / 3  
    return result


