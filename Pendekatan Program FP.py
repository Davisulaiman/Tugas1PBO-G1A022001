# fungsi FP
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# pemanggilan fungsi
print(factorial(5)) # output: 120
