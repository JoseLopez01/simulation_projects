import numpy as np

numbers = np.array([0.000008, 0.131538, 0.755605, 0.458650, 0.532767, 0.218959, 0.047045, 0.678865, 0.679296, 0.934693, 0.383502, 0.519416, 0.830965, 0.034572, 0.053462, 0.529700, 0.671149, 0.007698, 0.383416, 0.066842])

ordered_numbers = np.sort(numbers)
n = len(ordered_numbers)

temp_max = []
for i in range(1, len(numbers) + 1):
  first_value = ordered_numbers[i - 1] - ((i - 1) / n)
  second_Value =  (i / n) - ordered_numbers[i - 1]
  temp_max.append(np.max([first_value, second_Value]))

print(np.max(temp_max))