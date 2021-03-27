import numpy as np
from collections import Counter

EXPERIMENTS_NUMBER = 10

dice_1 = np.random.randint(1, 7, size=(1, EXPERIMENTS_NUMBER))
dice_2 = np.random.randint(1, 7, size=(1, EXPERIMENTS_NUMBER))
rolls = [dice_1, dice_2]

sums = sum(rolls)
lsums = np.array(sums).tolist()
prob = 0

for key, value in Counter(lsums[0]).items():
  print(str(key) + ': ' + str(value) + ', probability: ' + str(value / EXPERIMENTS_NUMBER))
  prob += value / EXPERIMENTS_NUMBER

print('Runs: ' + str(EXPERIMENTS_NUMBER) + ', Sum of probabilities: ' + str(prob))