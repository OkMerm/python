import math
import matplotlib.pyplot as plt
import csv

x_min = -10
x_max = 10
step = 0.1
A = 9.66459
x = x_min
x_arr = []
y_arr = []

while x <= x_max:
    y = - abs(math.sin(x) * math.cos(A) * math.exp(abs(1-((x ** 2 + A ** 2) ** 0.5) / math.pi)))
    x_arr.append(x)
    y_arr.append(y)
    print(x, ' ', y, ' ')
    x = x + step
    
if not os.path.isdir("results"):
     os.mkdir("results")

with open("./results/data.cvs", "w") as file:
    writer = csv.writer(file)
    for i in range(0, len(x_arr)):
        writer.writerow([str(i + 1), str(x_arr[i]), str(y_arr[i])])    

plt.plot(x_arr, y_arr)
plt.title('Задача 1')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
