num1 = input("Please enter the first  number:")
num2 = input("Please enter the second  number:")
num3 = input("Please enter the third  number:")
num4 = input("Please enter the forth  number:")
x1 = int(num1) 
x2 = int(num2)
y1 = int(num3)
y2 = int(num4)

import matplotlib.pyplot as plt

def main():
    x = [x1,x2]
    y = [y1,y2]
    plt.plot(x,y)
    plt.show()

main()