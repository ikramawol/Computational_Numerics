# Python imlementation for Trapezoidal Integration
def trapezoidal_integration(func, a, b, n):
    
    h = (b - a) / n  
    result = 0.5 * (func(a) + func(b))  
    for i in range(1, n):
        result += func(a + i * h)  
    result *= h  
    return result
