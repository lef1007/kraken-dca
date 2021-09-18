
# 引入ccxt这个图书馆
import ccxt
# 从pprint图书馆中引入pprint这个method
from pprint import pprint
import sys
import time
from getpass import getpass

# print(sys.argv)
# easier for the user to specified the market, and operate in terminal。
# 如果不写这个line的话，每次用terminal的时候，想查其他的cypto market的话，之后的line就需要改变。 
MARKET_SYMBOL = sys.argv[1]
MARKET_SYMBOL = MARKET_SYMBOL.upper()
BASE_CURRENCY = MARKET_SYMBOL.split("/")[0]
QUOTE_CURRENCY = MARKET_SYMBOL.split("/")[1]

kraken = ccxt.kraken()

kraken.apiKey = sys.argv[2]
kraken.secret = getpass("🔑 Kraken API private key: ")

my_balance = kraken.fetch_balance()
# pprint(my_balance)

base_balance = my_balance.get(BASE_CURRENCY)
quote_balance = my_balance.get(QUOTE_CURRENCY)
# print(base_balance)

total_base_balance = base_balance.get("total")
total_quote_balance = quote_balance.get("total")
# print(total_base_balance)

print(f"💰 Total {BASE_CURRENCY} balance is {total_base_balance}.")
print(f"💸 Total {QUOTE_CURRENCY} balance is {total_quote_balance}.")

# kraken_markets = kraken.fetch_markets()
# for market in kraken_markets:
#     if market.get("symbol") == MARKET_SYMBOL:
#         pprint(market)

market_ticker = kraken.fetch_ticker(MARKET_SYMBOL)
# pprint(market_ticker)
market_price = market_ticker.get("last")
print(f"📈 The last price of {BASE_CURRENCY} is {market_price:,}.")

base_amount_quote_currency = sys.argv[3]
base_buy_amount = float(base_amount_quote_currency) / market_price
# 8是现实小数点后可以留8位最多，并且四舍五入
base_buy_amount = round(base_buy_amount, 6)
print(f"I'm gonna buy: {base_buy_amount} {BASE_CURRENCY} (${base_amount_quote_currency} worth of {BASE_CURRENCY.title()}).")

ONE_WEEK_IN_SEC = 3600*24*7

while True:
        
    # -TRADE Line-
    # my_order = kraken.create_order(MARKET_SYMBOL, "market", "buy", base_buy_amount)
    # pprint(my_order)

    print("😴 Sleeping for one week now...")
    time.sleep(ONE_WEEK_IN_SEC)





