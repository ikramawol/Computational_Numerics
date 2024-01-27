# Python Implementation for simpsons three eighth integration (3/8)
def simpsons_three_eighth_integration(func, a, b, n):
    
    h = (b - a) / n  
    x = [a + i * h for i in range(n+1)]  
    y = [func(x_i) for x_i in x]  
    
    result = y[0] + y[-1] 
    for i in range(1, n, 3):
        result += 3 * (y[i] + y[i+1])
    for i in range(3, n-1, 3):
        result += 2 * y[i]
    result *= 3 * h / 8 
    return result