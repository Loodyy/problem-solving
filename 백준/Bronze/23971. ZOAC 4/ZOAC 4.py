from math import ceil
h, w, n, m = map(int, input().split())

wc = ceil(w / (1+m))
hc = ceil(h / (1+n))
print(wc * hc)