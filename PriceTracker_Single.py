import time
import datetime
import pybithumb

# List of coins
coin_list = ['COLA']


price_old = 0
while True:
    for i,coin in enumerate(coin_list):
        # Get time and price
        now = datetime.datetime.now()
        price = pybithumb.get_current_price(coin)
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

        # Compare old and current prices
        if price_old != 0:
                pass
                if price_old > price:
                    percentage =((price - price_old) / price_old) * 100
                    print(nowDatetime,coin,'Down',round(percentage,2),'%')
                    #print(nowDatetime,'Down',price_old, price,round(percentage,2))
                elif price_old < price:
                    percentage =((price - price_old) / price_old) * 100
                    print(nowDatetime,coin,'UP',round(percentage,2),'%')
                    #print(nowDatetime,'Down',price_old, price,round(percentage,2))
                elif price_old == price:
                    pass
                  
        # Save old price
        price_old = float(price)
