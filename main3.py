import math
import numpy as np


def get_relative_error(v01, v1):
    return math.sqrt(np.sum(np.array([((v01[i] - v1[i]) / v01[i]) ** 2 for i in range(5)])) / 5)


v01 = [68.1, 6.75, 14.3, 15.4, 51.9]
v1 =  [67.6, 6.57, 14.9, 15.6, 53.2]

v02 = [688. , 140., 110. , 151. , 620]
v2 =  [684.9, 143., 113.7, 156.2, 595]

v03 = [6900. , 1450., 1600. , 9000., 5610.]
v3 =  [6944.4, 1430., 1666.7, 9250., 5430.]

v04 = [70300, 14103, 93100, 20100, 52800]
v4  = [71400, 13700, 92600, 19230, 50000]

print(f"1: {get_relative_error(v01, v1)}")
print(f"2: {get_relative_error(v02, v2)}")
print(f"3: {get_relative_error(v03, v3)}")
print(f"4: {get_relative_error(v04, v4)}")




