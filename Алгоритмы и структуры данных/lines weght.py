from sys import stdin
import numpy as np

def make_array(m):
    return np.zeros((m, 3))

def sort_array_w(array):
    return array[array[:,1].argsort()]

def sort_array_c(array):
    return array[array[:,0].argsort()]

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
num_of_data = int(lines[0])
lines.pop(0)
chlen = 0
for j in range(len(lines)):
    if lines[j] == '':
        n_m = list(map(int, str(lines[j + 1]).split()))
        n, m = n_m[0], n_m[1]
        array = make_array(m)
        for k in range(m):
                c_w = list(map(int, str(lines[j + 2 + k]).split()))
                array[k][0], array[k][1], array[k][2] = c_w[0], c_w[1], k + 1
        if m != 2*n:
            array_sorted_w = sort_array_w(array)
            array_sorted_min = array_sorted_w[:2*n]
            array_sorted_c = sort_array_c(array_sorted_min)
            for l in range(n):
                print(int(array_sorted_c[l][2]), int(array_sorted_c[2*n - 1 - l][2]))
        else:
            array_sorted_c = sort_array_c(array)
            print(int(np.sum(array[:,1])))
            for l in range(n):
                print(int(array_sorted_c[l][2]), int(array_sorted_c[2*n - 1 - l][2]))
        chlen = chlen + 1
        if chlen != num_of_data:
            print()
        