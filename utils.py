def factorial(a):
	sulution = 1
	for number in range(a):
		sulution *= a
	return solution


def IsPrime(a):
	for i in range (2, int(a ** (0.5)) + 1):
		if a % i == 0:
			return False
	return True