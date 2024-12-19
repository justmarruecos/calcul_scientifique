import numpy
import matplotlib.pyplot as plt
from config_file import *

def f(x):
	return x**2 - 8 * numpy.log(x)

def g(x):
	return x**3 - 3



def solve_equation(f, left, right, precision=10**(-3)) :
	while right - left >= precision:
		middle = (right + left) / 2

		if f(middle) == 0:                              
			break

		elif f(left) * f(middle) < 0 :
			right = middle

		elif f(right) * f(middle) < 0:
			left = middle
	return middle


def plot_function(f, start, end, step=0.01):
	x = numpy.arange(start, end, step)
	y = f(x)

	plt.figure(figsize=(LENGTH, HEIGHT))
	plt.plot(x, y, "-", color="orange")
	plt.show()


if __name__ == "__main__":
	plot_function(f, start=0.1, end=10, step=0.01)
	# middle = solve_equation(f, left=1, right=2)
	# print(middle)
	# print(g(middle))