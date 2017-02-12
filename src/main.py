# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(-2*np.pi, 2*np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y, 'g-')
    plt.show()

main()
