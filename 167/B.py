# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

A, B, C, K = LI()

ans = -mod
if A >= K:
    ans = K
elif A + B >= K:
    ans = A
else:
    ans = A - (K - A - B)
print(ans)