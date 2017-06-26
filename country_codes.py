from pygal.maps.world import COUNTRIES

'''
def get_country_code(country_name):
    "give a country, retrieve its 2-digit country code"
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        else:
            return None
'''
def get_country_code(country_name):


    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
# If the country wasn't found, return None.
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
