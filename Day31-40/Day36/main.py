
import requests
from twilio.rest import Client

STOCK_NAME = "ORCL"
COMPANY_NAME = "Oracle Corporation"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing price
stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
#each date is a dictionary, need to turn that into a list
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get day before yesterday's closing price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

#Find the positive difference between yesterday's and day before yesterday's closing prices
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday
diff_percent = round((difference / float(yesterday_closing_price)) * 100)


#If percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 0: #changing to 0 here so we can continue testing the code
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}." for article in three_articles]

    #Send each article as a separate message via Twilio. 
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+17173668974",
            to="+16194306455",
        )

