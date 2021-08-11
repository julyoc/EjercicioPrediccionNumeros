import matplotlib.pyplot as plt
import numpy as np
def generateYData() -> list: 
    x = []
    for _ in range(5):
        for j in range(10):
            for k in range(10):
                if j == 0:
                    x.append([1,0,0,0,0,0,0,0,0,0])
                if j == 1:
                    x.append([0,1,0,0,0,0,0,0,0,0])
                if j == 2:
                    x.append([0,0,1,0,0,0,0,0,0,0])
                if j == 3:
                    x.append([0,0,0,1,0,0,0,0,0,0])
                if j == 4:
                    x.append([0,0,0,0,1,0,0,0,0,0])
                if j == 5:
                    x.append([0,0,0,0,0,1,0,0,0,0])
                if j == 6:
                    x.append([0,0,0,0,0,0,1,0,0,0])
                if j == 7:
                    x.append([0,0,0,0,0,0,0,1,0,0])
                if j == 8:
                    x.append([0,0,0,0,0,0,0,0,1,0])
                if j == 9:
                    x.append([0,0,0,0,0,0,0,0,0,1])
    return x

def predictGrafData(dt, resdt):
    plt.spy(np.reshape(dt, [30, 20]))
    if resdt == [1,0,0,0,0,0,0,0,0,0]:
        plt.title("el numero es un '0'.")
    elif resdt == [0,1,0,0,0,0,0,0,0,0]:
        plt.title("el numero es un '1'.")
    elif resdt == [0,0,1,0,0,0,0,0,0,0]:
        plt.title("el numero es un '2'.")
    elif resdt == [0,0,0,1,0,0,0,0,0,0]:
        plt.title("el numero es un '3'.")
    elif resdt == [0,0,0,0,1,0,0,0,0,0]:
        plt.title("el numero es un '4'.")
    elif resdt == [0,0,0,0,0,1,0,0,0,0]:
        plt.title("el numero es un '5'.")
    elif resdt == [0,0,0,0,0,0,1,0,0,0]:
        plt.title("el numero es un '6'.")
    elif resdt == [0,0,0,0,0,0,0,1,0,0]:
        plt.title("el numero es un '7'.")
    elif resdt == [0,0,0,0,0,0,0,0,1,0]:
        plt.title("el numero es un '8'.")
    elif resdt == [0,0,0,0,0,0,0,0,0,1]:
        plt.title("el numero es un '9'.")
    else:
        plt.title("No se reconoce el numero.")
    plt.show()

def predictGrafDataProba(dt, resdt):
    index = 0
    i = 0
    while i < len(resdt)-1:
        if resdt[i] > resdt[i+1]:
            index = i
        elif resdt[i] == resdt[i+1]:
            index = -1
        else:
            index = i+1
    plt.spy(np.reshape(dt, [30, 20]))
    if index == -1:
        plt.title("No se reconoce el numero.")
        return;
    plt.title("el numero es un '" + index +"'.")