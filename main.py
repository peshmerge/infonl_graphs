import numpy as np
import matplotlib.pyplot as plt
from user import User


def main():
    user_data = [
        User([[98, 35, 64], [66, 90, 42], [65, 126, 44]], [19194.948, 19742.966, 19068.638], [0.064, 0.0381, 0.0322]),
        User([[54, 10, 29], [32, 22, 21], [28, 33, 23]], [9927.009, 12528.58, 12812.635], [0.3795, 0.0109, 0.0213]),
        User([[52, 33, 42], [47, 43, 60], [36, 19, 21]], [10059.626, 18670.221, 12975.607], [0.4631, 0.0073, 0.0395]),
        User([[60, 2, 48], [20, 6, 20], [43, 32, 62]], [11119.35, 11413.964, 12940.586], [0.0831, 0.1197, 0.0317]),
        User([[66, 76, 54], [36, 39, 43], [40, 62, 18]], [11660.969, 10696.924, 11661.333], [0.0763, 0.0512, 0.0264]),
        User([[42, 41, 16], [34, 25, 35], [37, 59, 47]], [9319.373, 9643.929, 9583.329], [0.1581, 0.0106, 0.0786]),
        User([[39, 44, 29], [36, 52, 32], [23, 21, 9]], [9237.274, 11574.91, 10565.961], [0.1038, 0.0236, 0.0389]),
        User([[56, 56, 59], [21, 51, 8], [30, 34, 13]], [10840.654, 10565.991, 11561.004], [0.1326, 1, 0.0119]),
        User([[71, 35, 68], [19, 0, 21], [45, 54, 50]], [10202.009, 11994.292, 9620.324], [0.4196, 0.9687, 0.0107]),
        User([[8, 2, 1], [0, 0, 2], [3, 0, 0]], [15741.525, 14021.903, 13525.98], [0.8766, 0.4426, 0.3334]),
        User([[5, 14, 0], [2, 1, 0], [1, 0, 1]], [4481.262, 4481.262, 7955.328], [0.0616, 0.88, 0]),
        User([[5, 14, 0], [0, 3, 1], [0, 5, 0]], [4481.262, 10146.875, 2073.022], [0.0616, 0.0371, 0]),
        User([[3, 5, 3], [0, 0, 0], [0, 0, 0]], [9294.162, 9621.778, 6724.558], [0, 1, 1])]

    print("How many times did the user have to be corrected?")
    print(get_average_question1(user_data, 0))
    print(get_average_question1(user_data, 1))
    print(get_average_question1(user_data, 2))
    print()

    print("On average, how long did it take before the user corrected him/herself ")
    print(get_average_question2(user_data, 0))
    print(get_average_question2(user_data, 1))
    print(get_average_question2(user_data, 2))
    print()

    print("How long of the total time did they maintain correct posture?  ")
    print(get_average_question3(user_data, 0))
    print(get_average_question3(user_data, 1))
    print(get_average_question3(user_data, 2))

    get_graph_question1(user_data, 0)
    get_graph_question1(user_data, 1)
    get_graph_question1(user_data, 2)

    get_graph_question2(user_data,0)
    get_graph_question2(user_data,1)
    get_graph_question2(user_data,2)


    get_graph_question3(user_data,0)
    get_graph_question3(user_data,1)
    get_graph_question3(user_data,2)

    comparing_all_data_question1(user_data,0)
    comparing_all_data_question2(user_data,0)
    comparing_all_data_question3(user_data,0)


def comparing_all_data_question3(data_list,pattern):
    y_scale_fs_1 = []
    y_scale_fs_1.append(get_average_question3(data_list, 0))
    y_scale_fs_1.append(get_average_question3(data_list, 1))
    y_scale_fs_1.append(get_average_question3(data_list, 2))
    # create a plot
    fig = plt.figure()
    index = np.arange(3)
    bar_width = 0.25
    opacity = 0.99
    plt.bar(index, y_scale_fs_1, bar_width, alpha=opacity,color='r',label='Time percentage')
    plt.xlabel("Patterns")
    plt.ylabel("Percentage")
    plt.title("How long of the total time did they maintain correct posture?")
    plt.xticks(index, ('Pattern 1', 'Pattern 2', 'Pattern 3'))
    plt.setp(plt.xticks()[1])
    plt.legend()
    average = get_average_question2(data_list, pattern)
    fig.savefig("figure_7_2_3")
    plt.show()

