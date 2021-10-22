import numpy as np
import matplotlib.pyplot as plt

radianes = []
radio = []

angulo = [0,22.5,45,67.5,90,112.5,135,157.5,180,202.5,225,247.5,270,292.5,315,337.5,0]

for an in angulo: 
    radianes.append( an * np.pi / 180 )

dbm = [-62,-61,-52.5,-50,-43,-40,-39,-38,-41.2,-45,-50.5,-66,-66,-65.5,-61,-54.5,-62]

#formula de friis
Pt = 0
Gt = 12 #bdi
Gr = 10.24 #db
Gt = [] #dbm
L = 20 * np.log( 4 * np.pi * 2.57 / 0.125) #dbm

#aplicar formula de friis a los valores de potencia transmitida
for Pr in dbm:
    Gt.append(Pr - Pt - Gr + L)

#normalizar valores
for b in Gt: 
    radio.append((b - Gt[0],2))

#plot
ax = plt.figure().add_subplot()
ax.plot(angulo,radio)
plt.xlim(0,360)
plt.title("Diagrama de radiación")
plt.xlabel("Angulos(Grados)")
plt.ylabel("Potencia(dBi)")
plt.show()

ax = plt.figure().add_subplot(111, projection="polar")
ax.plot(radianes,radio)
ax.set_rlabel_position(135)
ax.set_theta_offset(np.pi/2)
plt.title("Diagrama de radiación")
plt.xlabel("Radianes/Ganancia(dB)")
plt.show()

print(Gt)
for i in range(0,len(radio)):
    print("(" + str(round(radianes[i],2)) + "," + str(radio[i]) + ")\n")
