import numpy
import matplotlib.pyplot as plt

def f(x):
	return numpy.exp(x)

if __name__ == "__main__":
	step = 0.001
	x = numpy.arange(0, 3, step)
	y = f(x)

	y_euler = [1]
	number_points_to_compute = len(x) - 1
	for index in range(0, number_points_to_compute):
		next_value = y_euler[index] * step + y_euler[index]
		y_euler.append(next_value)


	plt.figure(figsize=(15, 6))
	plt.plot(x, y, ":")
	plt.plot(x, y_euler, color="red")
	plt.show()