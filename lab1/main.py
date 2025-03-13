import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


def gauss_np(s, v, r, steps=100):
    y = np.linspace(r[0],r[1],steps)
    for i,x in enumerate(y):
        y[i] = math.exp((-(x-v)**2)/2*s**2) / (s*math.sqrt(2*math.pi))
    return y


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=float)
    parser.add_argument('-u', type=float)
    parser.add_argument('-w', type=float)
    parser.add_argument('-r', type=list)
    parser.add_argument('--min', type=float)
    parser.add_argument('--max', type=float)
    parser.add_argument('--steps', type=int)

    args = parser.parse_args()

    std_dev = args.s if args.s else math.sqrt(args.w)
    avg = args.u
    r = args.r if args.r else [args.min, args.max]
    steps = args.steps

    x_np = np.linspace(r[0],r[1],steps)
    y_np = gauss_np(std_dev, avg, r, steps=steps)

    y_sp = sp.stats.Normal(mu=std_dev, sigma=avg)
    y_sp.plot()

    plt.plot(x_np, y_np)

    plt.show()

    


if __name__ == "__main__":
    main()