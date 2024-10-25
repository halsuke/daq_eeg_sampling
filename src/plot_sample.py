import sys, os
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.getcwd())

from lib.select_npy_file import SelectNpyFile


def PlotData(data):
    fig = plt.figure(figsize=(6.4, 4.8))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(data)
    ax.grid()


def main():
    data_path = SelectNpyFile(os.path.join(os.getcwd(), "src"))
    sampling_data = np.load(data_path)
    PlotData(sampling_data)
    plt.show()


if __name__ == "__main__":
    main()
