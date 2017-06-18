from die import Die

'''Create a six_sided die.'''
die = Die()

'''make rolls and store results in a list named results'''
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

frequencies = []
for value in range(1, die.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
