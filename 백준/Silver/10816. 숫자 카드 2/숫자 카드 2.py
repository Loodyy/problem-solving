from collections import Counter

n = int(input())
cards = dict(Counter(map(int, input().split())))
m = int(input())
required = list(map(int, input().split()))
print(*[cards[re] if cards.get(re) else 0 for re in required])