#collatz()
def collatz(number):
    if number%2 == 1 and number > 1:
        print(3*number+1)
        collatz(3*number+1)
    elif number%2 == 0:
        print(number//2)
        collatz(number//2)


while True:
    n = input('请输入一个数字:')
    try:
        int(n)
    except ValueError:
        print('输入类型错误，请重新输入。')
        continue
    break
arg = int(n)

collatz(arg)

