#creating a function to calculate factorial
def factorial(n):
    result=1
#for loop range starting from 1 upto 5 (does not include the stop value 6)
    for i in range(1, n+1):
#new result is the previous result multiplied by n+1
        result= result*i
#returns the factorial
    return result
#displays the factorial of 5
print(factorial(5))
        