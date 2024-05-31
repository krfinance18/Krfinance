import Credentials as Cre
import access as AT
import pandas as pd
from datetime import date
from datetime import timedelta

from fyers_apiv3 import fyersModel


client_id       = Cre.client_id;
access_token    = AT.at;

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

watchlist = ["NSE:HAVELLS24MAY1900CE","NSE:RELIANCE-EQ"]
#filter both equity, contract
#monthly -- 700 --save fyres free
#
#watchlist = ["NSE:PERSISTENT24MAY3700CE"]
print(watchlist)
data = {
        "symbol": watchlist[0],
        "resolution":"1",
        "date_format":"1",
        "range_from":"2024-05-27",
        "range_to":"2024-05-28",
        "cont_flag":"1"
    }
response = fyers.history(data=data)
data1 = response['candles']
df = pd.DataFrame(data1)
df['Symbol'] = watchlist[0];

df.columns = ['date','open','high','low','close','volume','Symbol']
df['date'] = pd.to_datetime(df['date'], unit = 's')
df.date=(df.date.dt.tz_localize('UTC')).dt.tz_convert('Asia/Kolkata')
df['date']=df['date'].dt.tz_localize(None)
df = df.set_index('date')
df['x'] = df['close']-df['low']
print(df)


#today = date.today();
#yesterday = today - timedelta(days = 1);


#data1 = {
#        "symbol": watchlist[0],
#       "resolution":"5",
#        "date_format":"1",
#        "range_from":"2024-05-24",
#        "range_to":"2024-05-26",
#        "cont_flag":"1"
#        }
#    response = fyers.history(data=data)
#    data1 = response['candles']
#    df = pd.DataFrame(data1)
#    df['Symbol'] = watchlist[0];
    #df2 = pd.DataFrame({'symbol':[i]})
#    df.columns = ['date','open','high','low','close','volume','Symbol']
#    df['date'] = pd.to_datetime(df['date'], unit = 's')



#print(df)










