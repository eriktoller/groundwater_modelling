import random

names = ["Moa", "Victor", "Andrea"]
random.shuffle(names)

from collections import Counter

results = []
num = 100000
for _ in range(num):
    random.shuffle(names)
    results.append(tuple(names))

counts = Counter(results)
labels = [f"{', '.join(order)}" for i, order in enumerate(counts.keys())]
values = [count / num * 100 for count in counts.values()]

# draw the final order
ind_rand = random.choice(results)
print("\nRandomly selected order:")
for i in range(len(ind_rand)):
    print(f"{i + 1}: {ind_rand[i]}")

print("\nDistribution of orders:")
for label, value in zip(labels, values):
    print(f"{label}: {value:.2f}%")
