from die import Die
import pygal

'''Create a six_sided die.'''
die = Die()

'''make rolls and store results in a list named results'''
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


'''visualize the results.'''
hist = pygal.Bar()
hist.title = ""
hist.x_labels = ["1","2","3","4","5","6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file("C:\\Users\\Asymmetry\\Desktop\\die_visual.svg")
