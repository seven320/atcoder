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

# n, a, b = LI()


# ans = pow(2, n, mod) - 1
# math.factorial()

# print(ans % mod)

def fur(n,r):
    p,q = 1,1
    for i in range(r):
        p = p*(n-i)%mod
        q = q*(i+1)%mod
        print(p, q)
    return p * pow(q,mod-2,mod) % mod

# print((ans - fur(n, a) - fur(n, b)) % mod)