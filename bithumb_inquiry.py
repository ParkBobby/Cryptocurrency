import time
import pybithumb


# Type in your key
sec_key = "Your_Key"
con_key = "Your_Key"


# Bithumb API
bithumb = pybithumb.Bithumb(con_key,sec_key)


# Possessed coins
print(bithumb.get_tickers(),"\n")


# Current price of possessed coins
for ticker in bithumb.get_tickers():
    balance = bithumb.get_balance(ticker)
    if balance[0] != 0:
        print(ticker, " \t ", balance)
    time.sleep(0.5)
