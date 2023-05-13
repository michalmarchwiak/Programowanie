import numpy as np
from scipy.integrate import odeint
import matplotlib;
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sys

def seir(y, t, N, beta, sigma, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

N, S0, E0, I0, R0, beta, sigma, gamma = map(float, sys.argv[1:])
t = np.linspace(0, 100, 1000)
y0 = [S0, E0, I0, R0]
res = odeint(seir, y0, t, args=(N, beta, sigma, gamma))

S, E, I, R = res.T

plt.plot(t, S, label='Susceptible')
plt.plot(t, E, label='Exposed')
plt.plot(t, I, label='Infected')
plt.plot(t, R, label='Recovered')
plt.legend()
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.show()