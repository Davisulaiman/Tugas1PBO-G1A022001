# fungsi FP
def sum_of_squares(n):
    return sum(map(lambda x: x**2, range(1, n+1)))

# pemanggilan fungsi
print(sum_of_squares(4)) # output: 30
