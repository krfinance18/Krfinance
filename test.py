import Credentials as Cre
import time
import access as AT
import pandas as pd
from datetime import date
from datetime import timedelta
import watchMaster as watchlist
from ta import add_all_ta_features
from ta.utils import dropna
from ta.momentum import RSIIndicator
import ta as TechA
from fyers_apiv3 import fyersModel


client_id       = Cre.client_id;
access_token    = AT.at;

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")


w = watchlist.watchlist
#print(w)
#watchlist1[]NSE:AARTIIND-EQ
Numbers =[x for x in range(4)]
#print(Numbers)
a = len(w)
#print(a)
toDay = date.today();
#fourteenDay = toDay - timedelta(days = 15);
#print(fourteenDay)

for i in Numbers:
    data = {
        "symbol": w[i],
        "resolution":"D",
        "date_format":"1",
        "range_from":"2024-05-05",
        "range_to":toDay,
        "cont_flag":"1"
    }
    response = fyers.history(data=data)
    data1 = response['candles']
    df = pd.DataFrame(data1)
    df['Symbol'] = w[i]
    df.columns = ['date','open','high','low','close','volume','Symbol']
    df['date'] = pd.to_datetime(df['date'], unit = 's')
    df.date=(df.date.dt.tz_localize('UTC')).dt.tz_convert('Asia/Kolkata')
    df['date']=df['date'].dt.tz_localize(None)
    df = df.set_index('date')
    #df2 = df[-7:]
    #df2 = pd.DataFrame()
    

print(df)
    
            
        
        
        
    
    
    
    
    
    
    