def comparing_all_data_question2(data_list,pattern):
    y_scale_fs_1 = []
    y_scale_fs_1.append(get_average_question2(data_list, 0))
    y_scale_fs_1.append(get_average_question2(data_list, 1))
    y_scale_fs_1.append(get_average_question2(data_list, 2))
    # create a plot
    fig = plt.figure()
    index = np.arange(3)
    bar_width = 0.25
    opacity = 0.99
    plt.bar(index, y_scale_fs_1, bar_width, alpha=opacity,color='r',label='Average time')
    plt.xlabel("Patterns ")
    plt.ylabel("Average ")
    plt.title("How long did it take before the user corrected him/herself?")
    plt.xticks(index, ('Pattern 1', 'Pattern 2', 'Pattern 3'))
    plt.setp(plt.xticks()[1])
    plt.legend()
    average = get_average_question2(data_list, pattern)
    fig.savefig("figure_7_2_2")
    plt.show()


def comparing_all_data_question1(data_list,pattern):
    groups = len(data_list)
    y_scale_fs_1 = []
    y_scale_fs_2 = []
    y_scale_fs_3 = []
    y_scale_fs_1.append(get_average_question1(data_list, 0))
    y_scale_fs_2.append(get_average_question1(data_list, 1))
    y_scale_fs_3.append(get_average_question1(data_list, 2))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    index = np.arange(3)
    bar_width = 0.25
    opacity = 0.99
    ax.bar(index, y_scale_fs_1[0], bar_width, alpha=opacity,color='b',label="Flex sensor 1")
    ax.bar(index + bar_width + 0.20, y_scale_fs_2[0], bar_width,alpha=opacity,color='g',label='Flex sensor 2')
    ax.bar(index + bar_width, y_scale_fs_3[0], bar_width,alpha=opacity,color='r',label='Flex sensor 3')
    plt.xlabel("Patterns")
    plt.ylabel("Average")
    plt.title("How many times did the user have to be corrected? ")
    plt.xticks(index, (
    'Pattern 1', 'Pattern 2', 'Pattern 3'))
    plt.setp(plt.xticks()[1])
    plt.legend()
    fig.savefig("figure_7_2_1")
    plt.show()


def get_graph_question3(data_list,pattern):
    groups = len(data_list)
    y_scale_fs_1 = []
    for data in data_list:
        y_scale_fs_1.append(data.get_question3()[pattern])
    # create a plot
    fig = plt.figure()

    index = np.arange(groups)
    bar_width = 0.25
    opacity = 0.99

    plt.bar(index, y_scale_fs_1, bar_width,
            alpha=opacity,
            color='r',
            label='Time Percentage')

    plt.xlabel("Users")
    plt.ylabel("Percentage ")
    plt.title("How long of the total time did they maintain correct posture? Pattern" + str(pattern + 1))
    plt.xticks(index, (
        'User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9', 'User10', 'User11', 'User12',
        'User13'))
    plt.setp(plt.xticks()[1], rotation=90)
    plt.legend()
    average = get_average_question3(data_list, pattern)

    plt.axhline(y=average, linestyle='dashed', xmin=0, xmax=0.99, color='b')
    plt.text(1.02, average, average)
    fig.savefig("figure3_pattern" + str(pattern + 1))
    plt.show()


