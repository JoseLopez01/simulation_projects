import numpy as np
import scipy.stats as st

numbers = np.array([59,12,19,5,59,58,83,18,36,00,61,47,24,41,42,98,23,67,84,43,29,71,88,74,60,10,46,23,15,11,78,31,11,91,99,57,28,18,32,21,12,95,38,76,7,96,33,63,10,5])
n = len(numbers)
mean = np.mean(numbers)

above_mean = np.count_nonzero(numbers > mean)
below_mean = np.count_nonzero(numbers < mean)

runs = 1
current_sign = numbers[0] > mean
for sign in (numbers > mean):
  if sign != current_sign:
    runs += 1
    current_sign = sign

product = 2 * above_mean * below_mean
sum = above_mean + below_mean

u = (product / sum) + 1
sigma = np.sqrt((product * (product - n)) / (pow(n, 2) * (n - 1)))
observed_z = (runs - u) / sigma
theoretical_z = st.norm.ppf(0.95)

answer = 'REJECTED' if np.abs(observed_z) >= theoretical_z else 'ACCEPTED'
print('Randomness hypothesis is ' + answer)