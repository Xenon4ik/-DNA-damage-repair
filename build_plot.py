import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import os

# cur_dir=os.getcwd()
# # Указываем путь к директории
# directory = f'{cur_dir}'

my_path = os.path.dirname(os.path.abspath(__file__)) # Figures out the absolute path for you in case your working directory moves around.
my_file = 'static\plot.png'

def Plot(D):
    def F(s,t):
        dx = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        k = [7.55e-3,1.335e-4,3.08,0.05,0.625,0.04,0.0022,0.075,0.78,1.51e9]
        K = [22432,81933,327731,757576,3937,169192,98485,7183]
        A = [123000,300000,50000,50000,50000,5000,500000]
        dx[0] = 0.001-(k[0]/(s[0]+K[0]))*A[0]*s[0]
        dx[1] = 0.120+(k[0]/(s[0]+K[0]))*A[0]*s[0]-k[1]*s[1]-(k[2]/(s[1]+K[1]))*A[1]*s[1]
        dx[2] = k[1]*s[1]-(k[3]/(s[2]+K[2]))*A[1]*s[2]-(k[6]/(s[2]+K[5]))*A[3]*s[2]
        dx[3] =(k[3]/(s[2]+K[2]))*A[1]*s[2]-(k[4]/(s[3]+K[3]))*A[2]*s[3]
        dx[4] =(k[4]/(s[3]+K[3]))*A[2]*s[3]-(k[5]/(s[4]+K[4]))*A[5]*s[4]
        dx[5] =(k[2]/(s[1]+K[1]))*A[1]*s[1]-(k[2]/(s[5]+K[1]))*A[2]*s[5] - (k[6]/(s[5]+K[5]))*A[3]*s[5]
        dx[6] =(k[2]/(s[5]+K[1]))*A[2]*s[5]-k[7]*s[6]
        dx[7] = k[7]*s[6]-(k[5]/(s[7]+K[4]))*A[5]*s[7]
        dx[8] =(k[6]/(s[2]+K[5]))*A[3]*s[2]+(k[6]/(s[5]+K[5]))*A[3]*s[5] - (k[8]/(s[8]+K[6]))*A[4]*s[8]
        dx[9] =(k[8]/(s[8]+K[6]))*A[4]*s[8]-(k[5]/(s[9]+K[4]))*A[5]*s[9]
        dx[10]= k[5]*(s[4]/(s[4]+K[4])+s[7]/(s[7]+K[4])+s[9]/(s[9]+K[4]))
        dx[11]=-(k[9]/(s[11]+K[7]))*A[6]*s[11]
        dx[12]= (k[9]/(s[11]+K[7]))*A[6]*s[11]-(k[3]/(s[12]+K[2]))*A[1]*s[12]
        return dx
    T = 150
    # Время в секундах
    t = np.linspace(0,T,151) # Шаг по времени
    s0= [1500*D,0,0,0,0,0,0,0,0,0,0,400*D,0] # Начальные условия
    x=odeint(F,s0,t)
    # for i in range(0,151):
    #  # Вывод данных
    #   print('{0:6.3f} {1:6.3e} {2:6.3e}'.format(t[i], x[i,0]+x[i,1],x[i,3]+x[i,5]+x[i,11]+x[i,12]))
    fig, ax = plt.subplots(1)
    plt.plot(t,x[:,0]+x[:,1],'r-',linewidth=3.0,label="ПО")
    plt.plot(t,x[:,3]+x[:,5]+x[:,11]+x[:,12],'b-',linewidth=3.0,label="ОР")
    #начальное число ПО 8250, ОР 2200. тогда после восстановления на 50% останется  4125 ПО и 1100 ОР это 21с и 17с соответсвенно.
    # ax.scatter(17,1100)
    # ax.scatter(21,4125)
    plt.xlabel("Время, сек.")
    plt.ylabel("Число повреждений, мол./кл.")
    plt.legend()
    if os.path.exists(os.path.join(my_path, my_file)):
        os.remove(os.path.join(my_path, my_file))
    fig.savefig(os.path.join(my_path, my_file))    