def sum_of_digits(n):
#base case to terminate recursion
    if n==0:
        return 0
    else:
#adding last digit of the number to the total digit sum
        return (n % 10) + sum_of_digits(n//10)
n = 12345
print(sum_of_digits(n))