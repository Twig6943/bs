is_buyer_good_credit = False

house_price = 150

if is_buyer_good_credit :
    house_price_w_disc = house_price - 10 * (house_price / 100)
    print(house_price_w_disc)
else:
    house_price_w_disc = house_price - 20 * (house_price / 100)
    print(house_price_w_disc)

