import random
import math
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import MultipleLocator

# 产生符合负指数随机分布的时间间隔序列
def poisson(load):
    while True:
        rand = random.random()
        if rand != 0 and rand != 1:
            break
    return -math.log(rand) / load
def f(t):
    return 1/(1+math.exp(-t))


def sgn(t):
    if t > 0:
        return 1
    elif t == 0:
        return 1/2
    else:
        return 0


# 计算每个用户的alpha值
def cal_alpha(t, T2):
    alphas = []
    for i in range(len(t)):
        value = (2*sgn(t[i]-T2)*f(T2-t[i])+sgn(T2-t[i]))
        alphas.append(value)
    return alphas


# 计算每个用户的beta值
def cal_beta(r, t, T1, T2):
    betas = []
    for i in range(len(t)):
        if r[i] > 0:
            value = (2-2/(1+math.exp(-1*r[i])))*t[i]/(T2-T1)
            betas.append(value)
        else:   # ri[]=0
            value = t[i]/(T2-T1)
            betas.append(value)
    return betas


# 画变化的用户数与社会福利图
def plot_vary_users_with_welfare(user_range, vary_users_welfares):
    # index = np.arange(0, len(user_range), 10)
    # x = [user_range[i] for i in index]
    # y = [vary_users_welfares[i] for i in index]
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    plt.plot(user_range, vary_users_welfares, linestyle='-', marker='.')

    # xmajorLocator = MultipleLocator(20)  # 将此x轴主刻度标签设置为10的倍数
    # yminorLocator = MultipleLocator(400) # 将此y轴次刻度标签设置为200的倍数
    #
    # # 显示主刻度标签的位置,没有标签文本
    # ax.xaxis.set_major_locator(xmajorLocator)
    #
    # ax.yaxis.set_minor_locator(yminorLocator)
    #
    # ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    # ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度

    plt.xlabel('Number of Users')
    plt.ylabel('Social Welfare')
    plt.title('Vary User Numbers VS Social Welfare')
    # plt.ylim(0, 10000)
    plt.show()


# 画变化的任务数与社会福利图
def plot_vary_tasks_with_welfare(task_range, vary_tasks_welfares):
    # index = np.arange(0, len(task_range), 10)
    # x = [task_range[i] for i in index]
    # y = [vary_tasks_welfares[i] for i in index]
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    plt.plot(task_range, vary_tasks_welfares, linestyle='--', marker='s')
    # xmajorLocator = MultipleLocator(20)  # 将此x轴主刻度标签设置为10的倍数
    # yminorLocator = MultipleLocator(200) # 将此y轴次刻度标签设置为200的倍数
    #
    # # 显示主刻度标签的位置,没有标签文本
    # ax.xaxis.set_major_locator(xmajorLocator)
    #
    # ax.yaxis.set_minor_locator(yminorLocator)
    #
    # ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    # ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度

    plt.xlabel('Number of Tasks')
    plt.ylabel('Social Welfare')
    plt.title('Vary Task Numbers VS Social Welfare')
    # plt.ylim(1000, 8000)
    plt.show()


# 画变化的用户数与社会福利图(变化alpha)
def plot_vary_users_with_welfare_vary_alpha_or_beta(user_range, vary_list, vary_users_welfares_vary_list, vary_type):
    # index = np.arange(0, len(user_range), 10)
    # x = [user_range[i] for i in index]

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    marker_list = ['^', 's', 'v']
    for j in range(len(vary_list)):
        # y = [vary_users_welfares_vary_list[j][i] for i in index]
        plt.plot(user_range, vary_users_welfares_vary_list[j], label=vary_type+'='+str(vary_list[j]), linestyle='-', marker=marker_list[j])

    xmajorLocator = MultipleLocator(20)  # 将此x轴主刻度标签设置为10的倍数
    yminorLocator = MultipleLocator(400) # 将此y轴次刻度标签设置为200的倍数

    # 显示主刻度标签的位置,没有标签文本
    ax.xaxis.set_major_locator(xmajorLocator)

    ax.yaxis.set_minor_locator(yminorLocator)
    
    ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度

    plt.legend(loc='lower right')
    plt.xlabel('Number of Users')
    plt.ylabel('Social Welfare')
    plt.title('Vary User Numbers VS Social Welfare(varying '+vary_type+')')
    # plt.ylim(0, 10000)
    plt.show()    


