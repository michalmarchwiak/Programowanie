from zadanie1 import seir
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-N', dest="N", type=int, default=1000)
    parser.add_argument('-S0', dest="S0", type=int, default=999)
    parser.add_argument('-E0', dest="E0", type=int, default=1)
    parser.add_argument('-I0', dest="I0", type=int, default=0)
    parser.add_argument('-R0', dest="R0", type=int, default=0)
    parser.add_argument('-beta', dest="beta", type=float, default=1.34)
    parser.add_argument('-sigma', dest="sigma", type=float, default=0.19)
    parser.add_argument('-gamma', dest="gamma", type=float, default=0.34)
    args = parser.parse_args()

    if args.S0 is None:
        args.S0 = args.N - args.I0 - args.R0
    if args.E0 is None:
        args.E0 = 0

    return args


def main():
    args = parse_args()

    y0 = args.S0, args.E0, args.I0, args.R0

    t = np.linspace(0, 200, 200)

    ret = odeint(seir, y0, t, args=(args.N, args.beta, args.sigma, args.gamma))
    S, E, I, R = ret.T

    plt.plot(t, S, label='Susceptible')
    plt.plot(t, E, label='Exposed')
    plt.plot(t, I, label='Infected')
    plt.plot(t, R, label='Recovered')
    plt.legend()
    plt.xlabel('Time (days)')
    plt.ylabel('Population')
    plt.show()

if __name__ == '__main__':
    main()
