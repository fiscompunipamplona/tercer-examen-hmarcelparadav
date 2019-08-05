from numpy import array, linspace
from math import sin, cos, pi
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint

from vpython import sphere, scene, vector, color, arrow, text, sleep

arrow_size = 0.1

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.02 #Radio de la esfera

def func (conds, t, q, b, m):#Función que devuelve valores de theta y omega, recibe 4 cosas y devuelve un arreglo
    dx = conds[1] #Posición 1 del arreglo en la línea 28 (dthe\dt=omega)
    dv1 = (q/m)*conds[2]*b
    dy=conds[0]
    dv2 = -(q/m)*conds[3]*b
    dz=conds[4]
    dv3=conds[5]#Posición 0 del arrel de la línea 28 
    return array([dx, dv1, dy, dv2, dz, dv3],float)


q = 1#
m = 1
b=1
#thes = 45*pi/180.#valores iniciales
#omes = 0.
vx=10
vy=6
vz=2
x=0
y=0
z=0
initcond = array([vx, vy, x, y, vz, z], float) #Aarreglo de onciones iniciales

n_steps = 1000 #Número de pasos
t_start = 0. #Tiempo inicial
t_final = 15. #Tiempo final
t_delta = (t_final - t_start) / n_steps #Paso temporal
t = linspace(t_start, t_final, n_steps) #Arreglo de diferencial de tiempo

solu, outodeint = odeint( func, initcond, t, args = (q, b, m), full_output=True) #Solución de la ecuación diferencial (Parámetros acordes a los definidos en la función) 
#solu tiene la solución de tiempo decuanto vale theta y cuanto vale omega

dxx, vvx, dyy, vvy, dzz, vvz  = solu.T # matríz que tiene n filas por dos columnas devuelve la matríz transpuesta y a cada una de lasvariables de laizquierda le asigna un vector, convierte un arreglo de 2 filas por n columnas, la fla 1 la pasa a theta y la fila 2 a omega
#print(dxx, vvx, dyy, vvy, dzz)
#od información  numérica de coḿo se hizo la ecuación diferencial
#hasta ahi solucion de la ecuacion diferencial
# =====================

scene.range = 0.2 # m #definir el tamaño de la ventana 

xp = 0#l*sin(thes) #coordenadas cartisianas de la esfera, pasade coordenadas porlares a cartesianas, lo msmo para yp y zp 
yp =  0 #-l*cos(thes)# condicion inicial para el angulo theta
zp = 0.

sleeptime = 0.0001 # es el tiempo con que la maquina va a actualizar la posicon de la particula

prtcl = sphere(pos=vector(xp,yp,zp), radius=R, color=color.red) # Define objeto con que se va a trabajar, define la particula que es una esfera, y la poscion inicial de la esfera sonlas coordenas xp, yp y zp,
# A continuació
time_i = 0 #se feine la variable, hasta ahi se tiene la solucion lo que quiere es grafica lo que quiere es cuant, es un contandor que se mueve en el espacio temporal en el que se resolvió la condicion diferencial, la longitud de theta y de omega es la misma que la de ray t y para esa posición se encontró cuanto vale theta y omega
t_run = 0# tiempo en le que se va ejecutando la animación 

#for i in omega:
#    print(i)


while t_run < t_final:#loop while, arraqnca en 0 y tfinal es el tiempo finalpara el que se reolviera la ecuació diferencial, mientras el trun<que el tiempo final sigue corriendo, llega a línea 61 se duerme y no hace nada y luego actualiza la posicó de la partucula, no hace nada durante 0,001 segundos. entra cambia la poscición de la partícula y aumenta el contador de time_i, cambia la poscion y la actualiza, con el tiempo que se le da abajo, el trun y el time_i hacen lo mismo, el nummero maximo que hace tme_i es el numero de pasos, mientras tme:_i sea menor a trun hagalo
    sleep(sleeptime)
    prtcl.pos = vector( xp[time_i], yp[time_i], vvz[time_i])
# la posción time devuelve cuanto vale la poscion x y y    
    t_run += t_delta
    time_i += 1
