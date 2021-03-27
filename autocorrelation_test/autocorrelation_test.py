import numpy as np
import scipy.stats as st

numbers = np.array([0.13,0.91,0.11,0.02,0.65,0.33,0.86,0.05,0.25,0.28,0.80,0.82,0.10,0.78,0.88,0.76,0.29,0.20,0.66,0.17,0.71,0.45,0.40,0.35])

i = int(input("Enter i \n"))
m = int(input("Enter autocorrelation amplitude \n"))
n = len(numbers)
M = np.trunc((n - i) / m) - 1

print('-----------------------------')
sum = 0
for j in range(i - 1, n, m):
  if j + m < n:
    print(str(numbers[j]) + ' * ' + str(numbers[j + m]))
    sum += numbers[j] * numbers[j + m]

pim = (1 / (M + 1)) * sum
standard_deviation =  np.sqrt((13 * M) + 7) / (12 * (M + 1))
observed_z =  (pim - 0.25) / standard_deviation
theoritical_z = st.norm.ppf(0.95)

print('-----------------------------')
if observed_z == 0:
  print("The RNG's are not random")
elif observed_z != 0:
  print("The RNG's are random")
elif np.abs(observed_z) > theoritical_z:
  print("The null hypothesis is rejected")