import math
 
# Definimos los tipos de monedas
monedas=[500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]

# Definimos la cantidad de monedas que disponemos de cada tipo
cantidad=[9999999, 99999999, 99999999, 9999999999, 99999999, 9999999, 99999999, 99999999, 9999999, 999999999, 9999999, 99999999, 9999999, 9999999, 999999999]

# Definimos una lista vacia que contendra las cantidades de cada moneda
cambio=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

importe=12056.83
 
print("Cantidad a devolver: {:.2f}".format(importe))
 
for i in range(len(monedas)):
    if importe>monedas[i]:
        cantidadMoneda=math.floor(importe/monedas[i])
        if cantidadMoneda<=cantidad[i]:
            cambio[i]=cantidadMoneda
        else:
            cambio[i]=cantidad[i]
        importe-=(cambio[i]*monedas[i])
 
for i in range(len(monedas)):
    if cambio[i]>0 and monedas[i]>=5:
        print("Hay {} billetes de {}".format(cambio[i], monedas[i]))
    elif cambio[i]>0:
        print("Hay {} monedas de {}".format(cambio[i], monedas[i]))

print(cambio)
'''
import pandas as pd

df = pd.read_csv("fraud_log.csv")
df2 = df[df["isFraud"]==1]
df2.info()
amountTotal = df2["amount"].sum()
print(amountTotal)'''