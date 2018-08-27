#!/usr/bin/env python3
# coding=utf-8
# title          :readCensusExcel.py
# description    :Tabulates population and number of census tracts for each county
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/6/15 15:14:54
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import os,openpyxl, pprint

print('Opening workbook....')
wb = openpyxl.load_workbook('D:\\Codes\\PythonApplication1\\py\\automate_online-materials\\censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# TODO: Fill in countyData with each county's population and tracts.
print('Reading rows....')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exists.
    countyData.setdefault(state, {})
    # Make sure the key for this county in this staste exists.
    countyData[state].setdefault(county, {'tracts':0, 'pop':0})

    # Each row represetns one cnesus tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    # Increase the conty pop by the pop in this census tract.
    countyData[state][county]['pop'] += 1

# TODO: Open a new text file and write the contents of countyData to it
print('Print writing results...')
os.chdir('D:\\Codes\\PythonApplication1\\PythonApplication1')
resultFile = open('census2017.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
