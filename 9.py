import math
N = int(input('Введите натуральное число,которое является наиб-им кол-ом точек на всех костях домино:'))
'''
a = 0
for i in range(N):
    a += math.factorial(N) // (math.factorial(i)*math.factorial(N - i))
    b = a*2
print(b)
'''

a = math.factorial(N+1)
b = a*2
print(b)