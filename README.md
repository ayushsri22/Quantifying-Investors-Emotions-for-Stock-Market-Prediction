# Quantifying Investors' Emotions for Stock Market Prediction

## Project Overview
This project explores the field of behavioral finance by examining the relationship between market behavior and investor emotional states. Our goal is to determine if firm-specific investor emotions can effectively predict daily stock price movements.

## Objectives
- To understand the behavioral finance field by exploring the link between market behavior and investor emotional states.
- To investigate the potential of firm-specific investor emotions in predicting daily stock price movements, focusing on four firms listed on the London Stock Exchange, by employing the Emtract model to extract emotions from social media text.
- To retrieve financial metrics such as open, close, returns, market cap, volume, and market volatility using the Yahoo Finance API and incorporate these into an Ordinary Least Squares (OLS) regression model for predicting daily return values.
- To analyze the relationship between social media investor sentiment and firm characteristics such as trading volumes, volatility, and market capitalization.

## Data Sources
- **Social Media Data**: Tweets data from Stocktwits for 4 firms listed on the London Stock Exchange.
- **Financial Metrics**: Yahoo Finance API to fetch values such as open, close, returns, market cap, volume, and market volatility.

## Methodology
1. **Data Collection**: Scraped tweets data from Stocktwits for 4 selected firms.
2. **Data Cleaning**: Cleaned the tweet text by removing usernames, URLs, stock symbols, and non-alphanumeric characters, converted the text to lowercase, and split it into individual words. The process uses regular expressions for pattern matching and the NLTK library for text preprocessing.
3. **Emotion Extraction**: Used the Emtract model to extract emotions from the collected social media text, assigning each message a probability for 7 emotional states.
4. **Financial Data Retrieval**: Collected financial metrics(open-close returns, market capitalisation, trading volume, and market volatility) using the Yahoo Finance API.
5. **Model Implementation**: Implemented an Ordinary Least Square(OLS regression model with outlier removal to predict daily return values.
6. **Evaluation**: Evaluated the model's performance using R-squared and correlation values.

## Model Pipeline
1. **Data Preprocessing**: The dataset is loaded and preprocessed by adding the previous day's return and removing rows with missing values. Outliers are removed using the IQR method to enhance data quality.
2. **Feature Selection**: Emotion metrics, previous day's return, and control variables are selected as independent variables. These features aim to capture various factors influencing the actual return, the dependent variable.
3. **Model Training**: An OLS regression model is trained using the selected features and `actual return`, with a constant added for the intercept. The `statsmodels` library fits the model, providing regression coefficients and statistical measures.
4. **Model Evaluation**: The model's performance is evaluated using the summary of OLS results, R-squared, and the correlation between actual and predicted values. Error metrics (MAE, MSE, RMSE) quantify prediction accuracy.
5. **Prediction**: The trained model predicts `actual return`, storing the predictions in a new column. The DataFrame with predictions is saved to a new Excel file for further analysis and validation.

## Results
- **Model Performance**: Achieved an R-squared value of 0.58 and a correlation value of 0.76, indicating a strong linear relationship and predictive accuracy.
- **Investor Behavior Insights**: Noted a significant interest among social media investors in firms with larger trading volumes, higher volatility, and greater market capitalization.

## Code and Data
The repository includes:
- OLS implementation code
- Prediction database obtained using the Emtract model

## Conclusion
This project successfully demonstrates the potential of using firm-specific investor emotions, derived from social media, to predict stock price movements. The findings highlight the importance of integrating behavioral finance concepts with traditional financial metrics for enhanced market prediction.

## Acknowledgements
- Thanks to Stocktwits for providing the tweets data.
- Thanks to Yahoo Finance for the financial metrics API.
