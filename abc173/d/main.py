#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
from decimal import Decimal # 10進数で考慮できる

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))
"""
N = int(input())
A = LI()

A.sort(reverse=1)
ans = 0
ans += A[0]

tmp = 1
for i in range(1, N - 1):
    ans += A[tmp]
    if i % 2 == 0:
        tmp += 1
print(ans)
"""
N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = 0
ans += A[0]
tmp = 1
for i in range(1, N - 1):
    ans += A[tmp]
    if i % 2 == 0:
        tmp += 1
print(ans)
