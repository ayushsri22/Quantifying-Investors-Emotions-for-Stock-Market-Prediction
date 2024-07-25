# Quantifying Investors' Emotions for Stock Market Prediction

## Project Overview

This project explores the field of behavioral finance by examining the relationship between market behavior and investor emotional states. Our goal is to determine if firm-specific investor emotions can effectively predict daily stock price movements.

## Objectives

- Gain an in-depth understanding of the behavioral finance field by exploring the link between market behavior and investor emotional states.
- Investigate the potential of firm-specific investor emotions in predicting daily stock price movements.
- Collect and preprocess tweets data from Stocktwits, focusing on 4 firms listed on the London Stock Exchange.
- Utilize the Emtract model, an NLP-based tool, to extract emotions from social media text and assign probabilities for 7 emotional states: neutral, happy, sad, anger, disgust, surprise, and fear.
- Retrieve financial metrics such as open, close, returns, market cap, volume, and market volatility using the Yahoo Finance API.
- Develop and implement an Ordinary Least Squares (OLS) regression model, incorporating feature engineering and outlier removal techniques, to predict daily return values using previous day’s returns, 20-day returns, and emotion variables.
- Analyze the relationship between social media investor sentiment and firm characteristics such as trading volumes, volatility, and market capitalization.

## Data Sources

- **Social Media Data:** Tweets data from Stocktwits for 4 firms listed on the London Stock Exchange.
- **Financial Metrics:** Yahoo Finance API to fetch values such as open, close, returns, market cap, volume, and market volatility.

## Methodology

1. **Data Collection:** Scraped and preprocessed tweets data from Stocktwits for 4 selected firms.
2. **Emotion Extraction:** Used the Emtract model to extract emotions from the collected social media text, assigning each message a probability for 7 emotional states.
3. **Financial Data Retrieval:** Collected financial metrics using the Yahoo Finance API.
4. **Feature Engineering:** Processed and engineered features from the collected data.
5. **Model Implementation:** Implemented an OLS regression model with outlier removal to predict daily return values.
6. **Evaluation:** Evaluated the model's performance using R-squared and correlation values.

## Model Pipeline
1. **Data Preprocessing**: Handle missing values, encode categorical variables, and scale numerical features.
2. **Feature Selection**: Select the most relevant features for prediction.
3. **Model Training**: Train the Logistic Regression model on the training dataset.
4. **Model Evaluation**: Evaluate the model using accuracy, precision, R-squared value, Mean Absolute Error(MAE), Mean Squared Error(MSE), Root Mean Squared Error (RMSE).
5. **Prediction**: Use the trained model to predict customer preferences.
## Results

- **Model Performance:** Achieved an R-squared value of 0.58 and a correlation value of 0.76, indicating a strong linear relationship and predictive accuracy.
- **Investor Behavior Insights:** Noted a significant interest among social media investors in firms with larger trading volumes, higher volatility, and greater market capitalization.

## Code and Data

The repository includes:

- OLS implementation code
- Prediction database obtained using the Emtract model

## Conclusion

This project successfully demonstrates the potential of using firm-specific investor emotions, derived from social media, to predict stock price movements. The findings highlight the importance of integrating behavioral finance concepts with traditional financial metrics for enhanced market prediction.
