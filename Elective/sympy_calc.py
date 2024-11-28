from scipy.special import jn, yn, jn_zeros, yn_zeros
from scipy.integrate import quad, dblquad, tplquad
import sympy as sp

# x² = 2x
#x = sp.symbols('x')
#equation = sp.Eq(x**2, 2*x)
#print("Solutions:", sp.solve(equation, x))

# 1_integral_4(x*log(x²) dx)
#x = sp.symbols('x')
#integral = sp.integrate(x*sp.log(x**2), (x, 1, 4))
#print("Solutions:", integral)

# 0_integral_3(x²_integral_9(x³*e^y dy) dx)
#x, y = sp.symbols('x'), sp.symbols('y')
#integral = sp.integrate(x**3 * sp.E**y, (y, x**2, 9), (x, 0, 3))
#print("Solutions:", integral)

# -1_integral_1(-sqrt(1-y²)_integral_sqrt(1+y²)(24x_integral_1(1 dz) dx) dy)
x, y, z = sp.symbols('x'), sp.symbols('y'), sp.symbols('z')
integral = sp.integrate(1, (z, 24*x, 1), (x, -sp.sqrt(1-y**2), sp.sqrt(1+y**2)), (y, -1, 1))
print("Solutions:", integral)
