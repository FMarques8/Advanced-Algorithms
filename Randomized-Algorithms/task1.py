import random
import statistics

def toss_coin():
    return random.randint(0,1)

def toss_dice():
    return random.randint(1,6)

# heads = 0, tails = 1
n = 3


attempts=10000
outcomes_coin=[]

for at in range(attempts):
    results_coin={'H':0, 'T':0}
    for i in range(1,n+1):
        if toss_coin()==0:
            results_coin['H']+=1
        else:
            results_coin['T']+=1

        if results_coin['H']==2 or results_coin['T']==2:
            outcomes_coin.append(i+1)
            break

#print(statistics.mean(outcomes_coin))

n = 7
outcomes_dice=[]
for at in range(attempts):
    results_dice={1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(1,n+1):
            results_dice[toss_dice()]+=1
            if 2 in list(results_dice.values()):
                outcomes_dice.append(i+1)
                break

#print(statistics.mean(outcomes_dice))

for i in range(max(outcomes_dice)):
    ocur = sum([1 for x in outcomes_dice if x == i+1])
    print("Number of occurrences: ", ocur)
    print("Probability of {i} repetitions".format(i = i+1))
    print(ocur/len(outcomes_dice))

def random_day():
    return random.randint(1,365)

attempts = 10000
n = 366
outcomes_days=[]
for at in range(attempts):
    results_days={x:0 for x in range(366)}
    for i in range(1,n+1):
            results_days[random_day()]+=1
            if 2 in list(results_days.values()):
                outcomes_days.append(i+1)
                break

#print(statistics.mean(outcomes_days))

# print("Repeating the experiment {attempts} times".format(attempts = attempts))
# for i in range(1,366):
#     ocur = sum([1 for x in outcomes_days if x == i+1])
#     print("Number of occurrences: ", ocur)
#     print("Probability of {i} repetitions".format(i = i+1))
#     print(ocur/len(outcomes_days))
# print(outcomes_days)


#### Repeating experiment until we have atleast 1 of each side

attempts = 1000
n=100
for at in range(attempts+1):
    results_coin={'H':0, 'T':0}
    for i in range(1,n+1):
        if toss_coin()==0:
            results_coin['H']+=1
        else:
            results_coin['T']+=1

        if 0 not in list(results_coin.values()):
            outcomes_coin.append(i+1)
            break

# print("Repeating the experiment {attempts} times".format(attempts = attempts))
# for i in range(1,max(outcomes_coin)):
#     ocur = sum([1 for x in outcomes_coin if x == i+1])
#     print("Number of occurrences: ", ocur)
#     print("Probability of {i} repetitions".format(i = i+1))
#     print(round(ocur/len(outcomes_coin),3))


attempts = 100000
outcomes_dice2 = []
for at in range(attempts+1):
    results_dice2={x:0 for x in range(1,7)}
    i = 1
    while 0 in list(results_dice2.values()):
            results_dice2[toss_dice()] += 1
            i+=1
    outcomes_dice2.append(i)

                

print(outcomes_dice2)

print("Repeating the experiment {attempts} times".format(attempts = attempts))
for i in range(1,max(outcomes_dice2)+1):
    ocur = sum([1 for x in outcomes_dice2 if x == i+1])
    print("Number of occurrences: ", ocur)
    print("Probability of {i} repetitions".format(i = i+1))
    print(round(ocur/len(outcomes_dice2),3))