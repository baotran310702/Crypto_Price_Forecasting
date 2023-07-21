# Crypto_Price_Forecasting
<h2>Description</h2>
The ARIMA-ADAUSDT-Forecaster repository is an exceptional resource that employs advanced forecasting techniques to predict the price movements of ADAUSDT, a cryptocurrency traded on the Binance exchange. Leveraging the power of ARIMA (Autoregressive Integrated Moving Average) models and the combined potential of ARIMA and Random Walk models, this repository offers a cutting-edge solution for accurate and reliable price predictions.

With the surge in popularity of cryptocurrencies and the increasing demand for efficient market analysis tools, the ARIMA-ADAUSDT-Forecaster repository stands out as a remarkable tool for traders, investors, and researchers in the cryptocurrency domain. This repository harnesses the principles of time series analysis, encompassing historical price data, to generate future price forecasts for ADAUSDT, facilitating informed decision-making in the volatile crypto market.

<h2>ARIMA Models</h2>

The repository integrates ARIMA models, which are widely recognized for their effectiveness in capturing complex temporal patterns and trends. By considering the autoregressive, moving average, and differencing components, ARIMA models deliver robust forecasts for ADAUSDT price fluctuations.

- Visualize data with line chart. <br/>

<img src="https://res.cloudinary.com/dxhsadna0/image/upload/v1689941431/pictureOfBugs/visualize_data_qhrrzb.png" /><br/>

- Using PACF & ACF and differencing method to find best parameters for models. <br/>

<img src="https://res.cloudinary.com/dxhsadna0/image/upload/v1689941307/pictureOfBugs/PACF_ACF_-_diff_method_u7z9ik.png" /><br/>

- Train - validate and test data with ratio 7 - 2 - 1 and predict next 30 days.
<img src="https://res.cloudinary.com/dxhsadna0/image/upload/v1689941595/pictureOfBugs/arima_s9gd8a.png" />

<h2>Random Walk Model</h2>

A random walk model is a stochastic process where each step is determined by chance. It's unpredictable and can be used to simulate various phenomena, like asset prices in finance or particle diffusion in physics. The model is straightforward but has essential theoretical implications and serves as a foundation for more complex stochastic models. Next step will be calculated by previous step plus random noise.

- Visualize random noise values.

<img src="https://res.cloudinary.com/dxhsadna0/image/upload/v1689941827/pictureOfBugs/ramdom_noise_lanhkk.png" />

<h3>Combinate ARIMA and Random Walk</h3>

<img src="https://res.cloudinary.com/dxhsadna0/image/upload/v1689941596/pictureOfBugs/ARIMAR_x8aank.png"/>

<h2>Dataset from Binance</h2>
I used data from Binance by API provided. I fetched them and export to a CSV file.
