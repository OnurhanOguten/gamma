"""deneme.py — çift Fibonacci sayıları"""

def even_fib_upto(limit=1000):
	"""Limit'e kadar olan çift Fibonacci sayılarını liste halinde döndürür."""
	evens = []
	a, b = 0, 1
	while a <= limit:
		if a != 0 and a % 2 == 0:
			evens.append(a)
		a, b = b, a + b
	return evens


if __name__ == "__main__":
	print(even_fib_upto(1000))

