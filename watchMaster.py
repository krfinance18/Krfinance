import pandas as pd



watchlist =["NSE:AARTIIND-EQ",
"NSE:ABB-EQ",
"NSE:ABBOTINDIA-EQ",
"NSE:ABCAPITAL-EQ",
"NSE:ABFRL-EQ",
"NSE:ACC-EQ",
"NSE:ADANIENT-EQ",
"NSE:ADANIPORTS-EQ",
"NSE:ALKEM-EQ",
"NSE:AMBUJACEM-EQ",
"NSE:APOLLOHOSP-EQ",
"NSE:APOLLOTYRE-EQ",
"NSE:ASHOKLEY-EQ",
"NSE:ASIANPAINT-EQ",
"NSE:ASTRAL-EQ",
"NSE:ATUL-EQ",
"NSE:AUBANK-EQ",
"NSE:AUROPHARMA-EQ",
"NSE:AXISBANK-EQ",
"NSE:BAJAJ-AUTO-EQ",
"NSE:BAJAJFINSV-EQ",
"NSE:BAJFINANCE-EQ",
"NSE:BALKRISIND-EQ",
"NSE:BALRAMCHIN-EQ",
"NSE:BANDHANBNK-EQ",
"NSE:BANKBARODA-EQ",
"NSE:BATAINDIA-EQ",
"NSE:BEL-EQ",
"NSE:BERGEPAINT-EQ",
"NSE:BHARATFORG-EQ",
"NSE:BHARTIARTL-EQ",
"NSE:BHEL-EQ",
"NSE:BIOCON-EQ",
"NSE:BOSCHLTD-EQ",
"NSE:BPCL-EQ",
"NSE:BRITANNIA-EQ",
"NSE:BSOFT-EQ",
"NSE:CANBK-EQ",
"NSE:CANFINHOME-EQ",
"NSE:CHAMBLFERT-EQ",
"NSE:CHOLAFIN-EQ",
"NSE:CIPLA-EQ",
"NSE:COALINDIA-EQ",
"NSE:COFORGE-EQ",
"NSE:COLPAL-EQ",
"NSE:CONCOR-EQ",
"NSE:COROMANDEL-EQ",
"NSE:CROMPTON-EQ",
"NSE:CUB-EQ",
"NSE:CUMMINSIND-EQ",
"NSE:DABUR-EQ",
"NSE:DALBHARAT-EQ",
"NSE:DEEPAKNTR-EQ",
"NSE:DIVISLAB-EQ",
"NSE:DIXON-EQ",
"NSE:DLF-EQ",
"NSE:DRREDDY-EQ",
"NSE:EICHERMOT-EQ",
"NSE:ESCORTS-EQ",
"NSE:EXIDEIND-EQ",
"NSE:FEDERALBNK-EQ",
"NSE:GAIL-EQ",
"NSE:GLENMARK-EQ",
"NSE:GMRINFRA-EQ",
"NSE:GNFC-EQ",
"NSE:GODREJCP-EQ",
"NSE:GODREJPROP-EQ",
"NSE:GRANULES-EQ",
"NSE:GRASIM-EQ",
"NSE:GUJGASLTD-EQ",
"NSE:HAL-EQ",
"NSE:HAVELLS-EQ",
"NSE:HCLTECH-EQ",
"NSE:HDFCAMC-EQ",
"NSE:HDFCBANK-EQ",
"NSE:HDFCLIFE-EQ",
"NSE:HEROMOTOCO-EQ",
"NSE:HINDALCO-EQ",
"NSE:HINDCOPPER-EQ",
"NSE:HINDPETRO-EQ",
"NSE:HINDUNILVR-EQ",
"NSE:ICICIBANK-EQ",
"NSE:ICICIGI-EQ",
"NSE:ICICIPRULI-EQ",
"NSE:IDEA-EQ",
"NSE:IDFC-EQ",
"NSE:IDFCFIRSTB-EQ",
"NSE:IEX-EQ",
"NSE:IGL-EQ",
"NSE:INDHOTEL-EQ",
"NSE:INDIACEM-EQ",
"NSE:INDIAMART-EQ",
"NSE:INDIGO-EQ",
"NSE:INDUSINDBK-EQ",
"NSE:INDUSTOWER-EQ",
"NSE:INFY-EQ",
"NSE:IOC-EQ",
"NSE:IPCALAB-EQ",
"NSE:IRCTC-EQ",
"NSE:ITC-EQ",
"NSE:JINDALSTEL-EQ",
"NSE:JKCEMENT-EQ",
"NSE:JSWSTEEL-EQ",
"NSE:JUBLFOOD-EQ",
"NSE:KOTAKBANK-EQ",
"NSE:LALPATHLAB-EQ",
"NSE:LAURUSLABS-EQ",
"NSE:LICHSGFIN-EQ",
"NSE:LT-EQ",
"NSE:LTF-EQ",
"NSE:LTIM-EQ",
"NSE:LTTS-EQ",
"NSE:LUPIN-EQ",
"NSE:MANAPPURAM-EQ",
"NSE:MARICO-EQ",
"NSE:MARUTI-EQ",
"NSE:MCDOWELL-N-EQ",
"NSE:MCX-EQ",
"NSE:METROPOLIS-EQ",
"NSE:MFSL-EQ",
"NSE:MGL-EQ",
"NSE:MOTHERSON-EQ",
"NSE:MPHASIS-EQ",
"NSE:MRF-EQ",
"NSE:MUTHOOTFIN-EQ",
"NSE:NATIONALUM-EQ",
"NSE:NAUKRI-EQ",
"NSE:NAVINFLUOR-EQ",
"NSE:NESTLEIND-EQ",
"NSE:NMDC-EQ",
"NSE:NTPC-EQ",
"NSE:OBEROIRLTY-EQ",
"NSE:OFSS-EQ",
"NSE:ONGC-EQ",
"NSE:PAGEIND-EQ",
"NSE:PEL-EQ",
"NSE:PERSISTENT-EQ",
"NSE:PETRONET-EQ",
"NSE:PFC-EQ",
"NSE:PIDILITIND-EQ",
"NSE:PIIND-EQ",
"NSE:PNB-EQ",
"NSE:POLYCAB-EQ",
"NSE:POWERGRID-EQ",
"NSE:PVRINOX-EQ",
"NSE:RAMCOCEM-EQ",
"NSE:RBLBANK-EQ",
"NSE:RECLTD-EQ",
"NSE:RELIANCE-EQ",
"NSE:SAIL-EQ",
"NSE:SBICARD-EQ",
"NSE:SBILIFE-EQ",
"NSE:SBIN-EQ",
"NSE:SHREECEM-EQ",
"NSE:SHRIRAMFIN-EQ",
"NSE:SIEMENS-EQ",
"NSE:SRF-EQ",
"NSE:SUNPHARMA-EQ",
"NSE:SUNTV-EQ",
"NSE:SYNGENE-EQ",
"NSE:TATACHEM-EQ",
"NSE:TATACOMM-EQ",
"NSE:TATACONSUM-EQ",
"NSE:TATAMOTORS-EQ",
"NSE:TATAPOWER-EQ",
"NSE:TATASTEEL-EQ",
"NSE:TCS-EQ",
"NSE:TECHM-EQ",
"NSE:TITAN-EQ",
"NSE:TORNTPHARM-EQ",
"NSE:TRENT-EQ",
"NSE:TVSMOTOR-EQ",
"NSE:UBL-EQ",
"NSE:ULTRACEMCO-EQ",
"NSE:UPL-EQ",
"NSE:VEDL-EQ",
"NSE:VOLTAS-EQ",
"NSE:WIPRO-EQ",
"NSE:ZEEL-EQ",
"NSE:ZYDUSLIFE-EQ"]


