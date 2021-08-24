import datetime
import pybithumb

coin = "BTC"
now = datetime.datetime.now()
price = pybithumb.get_current_price(coin)

print("Current Time: ",now)
print(coin,"Price: ",price)
