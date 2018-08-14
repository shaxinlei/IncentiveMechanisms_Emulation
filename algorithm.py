import math
import numpy as np
import copy
import pprint
import util


# 为每个任务以此选获胜者
'''
T：任务集（元素为任务编号），例如：[0,1,2,3...]
N:用户集（元素为用户编号），例如：[0,1,2,3...]
W:用户边际福利，例如：w[0]表示用户0的边际福利
q:用户的任务贡献，例如：q[0]表示用户0完成一个任务贡献的质量
Q:任务目标质量，例如：Q[0]表示任务1的目标质量
F:用户任务集(元素为每个用户参与竞价的任务列表)，例如：
'''
def acution_winner_determination(T, N, W, q, Q, F, t, r, T1, T2, alpha, beta, open_alpha_and_beta):
    new_N = []
    alphas = util.cal_alpha(t, T2)
    betas = util.cal_beta(r, t, T1, T2)
    # print('open_alpha_and_beta:', open_alpha_and_beta)
    # print('alpha:{0}  beta:{1}'.format(alpha, betas))
    # print('alphas:', alphas)
    # print('betas:', betas)
    if any(alphas):
        print('alphas is not zero')
    for i in range(len(N)):
        if not (alphas[i] < alpha or betas[i] < beta):
            new_N.append(N[i])

    # 启用alpha beta限制条件
    if open_alpha_and_beta:
        print('open_alpha_and_beta')
        regular_N = new_N[:]
    else:
        # print('len user:{0} len task:{1}'.format(len(N), len(T)))
        print('not open_alpha_and_beta')
        regular_N = N[:]

    # initialization
    N_ = []
    S = []  # 每一项为获胜者用户编号

    # select non-negative marginal social welfare
    for i in range(len(W)):
        if i in regular_N and W[i] >= 0:
            S.append(i)

    N_ = [a for a in regular_N if a not in S]  # 去除已经获胜的人

    # Calculate residual QoI requirement
    Q_re = []  # 相当于Q'
    for j in T:
        sum_j = 0
        for i in S:
            if j in F[i]:
                sum_j += q[i]
        Q_re.append(Q[j] - min(Q[j], sum_j))

    # main loop
    while sum(Q_re):
        # find the user with the minimum marginal social welfare effectiveness
        l = 0
        min_value = 10000
        for i in N_:
            sum_i = 0
            for j in F[i]:
                sum_i += min(Q_re[j], q[i])
            if sum_i == 0:
                pass
            value = abs(W[i])/sum_i
            if value < min_value:
                min_value = value
                l = i
        S.append(l)
        N_ = [a for a in N_ if a is not l]  # 缩小N_集合

        # update residual requirement
        for j in T:
            Q_re[j] -= min(Q_re[j], q[l])
    return S

# 确定拍卖竞价
# def auction_pricing(T, N, S, alpha, q, W, Q, F, t, r):
#     # initialization
#     N_ = []
#     P = [0] * len(S)

#     # find non-negative marginal welfare users
#     for i in range(len(W)):
#         if W[i] >= 0:
#             N_.append(i)  # N_相当于N+
 
#     # main loop
#     Q_re = list.copy(Q)  # 相当于Q'
#     for i in S:
#         N_re = [a for a in N if a is not i]     # N_re相当于N\{i}
#         S_re = acution_winner_determination(T, N_re, W, q, Q, F, t, r)  # S_re相当于S'

#         # Caluate payment
#         if len(S_re) <  len(N_):
#             P[i] = alpha * q[i] * len(F[i])
#         else:
#             S_re_n = [a for a in S_re if a not in N_]  # S_re_n相当于S'\N+
#             for k in S_re_n:
#                 for j in T:
#                     Q_re[j] -= q[k]
#         value_jk = 0
#         for j in F[k]:
#             value_jk += min(Q_re, q[k])

#         value_ji = 0
#         for j in F[i]:
#             value_ji += min(Q_re, q[i])

#         P[i] = max(P[i], alpha*q[i]*abs(F[i])-W[k]*value_ji/value_jk)
#     return P
    


    


