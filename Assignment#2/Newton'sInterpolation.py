# Python Implementation for Newton's Interpolation
def newton_interpolation(x, x_values, y_values):
   
    n = len(x_values)
    coefficients = y_values.copy()
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i - 1]) / (x_values[i] - x_values[i - j])

    result = coefficients[n - 1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_values[i]) + coefficients[i]

    return result

