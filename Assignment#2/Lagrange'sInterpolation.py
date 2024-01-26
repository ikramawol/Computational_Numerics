def lagrange_interpolation(x, x_values, y_values):
    result = 0
    for i in range(len(x_values)):
        term = y_values[i]
        for j in range(len(x_values)):
            if i != j:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result
