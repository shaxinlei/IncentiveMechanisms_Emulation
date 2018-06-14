# 这里使用python内置的random模块
import numpy as np
import random
import math
import pprint
import time as t
import util
import algorithm as alg

# 创建q列表，即表示用户的任务贡献
def create_q(num_user, q_range):
    q_list = []
    for i in range(num_user):
        q_list.append(random.uniform(q_range[0], q_range[1]))
    return q_list


# 创建Q列表，即表示任务的质量要求
def create_Q(num_tasks, Q_range):
    Q_list = []
    for i in range(num_tasks):
        Q_list.append(random.uniform(Q_range[0], Q_range[1]))
    return Q_list


# 创建用户列表(用户的到来是随机的)
# t_range:用户到达的时间范围，r_range：用户距离拍摄目标的距离
def create_user_random(num_user, t_range, r_range):
    user_list = [i for i in range(num_user)]
    time = []
    for i in user_list:
        time.append(random.uniform(t_range[0], t_range[1]))
    distance = []
    for i in user_list:
        distance.append(random.uniform(r_range[0], r_range[1]))
    return user_list, time, distance

# # 创建用户列表（用户到来符合泊松分布）
# def create_user_possion(num_user, t_range, r_range):
#     user_list = [i for i in range(num_user)]
#     arrive_time = []
#     for i in user_list:
#         arrive_time.append(util.poisson(3))
#     distance = []
#     for i in user_list:
#         distance.append(random.uniform(r_range[0], r_range[1]))
#     return user_list, arrive_time, distance

# 创建任务列表
def create_tasks(num_tasks):
    task_list = [i for i in range(num_tasks)]
    return task_list


# 指定每个用户选择的task列表
def create_eta(num_user, eta_range, T):
    eta_list = []
    for i in range(num_user):
        length = random.randint(eta_range[0],eta_range[1])
        slice = random.sample(T, length)
        eta_list.append(slice)
    return eta_list


# 根据公式计算W向量
def cal_W(lambda_, q, eta, t, k):
    W = []
    for i in range(len(t)):
        W.append(lambda_*q[i]*len(eta[i]) - random.uniform(2, 4))
    return W


# 变化用户数，计算不同用户数条件的社会福利，并将计算结果以列表的形式返回
def run_vary_users(user_range, num_tasks, alpha, beta, open_alpha_and_beta):
    welfares = []  # 存储社会福利
    run_times = {}
    for num_users in user_range:
        # start_time = t.time()
        lambda_ = 0.1
        l = 5
        k = 0.1 
        T1 = 0
        T2 = 30
        q_range = [1, 2] 
        Q_range = [10, 15]
        t_range = [20, 40]
        r_range = [0, 7]
        eta_range = [20, 30]
        q = create_q(num_users, q_range)
        Q = create_Q(num_tasks, Q_range)
        T = create_tasks(num_tasks)
        N, time, distance = create_user_random(num_users, t_range, r_range)
        eta = create_eta(num_users, eta_range, T)

        # 计算W
        W = cal_W(lambda_, q, eta, time, k)

        # 调用算法，返回获胜者列表
        winnners = alg.acution_winner_determination(T, N, W, q, Q, eta, time,
                                                    distance, T1, T2, alpha, beta, open_alpha_and_beta)

        welfare = 0  # 总社会福利
        for i in winnners:
            welfare += W[i]

        # end_time = t.time()
        # run_time = end_time - start_time
        # run_times[num_users] = run_time
        # print('welfare:', welfare)
        welfares.append(welfare)
    # with open('logs/vary_users.txt', 'w') as f:
    #     for key, value in run_times.items():
    #         print(str(key) + ':' + str(value), file=f)
    # print('run_time:', run_times)
    return welfares


