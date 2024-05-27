import Credentials as Cr


# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Replace these values with your actual API credentials
client_id = Cr.client_id;
secret_key = Cr.secret_key;
redirect_uri = Cr.redirect_url;
response_type = "code"  
state = "sample_state"


#Stop here



uri = 'https://trade.fyers.in/?s=ok&code=200&auth_code=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE3MTY2OTIyOTUsImV4cCI6MTcxNjcyMjI5NSwibmJmIjoxNzE2NjkxNjk1LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUjE5NjU0Iiwib21zIjoiSzEiLCJoc21fa2V5IjoiMDMyZWRlYWViZTBmOTNmZjdjNTFkYjA2NjBjOGY4OGM1OWNkY2VhYTQ4YjFjNjEwNDM4M2MzMjciLCJub25jZSI6IiIsImFwcF9pZCI6IjBJUkg3SzRVWk4iLCJ1dWlkIjoiYWU4NzQxZTMyNWVmNDI4YmEyYzc2ZWY0YTI0NzEyZTgiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.AeTatpv_6ErhnOPVISqPTCpsj__fW11QP3va8BuksiI&state=None';
s1          =   uri.split('auth_code=');


auth        =   s1[1].split('&state')[0];


# The authorization code received from Fyers after the user grants access
auth_code   = auth;
grant_type  = "authorization_code" 

# Create a session object to handle the Fyers API authentication and token generation
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key, 
    redirect_uri=redirect_uri, 
    response_type=response_type, 
    grant_type=grant_type
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token();
access_token = response['access_token']
print(access_token)

