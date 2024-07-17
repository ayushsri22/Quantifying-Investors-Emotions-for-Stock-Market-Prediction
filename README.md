# Quantifying-Investors-Emotions-for-Stock-Market-Prediction
In this project we did:
Learnt about behavioral finance field by extending the understanding of the link between market behavior and emotional states
Explored whether firm-specific investor emotions can effectively predict daily stock price movements.
Scrapped and preprocessed tweets’ data of 4 firms listed on London Stock Exchange from Stocktwits(investors’ social
media)
Employed an NLP based open source tool,Emtract model that extracts emotions from social media text and assigns each message a probability for 7 emotional states: neutral, happy, sad, anger, disgust, surprise. and fear.
Used yahoo finance API to get values of financial metrics like open,close returns,market cap,volume,market volatility.
Implemented Ordinary Least Squares (OLS) regression model with feature engineering and outlier removal to predict daily return values using previous day’s returns, 20-day returns, and emotion variables.
Got an R-squared value of 0.58 for the model and a correlation value of 0.76 indicating a strong linear relationship and predictive accuracy.
Observed a heightened interest among social media investors in firms characterized by larger trading volumes, higher volatility, greater market capitalizatio
