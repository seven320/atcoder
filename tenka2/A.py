# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

A,B,C = map(int,input().split())

if A<C<B or B<C<A:
    print("Yes")
else:
    print("No")
