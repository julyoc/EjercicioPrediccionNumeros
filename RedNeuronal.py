import numpy as np
from numpy.lib.function_base import append

class RedNeuronal:
    def __init__(self, cant_inter, factorApren):
        self.cant_inter = cant_inter
        self.factorApren = factorApren
        pass
    def setValues(self, x, y):
        self.w = np.random.rand(x, y)*0.1 - 0.05
        self.w0 = self.w.copy()

    def sigmoid(self, s):
        return (1/(1+np.exp(-s)))
    
    def Deffsigmoid(self, s):
        return (s*(1-s))

    def forward(self, datox, datoy, l):
        z0=np.dot(datox, self.w)
        z = self.sigmoid(z0)
        err = (z - datoy)*self.Deffsigmoid(z);
        self.err = np.linalg.norm(err)
        self.w += l*err*z 

    def train(self, xData, yData):
        self.setValues(len(xData[0]), len(yData[0]))
        for _ in range(self.cant_inter):
            for i in range(len(xData)):
                self.forward(xData[i], yData[i], self.factorApren)

    def predictProba(self, x):
        z0=np.dot(x, self.w)
        return self.sigmoid(z0)

    def predict(self, x):
        z0 = self.predictProba(x)
        #return np.round(z0)
        return self.rounded(z0)
    
    def rounded(self, x):
        u = x.copy()
        for i, v in enumerate(x):
            for j, vv in enumerate(v):
                if vv >= 0.5:
                    u[i][j] = 1
                    continue
                u[i][j] = 0
        return u
""""
class Perseptron(object):
    
    def __init__(self) -> None:
        super().__init__()
        self.err = 1.0

    def crearpeso(self, x, y):
        return np.random.rand(x, y)*0.1 - 0.05

    def setValues(self, x, y, layers):
        pesos = []
        pesos.append(self.crearpeso(x, layers[0]))
        for i in range(len(layers) - 1):
            pesos.append(self.crearpeso(layers[i], layers[i + 1]))

        pesos.append(self.crearpeso(layers[len(layers) - 1], y))
        self.w = np.array(pesos)
        self.w0 = self.w.copy()
        del pesos

    def sigmoid(self, s):
        return (1/(1+np.exp(-s)))
    
    def Deffsigmoid(self, s):
        return (s*(1-s))

    def forward(self, datoX, itera):
        z0 = np.dot(datoX, self.w[itera])
        z = self.sigmoid(z0)
        return z

    def backward(self, z, datoY, itera, L):
        if itera == len(self.w) - 1:
             self.err = (datoY - z)*self.Deffsigmoid(z)
             self.w[itera] += L*self.err*z
             return
        self.err = np.dot(self.sigmoid(z), self.w[itera].T)*self.err
        er, z1 = self.err.reshape((self.err.shape[0], 1)), z.reshape((z.shape[0],1))
        #print(self.w[itera].shape, '=', self.err.T.shape, 'x', z.T.shape)
        print("i =", itera, "; ", self.w[itera].shape, '=', er.shape, 'x', z1.T.shape)
        #self.w[itera] += np.dot(self.err.T, z.T)*L
        self.w[itera] += np.dot(er, z1.T)*L

    def train(self, Xdata, Ydata, iteracciones: int, layers = [], factorDeAprendizaje = 0.001) -> None:
        self.setValues(len(Xdata[0]), len(Ydata[0]), layers)
        for _ in range(iteracciones):
            for j, value in enumerate(Xdata):
                z = value
                for i in range(len(self.w)):
                    z = self.forward(z, i)
                    self.backward(z, Ydata[j], i, factorDeAprendizaje)

    def predict(self, Xdata):
        ret = Xdata
        for i in range(len(self.w)):
            ret = self.forward(ret, i)
        return ret


x = np.array([[1,1,0,1], [1,0,1,1], [0,1,1,1], [0,1,0,1]])
y = np.array([[1], [1], [0], [0]])
model = Perseptron()
model.train(x, y, 100, [3,2])
ret = model.predict([1,1,0])
print(ret, model.err)
"""

### Test Class
"""
model = RedNeuronal(1000, 0.001)
x = np.array([[1,1,0,1], [1,0,1,1], [0,1,1,1], [0,1,0,1]])
y = np.array([[1], [1], [0], [0]])
model.train(x, y)
print(model.predict([[1,1,0,1]]))
print(model.predictProba([[1,1,0,1]]))
print('pesos iniciales: ', model.w0)
print('pesos calculados: ', model.w)
print('error: ', model.err)
"""