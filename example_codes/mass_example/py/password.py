# swordfish
while True:
    print('Who are you?')
    name = input()
    if name != 'Jackie':
        continue
    print('Hello '+ name + ',Please input your password.')
    password = input()
    if password == 'password':
        break
print('Access granted.')
