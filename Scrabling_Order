import random 
import math 
import numpy as np
import sys
import matplotlib.pyplot as plt 

def Seeking_Tmax(N):
    dp = [[0] * (i + 1) for i in range(N + 1)]
    Tmax = [i for i in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][1] = i
    for i in range(2, N + 1):
        for j in range(2, i + 1):
            dp[i][j] = max(dp[i-k][j-1] * k // math.gcd(dp[i-k][j-1], k) for k in range(1, i) if i-k >= j-1 and k <= i/2)
            if dp[i][j] >= Tmax[i]:
                Tmax[i] = dp[i][j]
    return Tmax

def random_scrambling_generation (N):
    scrambling_number = {}
    numbers = list(range (1, N+1))
    random.shuffle (numbers)
    for i in range (N):
        scrambling_number[i+1] = numbers[i]
    return scrambling_number

def Seeking_scrambling_Tmax(scrambling_number):
    Tmax = 1
    visited = set()
    for i in range(1, len(scrambling_number) + 1):
        if i in visited:
            continue
        cycle_len = 1
        visited.add(i)
        next_num = scrambling_number[i]
        while next_num != i:
            cycle_len += 1
            visited.add(next_num)
            next_num = scrambling_number[next_num]
        Tmax = (Tmax * cycle_len) // math.gcd(Tmax, cycle_len)
    return Tmax

def chaotic_mapping(x0, N, u):
    x = [0] * (N + 1)
    x[0] = x0
    y = [(0, 0)]
    scramble = {}
    table1 = table2 = ''
    for i in range(1, N + 1):
        x[i] = u * x[i - 1] * (1 - x[i - 1])
        y.append((x[i], i))
    y.sort()
    for i in range(1, N + 1):
        scramble[i] = y[i][1]
    for i in range(1, N + 1):
        table1 += f"{i:>{len(str(N)) + 1}} "
        table2 += f"{scramble[i]:>{len(str(N)) + 1}} "
    l = Seeking_scrambling_Tmax(scramble)
    return l, table1, table2, scramble

def Sampling_curve_drawing(N, maxT):
    p = [0.0] * 30
    k = [0.0] * 30
    for i in range(pow(N, 2) + 10000):
        scramble = random_scrambling_generation(N)
        scramble_order = Seeking_scrambling_Tmax(scramble)
        K = min((scramble_order * 30) // maxT + 1, 30)
        for j in range(K - 1, 30):
            p[j] += 1.0
    for i in range(30):
        k[i] = (i + 0.5) * maxT / 30
        p[i] = round(p[i] / (N * N + 10000), 8)
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.plot([0] + k + [maxT], [0] + p + [1.0])
    ax.set_yticks(np.arange(0, 1.05, 0.05))
    ax.set_xticks(np.arange(0, maxT + maxT / 30, maxT / 30))
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel("Order", fontsize=20)
    ax.set_ylabel("probability", fontsize=20)
    ax.set_title(f"p(k) curve:N={N}", fontsize=20)
    for a, b in zip([0] + k + [maxT], [0] + p + [1.0]):
        ax.text(a, b, round(b, 2), ha='center', va='bottom', fontsize=8)
    plt.show()

def Sampling_chaotic_drawing(N, maxT):
    p = [0.0] * 30
    k = [0.0] * 30
    for i in range(pow(N, 2) + 10000):
        x0 = random.random()
        u = random.uniform(3.60, 4.00)
        _, _, _, scramble = chaotic_mapping(x0, N, u)
        scramble_order = Seeking_scrambling_Tmax(scramble)
        K = min((scramble_order * 30) // maxT + 1, 30)
        for j in range(K - 1, 30):
            p[j] += 1.0
    for i in range(30):
        k[i] = (i + 0.5) * maxT / 30
        p[i] = round(p[i] / (N * N + 10000), 8)
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.plot([0] + k + [maxT], [0] + p + [1.0])
    ax.set_yticks(np.arange(0, 1.05, 0.05))
    ax.set_xticks(np.arange(0, maxT + maxT / 30, maxT / 30))
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel("order", fontsize=20)
    ax.set_ylabel("probability", fontsize=20)
    ax.set_title(f"p(k) curve:N={N}", fontsize=20)
    for a, b in zip([0] + k + [maxT], [0] + p + [1.0]):
        ax.text(a, b, round(b, 2), ha='center', va='bottom', fontsize=8)
    plt.show()

def plot_sampling_curve(N):
    Tmax = Seeking_Tmax(N)
    print('最大阶T:', Tmax[N])
    predrawing = input('是否绘制p(k)曲线，需要请按1，不需要请按#')
    if predrawing == '1':
        Sampling_curve_drawing(N, Tmax[N])

def Chaotic_gengrating(N):
    Tmax = Seeking_Tmax(N)
    u = random.uniform(3.60, 4.00)
    x0 = random.random()
    ans, ansstr1, ansstr2, scramble = chaotic_mapping(x0, N, u)
    print('构造的置乱是:\n', ansstr1 + '\n', ansstr2 + '\n', '这个置乱的阶是:', ans)
    print('同时在这里，我给出N=', N, '时的最大阶T:', Tmax[N])
    print('同时在这里，我还将给出用该混沌函数作为置乱生成时所绘制的p(k)曲线')
    Sampling_chaotic_drawing(N, Tmax[N])

while 1:
    print('请选择你需要的功能')
    Function = input('功能1.求出N最大阶T以及绘制出P（K）曲线\n功能2：logistic混沌映射构造置乱\n选择你所需要的功能 请按 1 or 2\n需要退出请按 #\n')
    if Function == '1':
        N = int(input('请输入个数N:'))
        plot_sampling_curve(N)
    else:
        if Function == '2':
            N = int(input('请输入个数N:'))
            Chaotic_gengrating(N)
        else:
            if Function == '#':
                sys.exit()
