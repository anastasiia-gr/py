def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))

    if discount>=100:
         p_w_d= price
    else:
        p_w_d= price - price*discount/100
    print(p_w_d)

discounted(50,50)
