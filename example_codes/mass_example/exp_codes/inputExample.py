#!/usr/bin/env python
# print('hello  world')

"""
程序：购物车程序
需求：
    1、启动程序后，让用户输入工资，然后打印商品列表
    2、允许用户根据商品编号购买商品
    3、用户选择商品后，检测余额是否足够，足够就直接扣款，不够就提醒
    4、课随时退出，退出时，打印已购买商品和余额

基本逻辑：
    定义商品信息的列表 
    输入工资，格式化打印商品信息
    通过列表信息对工资做判断和减法
    购买商品时通过一个新的列表保存已购买的商品
"""


salary = int(input("请输入你的工资："))
products = ['', [1, '华为荣耀9', 1500], [2, '小米手环', 100], [3, 'PS4', 3000], [4, 'iphone', 6000], [5, 'MAC', 10000],
            [6, '特斯拉', 800000], [7, 'GTX1060', 2000]]
bought = []
bought_number = 0
user_input = ''
while user_input != 'q':
    product_info = '''
    ---------------------产品清单---------------------

    {product1}
    {product2}
    {product3}
    {product4}
    {product5}
    {product6}
    {product7}

    '''.format(product1=products[1], product2=products[2], product3=products[3], product4=products[4],
               product5=products[5], product6=products[6], product7=products[7])
    print(product_info)
    user_input = input("请输入您想要购买的商品，退出购买请输入q或Q: ")
    try:
        if int(user_input) in range(1, 8):
            product_numb = int(user_input)
            product_price = int(products[product_numb][2])
            print('您选购的是:')
            print(products[product_numb])
            print('它的价格是：' + str(product_price) + '元')
            if salary > product_price:
                salary = salary - product_price
                bought.append(products[product_numb])
                bought_number = bought_number + 1
                print('您已购买如下商品：')
                print('-----------------')
                for i in bought:
                    print(i)
                print('您的余额为' + str(salary))
            else:
                print('您的余额不足，请重新选购商品')
            continue
        else:
            print('您输入的商品不存在，请重新输入')
    except:
        if str(user_input) in ['q', 'Q']:
            break
        else:
            print('您的输入有误，请重新输入')
            continue
