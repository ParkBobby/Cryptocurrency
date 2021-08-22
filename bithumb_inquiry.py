import pybithumb
import time
con_key = "Your_Key"
sec_key = "Your_Key"
bithumb = pybithumb.Bithumb(con_key,sec_key)
print(bithumb.get_tickers())
print("\n")
for ticker in bithumb.get_tickers():
    balance = bithumb.get_balance(ticker)
    if balance[0] != 0:
        print(ticker, " \t ", balance)
    time.sleep(0.5)
