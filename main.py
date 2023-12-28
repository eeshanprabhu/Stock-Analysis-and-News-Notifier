import requests
from twilio.rest import Client

STOCK = "IBM"
COMPANY_NAME = "IBM"
account_sid = 'ACf898c1cf443a09afea4c7a52bd9fdf3f'
auth_token = 'f1c24b809495f1e141f55974bd27d5aa'

stock_parameters={
    'function':'TIME_SERIES_INTRADAY',
    'symbol':STOCK,
    'interval':'60min',
    'apikey':'742YQPVXP33X7AWG'
}
stock_response=requests.get(url="https://www.alphavantage.co/query",params=stock_parameters)
stock_data=stock_response.json()

opening=round(float(stock_data["Time Series (60min)"]["2023-12-27 04:00:00"]["1. open"]),2)
closing=round(float(stock_data["Time Series (60min)"]["2023-12-26 19:00:00"]["4. close"]),2)

percent=((closing-opening)/opening)*100

if percent<0:
    percent*=-1


if percent<5:
    news_generated=True

if news_generated:
    news_response=requests.get(url="https://newsapi.org/v2/everything?q=IBM&from=2023-12-01&sortBy=publishedAt",params={"apiKey":'32eb2e0fd1b948d3a4657579a4b3356b'})
    news_data=news_response.json()
    print(news_data)
    NEWS=[]
    for i in range(3):
        print(i+1)
        headline=f'headline:{news_data["articles"][i]["title"]}'
        brief=f'brief{news_data["articles"][i]["description"]}'
        NEWS.append(headline)
        NEWS.append(brief)
print(NEWS)


if news_generated:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12059272082',
        body=f"{NEWS}",

        to='+917767986722'
    )
    print(message.status)
