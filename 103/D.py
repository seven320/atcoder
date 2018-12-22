
# coding: utf-8

# 問題文
# 
# 東西一列に並んだ N
# 個の島と N−1
# 
# 本の橋があります。
# 
# i
# 番目の橋は、西から i 番目の島と西から i+1
# 
# 番目の島を接続しています。
# 
# ある日、いくつかの島同士で争いが起こり、島の住人たちから M
# 
# 個の要望がありました。
# 
# 要望 i
# : 西から ai 番目の島と西から bi
# 
# 番目の島の間で争いが起こったために、これらの島をいくつかの橋を渡って行き来できないようにしてほしい
# 
# あなたは橋をいくつか取り除くことでこれら M
# 
# 個の要望全てを叶えることにしました。
# 
# 取り除く必要のある橋の本数の最小値を求めてください。
# 問題文
# 
# 東西一列に並んだ N
# 個の島と N−1
# 
# 本の橋があります。
# 
# i
# 番目の橋は、西から i 番目の島と西から i+1
# 
# 番目の島を接続しています。
# 
# ある日、いくつかの島同士で争いが起こり、島の住人たちから M
# 
# 個の要望がありました。
# 
# 要望 i
# : 西から ai 番目の島と西から bi
# 
# 番目の島の間で争いが起こったために、これらの島をいくつかの橋を渡って行き来できないようにしてほしい
# 
# あなたは橋をいくつか取り除くことでこれら M
# 
# 個の要望全てを叶えることにしました。
# 
# 取り除く必要のある橋の本数の最小値を求めてください。
# 制約
# 入力は全て整数である
# 
# 2≤N≤105
# 1≤M≤105
# 1≤ai<bi≤N
# 組 (ai,bi)
# は全て異なる

# In[7]:


n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    
for i in range(m):
    if a[i] > b[i]:
        tem = a[i]
        a[i] = b[i]
        b[i] = tem
b.sort()

