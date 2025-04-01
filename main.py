import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pyautogui as pg
import math as m

def plot_histo(data):
    plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.show()

def list_to_nparray(data):
    return np.array(data)

def create_list(size):
    data = []
    for i in range(size):
        data.append(rng())
    return data

def rng(seed, iterations=5):
    ...

def seed():
    seed = float(str(dt.datetime.now().microsecond) + str(dt.datetime.now().second) + str(dt.datetime.now().minute) + str(dt.datetime.now().hour) + str(dt.datetime.now().day) + str(dt.datetime.now().month) + str(dt.datetime.now().year))
    return seed

def main(amt):
    data = create_list(amt)
    data = list_to_nparray(data)
    plot_histo(data)

if "__name__" == "__main__":
    amt = 5000  # Number of random numbers to generate
    main(amt)

print(seed())