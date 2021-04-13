import utils.database_service
import matplotlib.pyplot as plt
# import numpy as np
#
# import pandas as pd
# climate_change = pd.read_csv('climate.csv', parse_dates=["date"], index_col="date")
# print(climate_change)

#test data
pressure = [1000, 990, 1100, 1150]
wellness = [5, 4, 8, 10]
datatime = [1, 2, 3, 4]


def make_graph(datatime, pressure, wellness):
    fig, ax1 = plt.subplots() # Create plot with subplot object

    ax1.plot(datatime, pressure, label="pressure", color='red', alpha=1)
    ax1.set_xlabel('Timestamp') # Add an x-label to the axes
    ax1.set_ylabel('Pressure level') # Add an y-label to the axes
    ax1.set_title("Wellness/Pressure Plot")

    ax2 = ax1.twinx()
    ax2.bar(datatime, wellness, label="wellness", color='blue', alpha=0.1)
    ax2.set_ylabel('Wellness level')

    fig.tight_layout()
    lines, labels = ax1.get_legend_handles_labels() # get labels from line graph
    lines2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(lines + lines2, labels + labels2, loc=0) # create labels list
    plt.savefig('foo.png', bbox_inches='tight')
    plt.show()
    plt.close()
    #TODO return image

if __name__ == '__main__':
    make_graph(datatime,pressure,wellness)