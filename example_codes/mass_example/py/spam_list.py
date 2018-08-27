#/usr/bin/env python3
a = ['apples', 'bananas', 'tofu', 'cats', 'test']

def plist(spam):
    
    for i in range(len(spam)-1):
        print(spam[i] + ', ', end="")
    print('and ' + spam[(len(spam)-1)])

plist(a)
