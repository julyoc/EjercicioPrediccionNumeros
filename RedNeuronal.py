import numpy as np

class RedNeuronal:
    def __init__(self):
        pass
    def setValues(self, x, y):
        self.w = (np.random.randn(x, y)/2) - 0.4999
        self.w0 = self.w

    def sigmoid(self, s):
        return (1/(1+np.exp(-s)))
    
    def Deffsigmoid(self, s):
        return (s*(1-s))

    def forward(self, datox, datoy, l):
        z0=np.dot(datox, self.w)
        z = self.sigmoid(z0)
        err = (z - datoy)*self.Deffsigmoid(z);
        self.err = err
        self.w += l*err*z 

    def train(self, cant_inter, factorApren, xData, yData):
        self.setValues(len(xData[0]), len(yData[0]))
        for _ in range(cant_inter):
            for i in range(len(xData)):
                self.forward(xData[i], yData[i], factorApren)

    def predict(self, x):
        z0=np.dot(x, self.w)
        return self.sigmoid(z0)