# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N,M = LI()
ab = [[] for i in range(M)]
for i in range(M):
    a,b = LI()
    a -= 1
    b -= 1
    ab[i] = [a,b]


ans = 0
ab = sorted(ab,key = lambda x:x[1])
ans += 1
a,b = ab[0]
cutting = b-1
for i in range(1,M):
    a,b = ab[i]
    if a <= cutting < b:
        pass
    else:
        cutting = b-1
        ans += 1

print(ans)

# print(ab)
