#encoding: utf-8

n = int(input())
A = [int(i) for i in input().split()]


A.sort()
print(A[-1]-A[0])