# 变换任务数，计算不同任务数情况下的社会福利，并将结果以列表的形式返回
def run_vary_tasks(task_range, num_users, alpha, beta, open_alpha_and_beta):
    welfares = []
    run_times = {}
    for num_tasks in task_range:
        # start_time = t.time()
        lambda_ = 0.1
        l = 5
        k = 0.1 
        T1 = 0
        T2 = 60
        q_range = [1, 2]
        Q_range = [10, 15]
        t_range = [0, 60]
        r_range = [0, 7]
        eta_range = [20, 30]
        q = create_q(num_users, q_range)
        Q = create_Q(num_tasks, Q_range)
        T = create_tasks(num_tasks)
        N, time, distance = create_user_random(num_users, t_range, r_range)
        eta = create_eta(num_users, eta_range, T)

        # 计算W
        W = cal_W(lambda_, q, eta, time, k)

        # 调用算法，返回获胜者列表
        winnners = alg.acution_winner_determination(T, N, W, q, Q, eta, time,
                                                    distance, T1, T2, alpha, beta, open_alpha_and_beta)

        welfare = 0  # 总社会福利
        for i in winnners:
            welfare += W[i]

        # end_time = t.time()
        # run_time = end_time - start_time
        # run_times[num_tasks] = run_time
        # print('welfare:', welfare)
        welfares.append(welfare)
    # with open('logs/vary_tasks.txt', 'w') as f:
    #     for key, value in run_times.items():
    #         print(str(key) + ':' + str(value), file=f)
    # print('run_time:', run_times)
    return welfares
    

if __name__ == '__main__':
    # user_range = [i+200 for i in range(301)]  # 用户数的变化范围
    user_range = np.arange(100, 201, 5)  # 用户数的变化范围
    num_tasks = 62

    # # task_range = [i+300 for i in range(301)]  # 任务数的变化范围
    #     # task_range = np.arange(32, 62, 1)  # 任务数的变化范围
    #     # num_users = 100

    # 不启用alpha beta限制条件
    fix_alpha = 0.6
    fix_beta = 0.6
    vary_users_welfares = run_vary_users(user_range, num_tasks, fix_alpha, fix_beta, 0)

    # vary_tasks_welfares = run_vary_tasks(task_range, num_users, fix_alpha, fix_beta, 0)

    util.plot_vary_users_with_welfare(user_range, vary_users_welfares)

    # util.plot_vary_tasks_with_welfare(task_range, vary_tasks_welfares)

    # 启用alpha beta限制条件
    # fixed alpha and beta
    fix_alpha = 0.6
    fix_beta = 0.6
    vary_users_welfares = run_vary_users(user_range, num_tasks, fix_alpha, fix_beta, 1)

    # vary_tasks_welfares = run_vary_tasks(task_range, num_users, fix_alpha, fix_beta, 1)

    util.plot_vary_users_with_welfare(user_range, vary_users_welfares)

    # util.plot_vary_tasks_with_welfare(task_range, vary_tasks_welfares)

    # # vary alpha and fix beta
    vary_type1 = 'alpha'
    alpha_list = [0.6, 0.7, 0.9]
    fix_beta = 0.6

    vary_users_welfares_vary_alpha = []
    vary_tasks_welfares_vary_alpha = []
    for alpha in alpha_list:
        vary_users_welfares_vary_alpha.append(run_vary_users(user_range, num_tasks, alpha, fix_beta, 1))
        # vary_tasks_welfares_vary_alpha.append(run_vary_tasks(task_range, num_users, alpha, fix_beta, 1))

    util.plot_vary_users_with_welfare_vary_alpha_or_beta(user_range, alpha_list, vary_users_welfares_vary_alpha, vary_type1)
    # util.plot_vary_tasks_with_welfare_vary_alpha_or_beta(task_range, alpha_list, vary_tasks_welfares_vary_alpha, vary_type1)

    # # vary beta and fix alpha
    # vary_type2 = 'beta'
    # beta_list = [0.6, 0.7, 0.9]
    # fix_alpha = 0.6
    #
    # vary_users_welfares_vary_beta = []
    # vary_tasks_welfares_vary_beta = []
    # for beta in beta_list:
    #     vary_users_welfares_vary_beta.append(run_vary_users(user_range, num_tasks, fix_alpha, beta, 1))
    #     vary_tasks_welfares_vary_beta.append(run_vary_tasks(task_range, num_users, fix_alpha, beta, 1))
    #
    # util.plot_vary_users_with_welfare_vary_alpha_or_beta(user_range, beta_list, vary_users_welfares_vary_beta, vary_type2)
    # util.plot_vary_tasks_with_welfare_vary_alpha_or_beta(task_range, beta_list, vary_users_welfares_vary_beta, vary_type2)



    

