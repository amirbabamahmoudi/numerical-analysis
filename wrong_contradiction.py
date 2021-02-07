from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
import simpy
import math

def converge_roots(n):     # tabe baraye yafatan noqat ham geraee k haman node haaye chebishof hastand
    roots = []
    for i in range(1 , n+1):
        xi = math.cos((2*i-1)/(2*n)*math.pi)
        roots.append(xi)
    return np.asanyarray(roots , dtype= np.float16)

x = np.linspace(-1, 1, num= 200, endpoint=True)
y = 1 / (1+(x**2)*25)

f = interp1d(x, y)

x1 = np.linspace(-1, 1, num= 5, endpoint=True)   # az x1 ta x4  noqat motesavi ol fasele k vaagaraa hastand
y1 = f(x1) 

x2 = np.linspace(-1, 1, num= 10, endpoint=True)
y2 = f(x2)

x3 = np.linspace(-1, 1, num= 15, endpoint=True)
y3 = f(x3)

x4 = np.linspace(-1, 1, num= 20, endpoint=True)
y4 = f(x4)

x5 = converge_roots(5)   #n  az x5 ta x8 node haaye chebishof k hamgera mikonand daroon yaab ro 
y5 = f(x5)

x6 = converge_roots(10)
y6 = f(x6)

x7 = converge_roots(15)
y7 = f(x7)

x8 = converge_roots(20)
y8 = f(x8)

p1 = np.polyfit(x1 , y1 , len(x1) - 1)
p2 = np.polyfit(x2 , y2 , len(x2) - 1)
p3 = np.polyfit(x3 , y3 , len(x3) - 1)
p4 = np.polyfit(x4 , y4 , len(x4) - 1)
p5 = np.polyfit(x5 , y5 , len(x5) - 1)
p6 = np.polyfit(x6 , y6 , len(x6) - 1)
p7 = np.polyfit(x7 , y7 , len(x7) - 1)
p8 = np.polyfit(x8 , y8 , len(x8) - 1)


xvar  = np.linspace(1 , -1)
yvar1 = np.polyval(p1 , xvar)
yvar2 = np.polyval(p2 , xvar)
yvar3 = np.polyval(p3 , xvar)
yvar4 = np.polyval(p4 , xvar)
yvar5 = np.polyval(p5 , xvar)
yvar6 = np.polyval(p6 , xvar)
yvar7 = np.polyval(p7 , xvar)
yvar8 = np.polyval(p8 , xvar)




plt.plot(xvar , yvar5 , '--' ,xvar , yvar6 , '--' ,  xvar , yvar7 , '--' ,xvar , yvar8 , '--' ,x , f(x) , '-')    # nemoodar haaye ham gerayii  
plt.legend(['ph5', 'ph10', 'ph15','ph20','function'], loc='best')
#plt.plot(xvar , yvar1 , '--' ,xvar , yvar2,'--',xvar , yvar3,'--',xvar , yvar4,'--'   , x , f(x) , '-')  #nemoodar haaye vagaree
#plt.legend(['pv5', 'pv10', 'pv15','pv20','function'], loc='best')