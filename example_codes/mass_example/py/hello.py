#This program says hello and ask for my name
print('Hello world')
print('What is your name?')    #ask for their name

my_name = input()
print('It is good to see you,' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?')  #ask for their age
my_age = input()
print('You will be ' + str(int(my_age)+1) + ' in a year.')
