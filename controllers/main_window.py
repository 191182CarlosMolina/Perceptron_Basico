#import random
#import math
import sys
#from itertools import combinations
#from PySide2 import QWidgets, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5 import QtWidgets, uic
import numpy as np
import math as m
import matplotlib.pyplot as plt
import os
import decimal
#from shutil import rmtree
import pandas as pd
#import time

class Perceptron ():

    def __init__(self,aprendizaje, umbral):
        self.aprendizaje = aprendizaje
        self.umbral = umbral
        self.pesos = []
        self.error = 0
        self.X = []
        self.Y = []
        self.ids = []

        #self.pushButtonEjecutar.clicked.connect(self.inicializacion_alg)

    def leer_Archivo(self,archivo):
        df = pd.read_csv(archivo)
        x=df.iloc[:,1:4].values
        y = df.iloc[:, 4].values
        ids = df.iloc[: , 0].values
        x = self.bias(x)
        self.ids = ids
        self.X = x
        self.Y = y
        self.pesos = np.random.rand(len(x[0]))
        #print("Pesos:",self.pesos)

    def leer_Archivo2(self):
        df = pd.read_csv('191182.csv')
        x=df.iloc[:,1:4].values
        y = df.iloc[:, 4].values
        ids = df.iloc[: , 0].values
        x = self.bias(x)
        self.ids = ids
        self.X = x
        self.Y = y
        self.pesos = np.random.rand(len(x[0]))
        #print("Pesos:",self.pesos)

    def bias(self, x):
        x_bias = []
        for i in range(len(x)):
            x_bias.append([1,x[i][0], x[i][1],x[i][2]])
        #print("X_bias:",x_bias)
        return x_bias

    def calculo_u(self):
        transpuestaW = np.transpose(self.pesos)
        u = np.linalg.multi_dot([self.X, transpuestaW])
        return u

    def funcion_activacion(self, u):
        return u
    
    def cal_error(self,ycal):
        error = []
        for i in range(len(ycal)):
            error.append(self.Y[i]-ycal[i])
        return error

    def delta_W(self,e):
        ret = np.transpose(e)
        for i in range(len(self.pesos)):
            dw = np.linalg.multi_dot([ret,self.X])*self.aprendizaje
        return dw
    
    def nv_W(self,deltaW):
        nueva_W = self.pesos + deltaW
        self.pesos = nueva_W
        
        return nueva_W

    def cal_error2(self,error):

        #PARA EVITAR DESBORDE CON DECIMAL
        # e = decimal.Decimal(0)
        # n = len(error)
        # for i in range(len(error)):
        #     e = e + decimal.Decimal(error[i])**2
        # mse = e / n
        # rmse = m.sqrt(mse)
        # return rmse

        #PARA EVITAR EL DESBORDE DEL VALOR
        # e = 0
        # n = len(error)
        # error = np.clip(error, -1e10, 1e10)
        # for i in range(len(error)):
        #     e = e + error[i]**2
        # mse = e / n
        # rmse = m.sqrt(mse)
        # return rmse

        #LA COMPLETA SEGUN
        e = 0
        n = len(error)
        for i in range(len(error)):
            e = e + error[i]**2
        mse = e / n
        rmse = m.sqrt(mse)
        return rmse
        
        #LA NORMALITA
        # e = 0
        # for i in range(len(error)):
        #     e = e + error[i]**2
        # return m.sqrt(e)


    
def inicializacion_alg2():
    bandera=True
    archivo = "203411.csv"
    try:
        aprendizaje = float(window.lineEditTAprendizaje.text())
        umbral = float(window.lineEditEPermisible.text())
    except:
        bandera = False

    if bandera:
        window.labelMensaje.setText("Generando Graficas 203411")
        window.labelMensaje.setStyleSheet("color: Black ; font-size: 10pt")
        window.labelMensaje.repaint()
        #print(aprendizaje)
        #print(umbral)
        algoritmo(aprendizaje, umbral,archivo)
    
def inicializacion_alg():
    bandera=True
    archivo = "191182.csv"
    try:
        aprendizaje = float(window.lineEditTAprendizaje.text())
        umbral = float(window.lineEditEPermisible.text())
    except:
        bandera = False

    if bandera:
        window.labelMensaje.setText("Generando Graficas 191182")
        window.labelMensaje.setStyleSheet("color: Black ; font-size: 10pt")
        window.labelMensaje.repaint()
        algoritmo(aprendizaje, umbral,archivo)
    
