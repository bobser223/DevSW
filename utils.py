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
    
    
def IsPower5(n):
    if n%5!=0:
        return False
    while n%5==0:
        n=n/5
    if n%5!=0 and n!=1:
        return False
    else:
        return True
        
def IsPower2(n):
    if n%2!=0:
        return False
    while n%2==0:
        n=n/2
    if n%2!=0 and n!=1:
        return False
    else:
        return True
