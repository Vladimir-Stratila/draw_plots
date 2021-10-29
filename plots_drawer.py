import pandas as pd
import matplotlib.pyplot as plt
import os


class PlotDrawer:
    """This is a class for draw plots"""

    def __init__(self):
        self.directory = "./plots"
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def draw_plots(self, json_file):
        data = pd.read_json(json_file)
        ''' create and save plots for each columns
        for i in range(1, 12):
            file_name = self.directory + "/plot_" + data.columns[i] + ".png"
            fig = plt.figure()
            data[data.columns[i]].plot(title=data.columns[i], ylabel="Degrees")
            fig.savefig(file_name)
        '''
        fig = plt.figure()
        title = data.columns[1] + " vs " + data.columns[2]
        data.plot(kind='scatter', x=data.columns[1], y=data.columns[2], title=title, alpha=0.5)
        fig.savefig(self.directory + "/plot_" + title + ".png")

        fig = plt.figure()
        title = data.columns[6] + " vs " + data.columns[9]
        data.plot(kind='scatter', x=data.columns[6], y=data.columns[9], title=title, alpha=0.5)
        fig.savefig(self.directory + "/plot_" + title + ".png")

        fig = plt.figure()
        title = data.columns[7] + " vs " + data.columns[10]
        data.plot(kind='scatter', x=data.columns[7], y=data.columns[10], title=title, alpha=0.5)
        fig.savefig(self.directory + "/plot_" + title + ".png")

        fig = plt.figure()
        title = data.columns[8] + " vs " + data.columns[11]
        data.plot(kind='scatter', x=data.columns[8], y=data.columns[11], title=title, alpha=0.5)
        fig.savefig(self.directory + "/plot_" + title + ".png")

        path_list = []
        for root, dirs, files in os.walk(os.path.abspath(self.directory)):
            for file in files:
                full_path = os.path.join(root, file)
                path_list.append(full_path)
        return path_list
