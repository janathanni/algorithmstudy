import numpy as np

def solution(arr1, arr2):
    arr_1 = np.array(arr1)
    arr_2 = np.array(arr2)
    answer = arr_1 + arr_2
    return answer.tolist()

