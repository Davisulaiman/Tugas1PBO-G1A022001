# fungsi FP
def sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum(numbers[1:])

# pemanggilan fungsi
my_numbers = [1, 2, 3, 4, 5]
print(sum(my_numbers)) # output
