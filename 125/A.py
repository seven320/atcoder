# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

A,B,T = map(int,input().split())

ans = (T//A)*B

print(ans)
