import numpy as np


# x^3 + 5x = 20
# xn1 = (20-5*xn)^(1/3)
def f(x):
	return np.cbrt(20 - 5 * x)


def eq_iterator(init, func):
	# needs to be greater than the tolerance in the while loop
	i = 0.002
	xn = init
	xn1 = func(init)
	while i > 0.0001:
		i = abs(xn1 - xn)
		# print(f"xn1 = {xn1:.4f}\txn = {xn:.4f} \t i = {i:.4f}")
		xn = xn1
		xn1 = func(xn)
	return xn1


x = [n for n in range(-10, 10)]
# If I use a np.array without making it complex type any imaginary number will appear as nan. Use list or make the array complex
x_sol = [eq_iterator(xi, f) for xi in x]

result = zip(x, x_sol)
for r in result:
	print(f"{r[0]}\t{r[1]:.4f}")

# you can see where imaginary numbers will happen where we take the function to be y^3 + 5x = 20
# Any time x > 4 or y > 4 imaginary numbers appear. Whic sems to be related to the constants 20/5=4
# FIXED due to computing rounding 1/3 when used in **(1/3) it will never give the real part of the root. used np.cbrt() to solve it.
# print(eq_iterator(-8.9, f))
# print(eq_iterator(-5, f))
