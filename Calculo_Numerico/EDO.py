import math


def fxy(x, y):
    return -2*x - y


def Exato(x):
    return -3*math.exp(-x) - 2*x + 2


def Euler(a, b, h, y0):
    N = int((b - a)/h)
    x = [a + i*h for i in range(N)]
    y = [y0]*N
    for i in range(N-1):
        y[i+1] = y[i] + h*fxy(x[i], y[i])
    return y


def Runge_Kutta(a, b, h, y0):
    N = int((b - a)/h)
    x = [(a + h*i) for i in range(N)]
    d = [1, 2, 1, 3]
    K = [0, 0, 0, 0]
    y = [y0]*N
    for i in range(N-1):
        K[0] = h*fxy(x[i], y[i])
        K[1] = h*fxy(x[i] + h/2, y[i] + K[0]/2)
        K[2] = h*fxy(x[i] + h/2, y[i] + K[1]/2)
        K[3] = h*fxy(x[i] + h, y[i]+K[2])
        y[i+1] = y[i] + (K[0] + 2*K[1] + 2*K[2] + K[3])/6
    return y


a, b, h, y0 = 0, 0.5, 0.1, -1
N = int((b - a)/h)
euler = Euler(a, b, h, y0)
runge_kutta = Runge_Kutta(a, b, h, y0)
exato = [Exato(a + i*h) for i in range(N)]
erro_rk = [abs(runge_kutta[i] - exato[i]) for i in range(N)]
erro_eul = [abs(euler[i] - exato[i]) for i in range(N)]
print("Euler =", euler, '\n')
print("Runge Kuta =", runge_kutta, '\n\n')
print("exato =", exato, '\n')
print("erro Euler =", erro_eul, '\n')
print("erro R-K =", erro_rk)
