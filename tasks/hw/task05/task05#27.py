def main(z, x):
    res = 0
    for i in range(1, x.length):
        res += (18-x[(x.length+1-i/4)]**2-85*z[i])**2
    return res


print(main([-0.3, 0.6, 0.38, 0.63, -0.28, 0.03, -0.17, 0.42],
           [-0.88, 0.26, -0.16, 0.46, -0.83, -0.3, -0.19, -0.96]))
