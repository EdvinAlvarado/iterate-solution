# x^3 + 5x = 20
# xn1 = (20-5*xn)^(1/3)
def f(x):
	return (20-5*x)**(1/3)

x0 = 2

xn = 0
xn += x0
xn1 = 0
xn1 += f(xn)

i=10
while i>0.001:
	i = abs(xn1 - xn)
	xn = 0
	xn += xn1
	xn1 = 0
	xn1 += f(xn)
	print('xn1 = %f \t i=%f' %(xn1,i))
