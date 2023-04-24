# function FP
import multiprocessing

def square(x):
    return x * x

# membuat pool dengan jumlah process 4
pool = multiprocessing.Pool(processes=4)

# memproses data secara konkuren dengan fungsi square
results = pool.map(square, [1, 2, 3, 4, 5])

# menggabungkan hasil
print(results) # output: [1, 4, 9, 16, 25]