# 画变化的任务数与社会福利图(变化beta)
def plot_vary_tasks_with_welfare_vary_alpha_or_beta(task_range, vary_list, vary_tasks_welfares_vary_list, vary_type):
    index = np.arange(0, len(task_range), 10)
    x = [task_range[i] for i in index]
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)

    marker_list = ['^', 's', 'v']
    for j in range(len(vary_list)):
        y = [vary_tasks_welfares_vary_list[j][i] for i in index]
        plt.plot(x, y, label=vary_type+' = '+str(vary_list[j]), linestyle='--', marker=marker_list[j])
 
    xmajorLocator = MultipleLocator(20)  # 将此x轴主刻度标签设置为10的倍数
    yminorLocator = MultipleLocator(200) # 将此y轴次刻度标签设置为200的倍数

    # 显示主刻度标签的位置,没有标签文本
    ax.xaxis.set_major_locator(xmajorLocator)

    ax.yaxis.set_minor_locator(yminorLocator)
    
    ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度

    plt.legend(loc='lower right')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Social Welfare')
    plt.title('Vary Task Numbers VS Social Welfare(varying '+vary_type+')')
    # plt.ylim(1000, 8000)
    plt.show()

# 画柱状图
def plot_histogram(user_range, alpha_list, vary_users_welfares):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    x = np.arange(len(user_range))
    total_width = 0.8  # 柱状图宽度
    n = len(alpha_list)  # 类型个数
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, vary_users_welfares[0], width=width, label=r'$\alpha=$'+str(alpha_list[0]))
    plt.bar(x + width, vary_users_welfares[1], width=width, label=r'$\alpha=$'+str(alpha_list[1]))
    plt.bar(x + 2 * width, vary_users_welfares[2], width=width, label=r'$\alpha=$'+str(alpha_list[2]))
    x_labels = ['100', '120', '140', '160', '180', '200']
    x = x + width
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    plt.ylim(0, 400)
    plt.legend()
    plt.show()

# 画柱状图
def plot_histogram_vary_alpha(user_range, vary_users_welfares, alpha):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    x = np.arange(len(user_range))
    label_list = ['QoI-VCG', 'QoI-RA', 'QoI-greedy']
    total_width = 0.8  # 柱状图宽度
    n = len(label_list)  # 类型个数
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, vary_users_welfares[0], width=width, label=label_list[0])
    plt.bar(x + width, vary_users_welfares[1], width=width, label=label_list[1])
    plt.bar(x + 2 * width, vary_users_welfares[2], width=width, label=label_list[2])
    x_labels = ['100', '120', '140', '160', '180', '200']
    x = x + width
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    plt.ylim(0, 400)
    plt.legend()
    plt.title(r'$\alpha=$'+str(alpha))
    plt.show()


if __name__ == '__main__':
    user_range = np.arange(100, 201, 20)
    alpha_list = [0.5, 0.6, 0.7]

    vary_users_welfares = []

    vary_users_welfares_lapha5 = []
    vary_users_welfares_lapha5.append([212, 220, 232, 238, 248, 250])
    vary_users_welfares_lapha5.append([182, 185, 189, 200, 225, 230])
    vary_users_welfares_lapha5.append([153, 160, 162, 180, 182, 188])

    vary_users_welfares_lapha6 = []
    vary_users_welfares_lapha6.append([212, 220, 232, 238, 248, 250])
    vary_users_welfares_lapha6.append([182, 185, 189, 200, 225, 230])
    vary_users_welfares_lapha6.append([153, 160, 162, 180, 182, 188])

    vary_users_welfares_lapha7 = []
    vary_users_welfares_lapha7.append([212, 220, 232, 238, 248, 250])
    vary_users_welfares_lapha7.append([182, 185, 189, 200, 225, 230])
    vary_users_welfares_lapha7.append([153, 160, 162, 180, 182, 188])

    vary_users_welfares.append(vary_users_welfares_lapha5)
    vary_users_welfares.append(vary_users_welfares_lapha6)
    vary_users_welfares.append(vary_users_welfares_lapha7)

    # plot_histogram(user_range, alpha_list, vary_users_welfares)

    for i in range(len(alpha_list)):
        plot_histogram_vary_alpha(user_range, vary_users_welfares[i], alpha_list[i])


