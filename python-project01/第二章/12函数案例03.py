#根据传入的一批商品信息(商品名,价格,数量)、优惠(优惠券,积分抵扣有)、运费信息  计算订单总金额
#规则1: 优惠券需商品金额满5000可使用,且优惠金额不饿能超过商品总价
#规则2: 积分抵扣需要商品金额满5k可使用 100积分抵1R(且抵扣金额不可超过商品总价,积分只能整百抵扣)
def cal(*args,coupon,score,express):
    # 用元组来储存商品信息  ("鼠标",188,2)
    total_price=[goods[1]*goods[2] for goods in args]
    total_cost=sum(total_price)

    #扣减优惠券
    if total_cost>5000 and coupon<=total_cost:
        total_cost=total_cost-coupon

    #扣减积分抵扣
    if total_cost>=5000 and score//100<+total_cost:
        total_cost=total_cost-score//100

    #添加运费
    total_cost+=express
    return total_cost

total=cal(("鼠标",188,2),("键盘",388,1),("手机",3999,1),coupon=10,score=4000,express=9.9)
#要么不定长参数放在最后  要么采用关键词
print(total)