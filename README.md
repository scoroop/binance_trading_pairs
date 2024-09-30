# binance_trading_pairs
Binance spot trading USDT pairs list

To obtain up to date spot USDT trading pairs as a tradingview list: 
1. Use any rest client (for exmaple restninja.io or Thunder Client plugin for Visual Studio Code) and execute GET query to https://api.binance.com/api/v3/exchangeInfo without any params.
2. Save output as json file (for example binance.json)
3. Install python
4. Execute generate_tradingview_list.py script with a command "python generate_tradingview_list.py -input binance.json -output name_it_as_you_want.txt"
5. Import file in Tradingview
