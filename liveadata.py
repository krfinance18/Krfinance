from pkg_resources import resource_filename
from fyers_apiv3.FyersWebsocket import data_ws
import access as at
import watchMaster as watch
import WatchSocket as watchSocket
import checkHigh as checkHigh


def onmessage(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    
    symbbol1    = message['symbol']
    price       = message['ltp']
    high        = message['high_price']
    checkHigh.checkHigh.HighValue(symbbol1,price,high)
    #print(symbbol1,price,vol,)
    print("Response:", message)


def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.


    """
    print("Error:", message)


def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)


def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "SymbolUpdate"
    # data_type = "DepthUpdate"


    # Subscribe to the specified symbols and data type
    # Code To assign Historical Values
    
    
    symbols = ['NSE:INFY24JUNFUT','NSE:AARTIIND-EQ','NSE:ABB-EQ','NSE:ABBOTINDIA-EQ','NSE:ABCAPITAL-EQ','NSE:ABFRL-EQ','NSE:ACC-EQ','NSE:ADANIENT-EQ','NSE:ADANIPORTS-EQ']
    fyers.subscribe(symbols=symbols, data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()


# Replace the sample access token with your actual access token obtained from Fyers
access_token = at.at;

# Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
    access_token=access_token,       # Access token in the format "appid:accesstoken"
    log_path="",                     # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=False,                  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,              # Save response in a log file instead of printing it.
    reconnect=True,                  # Enable auto-reconnection to WebSocket on disconnection.
    on_connect=onopen,               # Callback function to subscribe to data upon connection.
    on_close=onclose,                # Callback function to handle WebSocket connection close events.
    on_error=onerror,                # Callback function to handle WebSocket errors.
    on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)

# Establish a connection to the Fyers WebSocket
fyers.connect()