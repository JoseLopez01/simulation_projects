from numpy import sqrt
import scipy.stats as st

numbers = [59,12,19,5,59,58,83,18,36,00,61,47,24,41,42,98,23,67,84,43,29,71,88,74,60,10,46,23,15,11,78,31,11,91,99,57,28,18,32,21,12,95,38,76,7,96,33,63,10,5]
n = len(numbers)

signs = []
for index, current_number in enumerate(numbers):
  if index + 1 < n:
    next_number = numbers[index + 1]
    signs.append(1 if next_number > current_number else -1)

runs = 1
current_sign = signs[0]
for sign in signs:
  if current_sign != sign:
    runs += 1
    current_sign = sign

u_a = ((2 * n) - 1) / 3
sigma_a_square = ((16 * n) -29) / 90
sigma_a = sqrt(sigma_a_square)

observed_z = (runs - u_a) / sigma_a
theoretical_z = st.norm.ppf(0.95)

if abs(observed_z) <= theoretical_z:
  print("The RNG's are independents and randoms")
elif abs(observed_z) > theoretical_z:
  print("The RNG's are not independents and not randoms")
