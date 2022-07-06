import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

l, r = 1, max(trees)
tar = 0
while l <= r:
    mid = (l+r)//2
    cut = 0
    for tree in trees:
        if tree > mid:
            cut += tree-mid
            continue
        break

    if m <= cut:
        tar = max(tar, mid)
        l = mid+1
    else:
        r = mid-1

print(tar)