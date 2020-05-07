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

N = int(input())
A = LI()
ans = 1
c = collections.Counter(A)
for key in c.keys():
    if c[key] > 1:
        ans = 0
        break

if ans:
    print("YES")
else:
    print("NO")