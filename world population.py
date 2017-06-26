import json
from country_codes import get_country_code
from pygal.maps.world import World

#load the data into a list
filename  = "C:\\Users\\Asymmetry\\Desktop\\population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

cc_pop_1, cc_pop_2, cc_pop_3, cc_populations = {}, {}, {}, {}
#print 2010 population for each country
for pop_dic in pop_data:
    if pop_dic["Year"] == "2010":
        country_name = pop_dic["Country Name"]
        population = int(float(pop_dic["Value"]))
        code = get_country_code(country_name)
        
        if code:
            cc_populations[code] = population


for cd, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cd] = pop
    elif pop < 1000000000:
        cc_pop_2[cd] = pop
    else: cc_pop_3[cd] = pop

 
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add("0-10m", cc_pop_1)
wm.add("10m-1bn", cc_pop_2)
wm.add(">1bn", cc_pop_3)


wm.render_to_file("C:\\Users\\Asymmetry\\Desktop\\world_populations.svg")
