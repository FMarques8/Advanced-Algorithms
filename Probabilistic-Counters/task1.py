import random
import statistics

events = {}

n = 10000
for i in range(n): #trials
    c = 0
    for i in range(10000): #events
        if random.randint(0, 32) == 32:
            c += 1
    if c not in events.keys():
        events[c] = 0
    else:
        events[c] += 1   

for k in sorted(list(events.keys())):
    if events[k] == 0:
        continue
    print("counter value: {k} - {v} times - {per}%".format(k = k, v = events[k], per = round(events[k]/n,4) * 100))

print(statistics.mean(events))
print(statistics.variance(events))
print(statistics.stdev(events))

