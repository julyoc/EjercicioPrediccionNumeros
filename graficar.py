import matplotlib.pyplot as plt
import numpy as np

def graficar(alldata):
    inp = input("Ingrese la posicion del numero [0, 500]: ")
    plt.spy(np.reshape(alldata[int(inp)], [30, 20]))
    plt.show()

def graficar(alldata, inp):
    plt.spy(np.reshape(alldata[int(inp)], [30, 20]))
    plt.show()

def graficarDT(dt):
    plt.spy(np.reshape(dt, [30, 20]))
    plt.show()

def graficarGrupo100(alldata):
    inp = input("Ingrese el numero de grupo(libro de exel) a graficar: ")
    fig, axs = plt.subplots(10, 10)
    fig.set_size_inches(20, 30)
    k = int(inp)*100 -100
    for i in range(10):
        for j in range(10):
            axs[j, i].spy(np.reshape(alldata[k], [30, 20]))
            k += 1
    plt.show()

def graficarGrupo100(alldata, inp):
    fig, axs = plt.subplots(10, 10)
    fig.set_size_inches(20, 30)
    k = int(inp)*100 -100
    for i in range(10):
        for j in range(10):
            #print((j, i))
            axs[j, i].spy(np.reshape(alldata[k], [30, 20]))
            k += 1
    plt.show()

def graficarPredData(alldata):
    fig, axs = plt.subplots(4, 10)
    fig.set_size_inches(20, 30)
    k = 0
    for i in range(10):
        for j in range(4):
            axs[j, i].spy(np.reshape(alldata[k], [30, 20]))
            k += 1
    plt.show()