import numpy as np
from taxi import reinforcement_learning, brute_force, print_frames

def get5(list):
    arr = []
    for i in range(5):
        j = 0 + 10**i
        arr.append(list[j])
    return arr

def print_avg(label, sum, k):
    avg = sum / k
    print(label,avg)

def calc_average(n):
    print("Calculating Average of RL")
    # gives the average epochs and penatlies
    sum_e = np.zeros(5)
    sum_p = np.zeros(5)

    i = 0

    while(i < n):
        print(i, "iteration")
        result = reinforcement_learning()
        sum_e = np.add(sum_e, get5(result[1]))
        sum_p = np.add(sum_p, get5(result[2]))
        i += 1

    print_avg("epochs", sum_e, i)
    print_avg("penalties", sum_p, i)

def calc_brute_average(n):
    print("Calculating average of brute force")
    sum = np.zeros(2)
    for i in range(n):
        result = brute_force()
        new_value = [result[1], result[2]]
        sum = np.add(sum, new_value)
    print_avg("epochs", sum[0], n)
    print_avg("penalties", sum[1], n)


if __name__ == '__main__':
    calc_average(50)
    calc_brute_average(1000)