def algoritmo(aprendizaje, umbral,archivo):
    perceptron = Perceptron(aprendizaje, umbral)
    a =str(aprendizaje)
    errores=[]
    pesosSesgo= []
    pesosX1 = []
    pesosX2 = []
    pesosX3 = []
    perceptron.leer_Archivo(archivo)
    e = 2
    i = 0
    while e > perceptron.umbral:
        u = perceptron.calculo_u()
        ycal = perceptron.funcion_activacion(u)
        error = perceptron.cal_error(ycal)
        #print("Error antes de deltaW", error)
        graficar_error2(error, i)
        deltaW = perceptron.delta_W(error)
        pesosSesgo.append(perceptron.pesos[0])
        pesosX1.append(perceptron.pesos[1])
        pesosX2.append(perceptron.pesos[2])
        pesosX3.append(perceptron.pesos[3])
        perceptron.nv_W(deltaW)
        e = perceptron.cal_error2(error)

        #print("e:",e)
        #print("deltaW",deltaW)
        #print("Pesos",perceptron.pesos)
        
        errores.append(e)
        i += 1     

    #print("errores:",errores)
    #print('Vueltas t:',i)
    graficar_error(errores, a)
    graficar_yc(ycal, perceptron)
    graficar_pesos(pesosSesgo,pesosX1,pesosX2,pesosX3)
    window.labelMensaje.setText("Graficas Generadas ")
    window.labelMensaje.setStyleSheet("color: Green ; font-size: 10pt")
    window.labelMensaje.update()
    
    
        
def graficar_error(errores, a):
    plt.title("Evoluci??n de la magnitud del error")
    plt.xlabel("Iteracion")
    plt.ylabel("Valor del error")
    plt.plot(errores, label="TA:"+a,linestyle="-")
    plt.legend()
    os.makedirs("assets\Graficas\Error", exist_ok=True)
    plt.savefig("assets\Graficas\Error\Error.png")
    plt.close()

def graficar_error2(error,i):
    plt.title("Error observador:"+str(i))
    plt.xlabel("Identificador")
    plt.ylabel("Valor del error")
    plt.plot(error, label="Error Observado:",linestyle="-")
    plt.legend()
    os.makedirs("assets\Graficas\ErrorObservado", exist_ok=True)
    plt.savefig("assets\Graficas\ErrorObservado\ErrorObservado"+str(i)+".png")
    plt.close()

def graficar_pesos(pesosSesgo,pesosX1,pesosX2,pesosX3):
    plt.title("Evoluci??n de los pesos")
    plt.xlabel("Iteracion")
    plt.ylabel("Valor")
    plt.plot(pesosSesgo, label="Sesgo:",linestyle="-")
    plt.plot(pesosX1, label="X1:",linestyle="-"  )
    plt.plot(pesosX2, label="X2:",linestyle="-"  )
    plt.plot(pesosX3, label="X3:",linestyle="-" )
    plt.legend()
    os.makedirs("assets\Graficas\Pesos", exist_ok=True)
    plt.savefig("assets\Graficas\Pesos\Pesos.png")
    plt.close()

def graficar_yc(ycal,perceptron):
    plt.xlabel("Identificador")
    plt.ylabel("Valores Yc y Yd")
    plt.plot(ycal, label="Yc", color="blue",linestyle="-")
    plt.plot(perceptron.Y, label="Yd", color="green",linestyle="--")
    plt.legend()
    os.makedirs("assets\Graficas\Ycalculada", exist_ok=True)
    plt.savefig("assets\Graficas\Ycalculada\Ycalculada.png")
    plt.close()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = uic.loadUi("ui_files/main_window.ui")
    window.show()
    valueAprendizaje = "0.00000001"
    valueError = "1"
    window.lineEditTAprendizaje.setText(valueAprendizaje)
    window.lineEditEPermisible.setText(valueError)
    window.pushButtonEjecutar.clicked.connect(inicializacion_alg)
    window.pushButtonEjecutar2.clicked.connect(inicializacion_alg2)
    sys.exit(app.exec())
