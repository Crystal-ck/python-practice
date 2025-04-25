def factorial(n):
#Base case
    if n==1: 
        return 1
    else:
#multiplies n by n-1 until n==1 
      return n*factorial(n-1)

print(factorial(5))