
# Regression

## Linear Regression

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data. The equation takes the form \(Y = b_0 + b_1 \cdot X\), where \(Y\) is the dependent variable, \(X\) is the independent variable, \(b_0\) is the y-intercept, and \(b_1\) is the slope. This method is particularly useful for predicting the value of the dependent variable based on the values of one or more independent variables.

## Polynomial Regression

Polynomial regression is an extension of linear regression that allows for more complex relationships between the dependent and independent variables. Instead of fitting a straight line, it fits a polynomial equation to the data. The equation takes the form \(Y = b_0 + b_1 \cdot X + b_2 \cdot X^2 + \ldots + b_n \cdot X^n\), where \(n\) is the degree of the polynomial. This method is suitable for datasets where the relationship is not strictly linear.

# Interpolation

## Newton Interpolation

Newton interpolation is a method for constructing a polynomial that passes through a given set of data points. It is particularly useful when the data points are unevenly spaced. The interpolation polynomial is represented in the Newton form, making it efficient for incremental calculations. Newton interpolation is commonly used in numerical analysis and mathematical modeling.

## Lagrange Interpolation

Lagrange interpolation is another method for constructing an interpolating polynomial through a given set of data points. The polynomial is a weighted sum of Lagrange basis polynomials, each associated with a specific data point. Lagrange interpolation is straightforward to implement and provides a polynomial that passes through all given data points.

# Integration

## Trapezoidal Rule

The trapezoidal rule is a numerical integration method used to estimate the definite integral of a function. It approximates the area under the curve by dividing the interval into small trapezoids and summing their areas. While simple, the trapezoidal rule provides a reasonable estimate for integrals and is easy to implement.

## Simpson's Rule (1/3, 3/8)

Simpson's rule is another numerical integration method that provides a more accurate estimate of the definite integral compared to the trapezoidal rule. It uses quadratic or cubic approximations for the function within each subinterval. The 1/3 and 3/8 refer to two variations of Simpson's rule, depending on the number of intervals used. These methods offer improved accuracy for a wide range of functions.

<i>GitHub Link: https://github.com/ikramawol/Computational_Numerics/tree/main/Assignment%232</i>

<h2>AUTHORS</h2>
 <ol>
   <li>Hiriya Girma ID: ETS0810/14</li>
   <li>Ikram Awol ID: ETS0823/14</li>
   <li>Mekdes Lemesa ID: ETS1022/14</li>
</ol>