def get_graph_question2(data_list,pattern):
    groups = len(data_list)
    y_scale_fs_1 = []
    for data in data_list:
        y_scale_fs_1.append(data.get_question2()[pattern])
    # create a plot
    fig = plt.figure()

    index = np.arange(groups)
    bar_width = 0.25
    opacity = 0.99

    plt.bar(index, y_scale_fs_1, bar_width,
           alpha=opacity,
           color='r',
           label='Average time')

    plt.xlabel("Users")
    plt.ylabel("Average ")
    plt.title("How long did it take before the user corrected him/herself Pattern" + str(pattern + 1))
    plt.xticks(index, (
        'User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9', 'User10', 'User11', 'User12',
        'User13'))
    plt.setp(plt.xticks()[1], rotation=90)
    plt.legend()
    average = get_average_question2(data_list, pattern)

    plt.axhline(y=average, linestyle='dashed', xmin=0, xmax=0.99, color='b')
    plt.text(1.02, average, average)
    fig.savefig("figure2_pattern" + str(pattern + 1))
    plt.show()



def get_graph_question1(data_list, pattern):
    groups = len(data_list)
    y_scale_fs_1 = []
    y_scale_fs_2 = []
    y_scale_fs_3 = []
    for data in data_list:
        y_scale_fs_1.append(data.get_question1()[pattern][0])
        y_scale_fs_2.append(data.get_question1()[pattern][1])
        y_scale_fs_3.append(data.get_question1()[pattern][2])

    # create a plot
    fig = plt.figure()

    ax = fig.add_subplot(111)
    index = np.arange(groups)
    bar_width = 0.25
    opacity = 0.99

    ax.bar(index, y_scale_fs_1, bar_width,
           alpha=opacity,
           color='b',
           label='Flex sensor 1')
    ax.bar(index + bar_width + 0.20, y_scale_fs_2, bar_width,
           alpha=opacity,
           color='g',
           label='Flex sensor 2')

    ax.bar(index + bar_width, y_scale_fs_3, bar_width,
           alpha=opacity,
           color='r',
           label='Flex sensor 3')
    plt.xlabel("Users")
    plt.ylabel("Average ")
    plt.title("How many times did the user have to be corrected? Pattern"+str(pattern+1))
    plt.xticks(index, (
    'User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9', 'User10', 'User11', 'User12',
    'User13'))
    plt.setp(plt.xticks()[1], rotation=90)
    plt.legend()
    average = get_average_question1(data_list,pattern)
    plt.axhline(y=average[0], linestyle='dashed', xmin=0, xmax=0.99, color='b')
    ax.text(1.02, average[0], average[0], transform=ax.get_yaxis_transform())

    plt.axhline(y=average[1], linestyle='dashed', xmin=0, xmax=0.99, color='g')
    ax.text(1.02, average[1], average[1], transform=ax.get_yaxis_transform())

    plt.axhline(y=average[2], linestyle='dashed', xmin=0, xmax=0.99, color='r')
    ax.text(1.02, average[2], average[2], transform=ax.get_yaxis_transform())
    fig.savefig("figure_pattern"+str(pattern+1))
    plt.show()


def get_average_question3(data_list, pattern):
    """
    This function returns the average of time percentages the user of all users who maintained correct posture
    :param data_list: a list of data of all users
    :param pattern: pattern number (0,1,2)
    :return: the average of the time
    """
    temp_sum = 0
    for data in data_list:
        temp_sum += (data.get_question3()[pattern])
    return round(temp_sum / len(data_list), 2)


def get_average_question2(data_list, pattern):
    """
    This functions returns the average time all users needed to correct themselves
    :param data_list: a list of data of all users
    :param pattern: pattern number (0,1,2)
    :return: the average of the time
    """
    temp_sum = 0
    for data in data_list:
        temp_sum += (data.get_question2()[pattern])
    return round(temp_sum / len(data_list), 3)


def get_average_question1(data_list, pattern):
    """
    This function returns the average amount of how many times each flex sensor has been corrected for all users
    :param data_list: a list of data of all users
    :param pattern: pattern number (0,1,2)
    :return: the average of of the time
    """
    temp_sum = [0, 0, 0]
    for data in data_list:
        temp_sum = [temp_sum[i] + data.get_question1()[pattern][i] for i in range(3)]
    return [round(i / len(data_list), 0) for i in temp_sum]


if __name__ == "__main__": main()
