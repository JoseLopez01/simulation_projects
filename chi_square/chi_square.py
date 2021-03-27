import numpy as np
from numpy.core.numeric import count_nonzero

numbers = np.array([0.1791, 0.1010, 0.8558, 0.7294, 0.6464, 0.2891, 0.8648, 0.8378, 0.8910, 0.7127, 0.3354, 0.3856, 0.9458, 0.2870, 0.2691, 0.6123, 0.4133, 0.8251, 0.1766, 0.7554]);
n = len(numbers)
k = int(np.sqrt(n))
numbers_of_expected_values = n / k

steps = 1 / k
interval_min = 0
interval_max = steps

counts = []

while interval_max <= 1:
  key = f'{interval_min} - {interval_max}'
  counts.append([key, np.count_nonzero(numbers < interval_max)])
  interval_min = interval_max
  interval_max += steps

sum = 0

for key, value in dict(counts).items():
  sum += ((value - numbers_of_expected_values) ** 2) / numbers_of_expected_values

print(sum)
