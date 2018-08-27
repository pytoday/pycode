#!/usr/bin/env python3
# coding=utf-8
# title          :world_population.py
# description    :draw population of the world
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/26 10:06
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import json
from pygal_maps_world.i18n import COUNTRIES
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle


def get_country_code(country_name):
    """get country code"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

# init country data
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    cc_population = {}

    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            country_code = get_country_code(country_name)
            if country_code:
                # print(country_code + ' : ' + str(population))
                cc_population[country_code] = population
            else:
                print(country_name + ' : ' + str(population) + ' -- No code ERROR')


# countries group by population
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for code, pop in cc_population.items():
    if pop < 10000000:
        cc_pops1[code] = pop
    elif pop < 1000000000:
        cc_pops2[code] = pop
    else:
        cc_pops3[code] = pop

# draw country map
wm_style = RotateStyle('#336699', bash_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'A world map of population'
# wm.add('NA(group of countries)', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
# wm.add("world population(2010)", cc_population)
wm.add('0-10m:'+str(len(cc_pops1)), cc_pops1)
wm.add('10m-1bn:'+str(len(cc_pops2)), cc_pops2)
wm.add('>1bn:'+str(len(cc_pops3)), cc_pops3)
wm.render_to_file('world_map.svg')
