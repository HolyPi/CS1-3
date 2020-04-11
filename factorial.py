def iterative_factorial(n):
    #you substract 1 each time
    #3, 3*2*1
    #1*2*3
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def recursive_factorial(n):
    #3! 3*2*1
    #3! 3*2!
    #base case, stops the recursion
    if n == 1:
        return 1
        #recursive case
        else: 
            result = recursive_factorial(n-1)
            return result * n