import math
import os
import wget
import numpy as np
import scipy
import matplotlib.pyplot as plt
import csv

variant = 8
url = 'https://jenyay.net/uploads/Student/Modelling/task_02_01.txt'
f = []
dx = 1_000_000

if (os.path.exists('data.txt') == 0):
    wget.download(url, r'data.txt')

with open ('data.txt', 'r') as data:
    lines = data.readlines()
arr = lines[variant - 1].split(";")

D = float(arr[0].split('=')[1])
fmin = float(arr[1].replace(' fmin=', ''))
fmax = float(arr[2].replace(' fmax=', ''))
f = np.arange(fmin, fmax, dx)
Lambda = scipy.constants.c / f
r = D / 2 
k = 2 * math.pi / Lambda

def hn(n, x): return scipy.special.spherical_jn(n, x) + 1j * scipy.special.spherical_yn(n, x)
def bn(n, x): return (x * scipy.special.spherical_jn(n - 1, x) - n * scipy.special.spherical_jn(n, x)) / (x * hn(n - 1, x) - n * hn(n, x))
def an(n, x): return scipy.special.spherical_jn(n, x) / hn(n, x)

arr_sum = [((-1) ** n) * (n+0.5) * (bn(n, k * r) - an(n, k * r)) for n in range(1, 20)]
sum = np.sum(arr_sum, axis=0)
sigma = (Lambda ** 2) / math.pi * abs(sum) ** 2

with open("results/data2.cvs", "w") as file:
    writer = csv.writer(file)
    for i in range(0, len(f)):
        writer.writerow([i + 1, f[i], sigma[i]])

plt.plot(f / 10e6, sigma)
plt.xlabel("f, МГц")
plt.ylabel("sigma, м^2")
plt.title('Задание 2')
plt.grid()
plt.show()
