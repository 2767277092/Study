# 字典
# 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车：要求用户输入要修改的购物车商品名称，然后提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx，商品价格：xxx，商品数量：xxx”。
# 5.推出购物车
# shopping_cart={"mate80":{"price:8000","num":2},"GPW":{}}

shopping_cart={}
# 1.制作菜单
print("欢迎使用购物车管理系统")
menu="""
###############购物车系统##################
#             1.添加购物车                #
#             2.修改购物车                #
#             3.删除购物车                #
#             4.查询购物车                #
#########################################
"""
print(menu)
# shopping_cart={"mate80":{"price:8000","num":2},"GPW":{}}

while True:
    choice = input("请选择要进行的操作(1-5)")
    match choice:
        case "1":
            name = input("请输入商品名称")
            price1 = float(input("请输入商品价格"))
            num1 = int(input("请输入商品数量 "))
            # 若商品存在,则不执行添加
            if name in shopping_cart:
                print("该商品已存在 无需添加")
            else:
                shopping_cart[name] = {"price": price1, "num": num1}
                print("商品添加完成")

        case "2":  # 修改购物车
            name = input("请输入要修改的商品名称")
            # price1 = float(input("请输入商品最新的价格"))
            # num1 = int(input("请输入商品最新的数量 "))
            # # 判断是否存在
            # if name not in shopping_cart:
            #     print("该商品不存在,请重新选择")
            # else:
            #     shopping_cart[name] = {"price": price1, "num": num1}
            #     print("商品修改完毕")


            #改良版
            if name not in shopping_cart:
                print("该商品不存在,请重新选择")
            price1 = float(input("请输入商品最新的价格"))
            num1 = int(input("请输入商品最新的数量 "))
        #     省略一个else 并且优化Input

        case "3":  # 删除购物车
            name = input("请输入")
            # 判断商品是否存在
            if name in shopping_cart:
                del shopping_cart[name]

            else:
                print("商品不在购物车")
        case "4":  # 查询购物车
            for name in shopping_cart.keys():
                information = shopping_cart[name]
                print(f"商品名称:{name},商品价格:{information["price"]},商品数量:{information['num']}")
        case "5":  # 退出购物车
            break
        case _:
            print("不支持该操作")