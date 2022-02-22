import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
def drow_chart(data, titles, chart):
    if chart == 'bar':
        left = [i for i in range(1, len(data) + 1)]

        # heights of bars
        height = []

        # labels for bars
        tick_label = []

        for key, value in data.items():
            height.append(value)
            tick_label.append(key)

        # plotting a bar chart
        plt.bar(left, height, tick_label = tick_label,
                width = 0.6, color = ['green'])
    elif chart == 'plot':
        # x axis values
        x = []
        # corresponding y axis values
        y = []

        for key, value in data.items():
            x.append(key)
            y.append(value)


        # plotting the points
        plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
                marker='o', markerfacecolor='blue', markersize=12)
        s = max(y)
        # setting x and y axis range
        plt.ylim(1,s + 1)
        plt.xlim(1,len(data))

    # naming the x-axis
    plt.xlabel(titles[0])
    # naming the y-axis
    plt.ylabel(titles[1])
    # plot title
    plt.title(chart.upper() + ' Chart')

    # function to show the plot
    plt.show()

