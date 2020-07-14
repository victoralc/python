from typing import List


def findLucky(arr: List[int]) -> int:
    lucky = -1
    freq = [0] * 500
    for num in arr:
        if freq[num] != 0:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1

    for i in range(len(freq)):
        if freq[i] != 0 and i == freq[i]:
            lucky = freq[i]

    return lucky

if __name__ == '__main__':
    print(findLucky([2,2,3,4]))