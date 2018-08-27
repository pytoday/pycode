#/usr/bin/python
while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print("Pls enter your age(Just number allowed):")

while True:
    print("Enter you password:")
    passwd = input()
    if passwd.isalnum():
        break
    print("Pls input you password(Just number and letters allowed):")

print("Your age: %d. Your passwd: %s" %(int(age), passwd))
