import plots_drawer

if __name__ == '__main__':
    pl_dr = plots_drawer.PlotDrawer()
    path_list = pl_dr.draw_plots('deviation.json')
    for path in path_list:
        print(path)

