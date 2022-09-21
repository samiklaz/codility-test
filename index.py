"""
An array A consisting of N integers is given. Rotation of the array means that each element is 
shifted right by one index, and the last element of the array is moved to the first place. 
For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] 
(elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
"""

def correctsolution(A, K):
    # write your code in Python 3.6
     old = A
     new = [0]*len(A)
     for i in range(K):
         new[0]=old[-1]
         new[1:] = old[:-1]
         old = new.copy() # This was the problematic line
     return new 


def solution(A, K):
    # write your code in Python 3.6
    old = A
    new = [0]*len(A)
    if len(A) == 0:
        new = []
    elif len(A) == 1:
        new = old
    else:
        for i in range(K):
            new[0]=old[-1]
            new[1:] = old[:-1]
            old = new.copy() # This was the problematic line
    return new 


def solution(A, K):
    new_list = []
    for i in range(len(A)):
        x = A[(i + K) % len(A)]
        new_list.append(x)
    return new_list

def solution2(A, K):
    return A[K % len(A):] + A[:K % len(A)]


def solution3(A, K):
    ret = []
    for i in range(len(A)):
        if (i + K) < len(A):
            ret.append(A[i + K])
        else:
            ret.append(A[i + K - len(A)])
    return ret


A = [3, 8, 9, 7, 6]
B = [0, 0, 0]
C = [1, 2, 3, 4]
K = 3

print(solution(A, K))
print(solution(B, K))
print(solution(C, K))


