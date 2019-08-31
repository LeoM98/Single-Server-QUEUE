import pandas as pd
import numpy as np
import re

vector = [] #Contenedor de ambas columnas
an = [] #Tiempos de llegada
sn = [] #Tiempo de servicio

def Archivo ():

    data = open ('data.txt', 'r') #Apertura del archivo
    for i in data.readlines(): #Recorrera todos los valores del archivo
        vector.append(re.findall(r'[\d]+[.][\d]+',i))#Identificar todo aquello que sea numero
    return np.array(vector,dtype=float)

vector = Archivo() #Se guarda el procesado de la función
align = pd.DataFrame (vector) #Tabula los datos a columnas y filas

#Asignación de columnas
an = vector[:,0]
sn = vector[:,1]
n = len (an) #Cantidad de datos en total


Co = 0.0 #departure initial
i = 0 #jobs
di = [] #delay time
Ci = []

#Algoritmo 1.2.1
while (i<n):

    if (an[i] < Co):
        var = Co-an[i]
        di.append(var)

    else:
        var = 0.0
        di.append(var)
    
    Ci.append(an[i]+di[i]+sn[i])
    Co = Ci[i]

    i = i+1

#Promedios estadisticos de trabajos

av_a_ai = an[n-1]/n
av_di = sum(di)/n
av_si = sum(sn)/n
av_w = (av_si+av_di)

av_a_rate = 1/av_a_ai #Tasa de llegada
av_s_rate = 1/av_si #Tasa de servicio

#Promedios estadisticos de tiempo

q = (n/Co)*sum(di)
x = (n/Co)*sum(sn)
l = (q+x)

print ("\n\t\t\t***PROMEDIOS ESTADISTICOS DE TRABAJO***\n")

print("Average interarrival: {0}\nAverage Delay: {1}\nAverage service time: {2}".format(av_a_ai,av_di,av_si))
print("Wait in node:{0}\nArrival rate {1}\nService Rate: {2}".format(av_w,av_a_rate,av_s_rate))

print ("\n\t\t\t***PROMEDIOS ESTADISTICOS DE TIEMPO***\n")
print("Number of jobs in the queue: {0}\nNumber of jobs in service: {1}\nNumber of jobs in the service node: {2}".format(q,x,l))