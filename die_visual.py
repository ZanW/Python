from die import Die
import pygal

'''Create 2 six_sided dies.'''
die_1 = Die()
die_2 = Die()


'''make rolls and store results in a list named results'''
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

max_result = die_1.num_sides + die_2.num_sides
min_result = 1+1

frequencies = []
for value in range(min_result, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


'''visualize the results.'''
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = list(range(min_result, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6+D6", frequencies)
hist.render_to_file("C:\\Users\\Asymmetry\\Desktop\\die_visual.svg")
