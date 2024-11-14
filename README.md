p1:

import numpy as np
from scipy import stats
print("Hitesh Bhanushali KSMSCIT005")
# Sample Dataset
Scores = [85, 90, 78, 92, 88, 76, 95, 89, 77, 84]

# Calculate Mean
Mean = np.mean(Scores)
print("Mean:", Mean)

# Calculate Median
Median = np.median(Scores)
print("Median:", Median)

# Calculate Mode
Mode = stats.mode(Scores)
print("Mode:", Mode)

# Calculate Standard Deviation
Standard_Deviation = np.std(Scores)
print("Standard Deviation:", Standard_Deviation)

# Calculate Mean Absolute Deviation
Mean_Absolute_Deviation = np.mean(np.abs(np.array(Scores) - Mean))
print("Mean Absolute Deviation:", Mean_Absolute_Deviation)



p1.2:

import numpy as np
from scipy import stats
population_mean = 100
population_std_dev = 15
alpha =0.05
np.random.seed(0)
sample_size=30
sample=np.random.normal(population_mean,population_std_dev,sample_size)
sample_mean = np.mean(sample)
z_score= (sample_mean-population_mean/(population_std_dev/np.sqrt(0.005)))
p_value= 2*(1-stats.norm.cdf(abs(z_score)))
print("Hitesh Bhanushali KSMSCIT005")
print(sample_mean,z_score,p_value)
if(p_value<alpha):
  print("reject null hypothesis")
else:
          print("Accept null hypothesis")







p2:


from scipy import stats
print("Hitesh Bhanushali KSMSCIT005")
# Given Data
Population_Mean = 100
Population_Standard_Deviation = 15
Sample_Mean = 140
Sample_Size = 30

# Calculate Z-Score
Z_Score = (Sample_Mean - Population_Mean) / (Population_Standard_Deviation / np.sqrt(Sample_Size))
print("Z-Score:", Z_Score)

# Calculate P-Value
P_Value = 2 * (1 - stats.norm.cdf(abs(Z_Score)))
print("P-Value (Two-Tailed Test):", P_Value)

Significance_Value = 0.05
if P_Value < Significance_Value:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")



p2.2:

import random

def flip_coin(n):
    head = 0
    for i in range(n):
        if random.random() < 0.5:
            head += 1
    return head

def calculate_error(n_flip):
    total_flip = 10000
    type_1 = 0
    type_2 = 0
    
    for j in range(total_flip):
        heads = flip_coin(n_flip)
        if abs(heads - n_flip / 2) > 1.96 * (n_flip ** 0.5):
            if flip_coin(n_flip) == n_flip / 2:
                type_1 += 1
            if flip_coin(n_flip) != n_flip / 2:
                type_2 += 1
    
    p_type_1 = type_1 / total_flip
    p_type_2 = type_2 / total_flip
    
    print("Prop of type1:", p_type_1)
    print("Prop of type2:", p_type_2)
print("Hitesh Bhanushali KSMSCIT005")
calculate_error(28)




p3.1:


from scipy import stats
import numpy as np
#sample data
mean = 1850
std = 100
data = [1850 for _ in range(50)]

#hypothesis test parameter
null_mean = 1800
alpha = 0.01

#calculate sample mean
sample_mean = sum(data)/len(data)

#calculate z_score using std
z_score = (sample_mean - null_mean)/(100/np.sqrt(50))
print("Hitesh Bhanushali KSMSCIT005")

#import for p value calculation (1 Tail)
#calculate p_value
p_value = 1-stats.norm.cdf(z_score)
p_value
if p_value < alpha:
  print("reject null hypothesis")
else:
  print("accept null hypothesis")




p3.2:

print("Hitesh Bhanushali KSMSCIT005")
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd

#Given data
overall_mean = 74.5
overall_std = 8.0
sample_size = 200
sample_mean = 75.90
alpha = 0.05

#HYPOTHESIS (NULL & ALTERNATIVE)
null_hypothesis = overall_mean >= sample_mean #assuming higher mean (1 tail)
alternative_hypothesis = not null_hypothesis #rejecting (2 tail)

#cal of z score
# 1 tail
z_score = (sample_mean - overall_mean)/(overall_std/np.sqrt(sample_size))


from scipy.stats import norm
p_value = 1-norm.cdf(z_score)
print(p_value)

#2 Tail (CONSIDERING BOTH THE VALUE)
p_value_2 = 2*(1-norm.cdf(abs(z_score)))
print(p_value_2)

#NORMAL DISTRIBUTION
x = np.linspace(overall_mean - 3*overall_std, overall_mean + 3*overall_std, 100)
plt.plot(x, norm.pdf(x, overall_mean, overall_std) , label = 'Normal Distribution')
plt.axvline(x=overall_mean, color='r', linestyle='--', label='Overall Mean')
plt.axvline(x=sample_mean, color='g', linestyle='--', label='Sample Mean')
plt.xlabel('Exam Grades')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')
plt.legend()
plt.show()






p4:


import pandas as pd
from scipy.stats import f_oneway
print("Hitesh Bhanushali KSMSCIT005")
data = {"subject1":[85,95,98,90,84,88,87],"Subject2":[88,93,94,93,80,89,86],"Subject 3":[83,90,93,94,88,92,84]}
df=pd.DataFrame(data)
df.head(7)


#performing ANOVA Testing
f,p=f_oneway(df["subject1"],df["Subject2"],df["Subject 3"])
print("F:",f)
print("p-value:",p)

if p<0.05:
  print("Reject null hypothesis")
else:
  print("Accept null hypothesis")




p4.2:


# ANOVA TWO WAY TESTING
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Corrected data
data = {
    "blend": ["x", "x", "x", "x", "y", "y", "y", "y", "z", "z", "z", "z"],
    "crops": ["wheat", "corn", "soya", "rice", "wheat", "corn", "soya", "rice", "wheat", "corn", "soya", "rice"],
    "values": [123, 138, 110, 151, 145, 165, 140, 167, 156, 176, 185, 175]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Hitesh Bhanushali KSMSCIT005")

# Show the first few rows of the DataFrame
print(df.head())

# Model creation for two-way ANOVA (blend and crops as factors)
model = ols('values ~ blend + crops', data=df).fit()

# Print the model summary
print(model.summary())







p5:


#pract 5
print ("Hitesh Bhanushali KSMSCIT005")
import numpy as np
from scipy.stats import linregress
x=np.array([44,78,43,50,64,56,70,55,45,44])
y=np.array([72,74,52,61,62,56,80,65,59,61])

#regressio y on x
slope_yx,intercept_yx,r_value_yx,p_value_yx,std_err_yx=linregress(x,y)
#regressio x on y
slope_xy,intercept_xy,r_value_xy,p_value_xy,std_err_xy=linregress(y,x)

#estimate y on x
estimate_y_on_x=slope_yx*61+intercept_yx
#estimate x on y
estimate_x_on_y=slope_xy*61+intercept_xy

print('estimate_y_on_x',estimate_y_on_x)
print('estimate_x_on_y',estimate_x_on_y)

print('slope_yx',slope_yx)
print('intercept_yx',intercept_yx)
print('r_value_yx',r_value_yx)
print('p_value_yx',p_value_yx)
print('std_err_yx',std_err_yx)





p6:


import scipy.stats as stats
import numpy as np
import pandas as pd
print("Hitesh Bhanushali KSMSCIT005")

height_father = [61,63,53,70,69,80,71]
height_son = [60,62,84,44,69,55,72]
c,pvalue = stats.pearsonr(height_father,height_son)
#perform paired ttest
t,pvalue2 = stats.ttest_rel(height_father,height_son)
print("Pearson Correlation Coefficient:",c)
print("P-Value:",pvalue)
print("T-Statistic:",t)
print("P-Value:",pvalue2)




p7:

import numpy as np
import pandas as pd
print("Hitesh Bhanushali KSMSCIT005")

# Define the treatments, subjects, and periods
treatments = ['Fertilizer A', 'Fertilizer B', 'Fertilizer C']
plants = ['Plant 1', 'Plant 2', 'Plant 3']
periods = ['Morning', 'Afternoon', 'Evening']

# Create a 3x3 Latin Square matrix
latin_square = np.array([
    [treatments[0], treatments[1], treatments[2]],  # Morning
    [treatments[1], treatments[2], treatments[0]],  # Afternoon
    [treatments[2], treatments[0], treatments[1]],  # Evening
])

# Create a DataFrame for the Latin Square Design
experiment_design = pd.DataFrame(latin_square, columns=plants, index=periods)

# Display the experiment design
print("Latin Square Design:")
print(experiment_design)

# Data collection: heights of plants after one month (in cm)
data = {
    'Plant 1': [33, 27, 29],  # Growth corresponding to the design
    'Plant 2': [32, 30, 31],
    'Plant 3': [31, 29, 33]
}

# Create a DataFrame for the collected data
growth_data = pd.DataFrame(data, index=periods)
print("\nCollected Plant Growth Data (cm):")
print(growth_data)

import statsmodels.api as sm
from statsmodels.formula.api import ols

# Reshape the data for ANOVA
growth_data_melted = growth_data.reset_index().melt(id_vars='index', var_name='Plant', value_name='Growth')
growth_data_melted.columns = ['Period', 'Plant', 'Growth']

# Fit the ANOVA model
model = ols('Growth ~ C(Plant) + C(Period)', data=growth_data_melted).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Display the ANOVA results
print("\nANOVA Results:")
print(anova_table)





p8.1:

#prc 8a
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Generate Data with clear upward trend
np.random.seed(0)
time = np.arange(100)
trend = 0.5 * time
noise = np.random.normal(0,5,size=100)

data = trend + noise

#Create a dataframe
df_trend = pd.DataFrame({'Time':time,'Data':data})

#Plotting
plt.figure(figsize=(10,6))
plt.plot(df_trend,color='blue',label='Data with Trend')
plt.plot(df_trend['Time'],trend,label='Linear',linestyle='dashed',color='red')
plt.title('Hitesh Bhanushali KSMSCIT005 \n Trend Analysis for Upward Trend')
plt.xlabel('Time')
plt.ylabel('Data')
plt.legend()
plt.show()




p8.2:


#prc 8 b
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Generate random data
np.random.seed(0)
time = np.arange(0,100)
seasonality = 10 * np.sin(2 * np.pi * time/12)
noise = np.random.normal(0,2, size = 100)

data = 50 + seasonality + noise

#Create a dataframe
df_seasonality = pd.DataFrame({'Time':time,'Data':data})

#Plotting
plt.figure(figsize=(10,6))
plt.plot(df_seasonality, label='Data with Seasonality')
plt.title('Hitesh Bhanushali KSMSCIT005 \n Seasonal Variation')
plt.xlabel('Time')
plt.ylabel('Data')
plt.legend()
plt.show()





p8.3:

#prc 8 c
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Generate random data
np.random.seed(0)
time = np.arange(0,100)
cycle = 20 * np.sin(2 * np.pi * time/50)
noise = np.random.normal(0,2, size = 100)

data = 50 + seasonality + noise

#Create a dataframe
df_cycle = pd.DataFrame({'Time':time,'Data':data})

#Plotting
plt.figure(figsize=(10,6))
plt.plot(df_cycle, label='Data with Cycle')
plt.title(' Hitesh Bhanushali KSMSCIT005 \n Cycle Variation')
plt.xlabel('Time')
plt.ylabel('Data')
plt.legend()
plt.show()



p8.4:

#prc 8 d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
time = np.arange(0,100)
noise = np.random.normal(0,10,size = 100)

df_irregular = pd.DataFrame({'Time':time,'Data':noise})

#Plotting
plt.figure(figsize=(10,6))
plt.plot(df_irregular,label='Irregular Fluctuation')
plt.title('Hitesh Bhanushali KSMSCIT005 \n Irregular Fluctuation')
plt.xlabel('Time')
plt.ylabel('Data')
plt.legend()


p8.5:

#prc 8 e
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

data = pd.read_csv('/content/airline-passengers.csv',index_col='Month',parse_dates=True)

#Decompose the time series into trend, seasonal and resudial
decompose = seasonal_decompose(data['Passengers'],model='multiplicative')

# Plot decomposition
fig = decompose.plot()

# Adjust layout to prevent overlap
plt.subplots_adjust(top=0.85)

plt.suptitle('Hitesh Bhanushali KSMSCIT005 \n Decomposition of Airline Passengers')
plt.show()



p9.1:



#stockpriceanlysis prc 9
!pip install yfinance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import yfinance as yf

stock_sysbol = 'SUZLON.NS'
stock_data = yf.download(stock_sysbol,start='2019-01-01',end='2024-09-28')
stock_data.head()
stock_data.tail()
plt.figure(figsize=(10,6))
plt.plot(stock_data['Adj Close'],label='Adj Close Price')
plt.title(f'{stock_sysbol} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

stock_data_monthly = stock_data['Adj Close'].resample('M').mean()
stock_data_monthly.head()
decompose_result = seasonal_decompose(stock_data_monthly,model = 'multiplicative')
decompose_result.plot()
plt.suptitle('decomposition of stock price',fontsize=12)
plt.show()
print("Hitesh Bhanushali KSMSCIT005")

#calculate simple moving average of 50 days and 200 day
stock_data['SMA_50'] = stock_data['Adj Close'].rolling(window=50).mean()
stock_data['SMA_200'] = stock_data['Adj Close'].rolling(window=200).mean()
stock_data.head()
plt.figure(figsize=(10,6))
plt.plot(stock_data['Adj Close'],label='Adj Close Price', color = 'blue')
plt.plot(stock_data['SMA_50'],label='SMA_50',color='green')
plt.plot(stock_data['SMA_200'],label='SMA_200',color='red')

plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
print("Hamza Mitkar KSMSCIT019")
print("kaustubh karande KSMSCIT015")





p9.2:

#prc 9 b
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
print("KFMSCIT024 Ayush Rane")
print("---------------------")

# Step 1: Load the dataset
file_path = '/content/daily-min.csv'  # Ensure this is the correct path to your file
data = pd.read_csv(file_path)

# Step 2: Data Preprocessing
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Display the first few rows of the dataset
print(data.head())

# Step 3: Trend Analysis
# Plot the original data
plt.figure(figsize=(12, 6))
plt.plot(data['Temp'], label='Daily Minimum Temperature', color='blue')
plt.title('KFMSCIT024 Ayush Rane \n Daily Minimum Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()

# Step 4: Seasonal Decomposition
decomposition = seasonal_decompose(data['Temp'], model='additive', period=365)  # Assuming yearly seasonality
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot the decomposition
plt.figure(figsize=(12, 12))
plt.subplot(4, 1, 1)
plt.plot(data['Temp'], label='Original', color='blue')
plt.legend(loc='upper left')

plt.subplot(4, 1, 2)
plt.plot(trend, label='Trend', color='orange')
plt.legend(loc='upper left')

plt.subplot(4, 1, 3)
plt.plot(seasonal, label='Seasonal', color='green')
plt.legend(loc='upper left')

plt.subplot(4, 1, 4)
plt.plot(residual, label='Residual', color='red')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

# Step 5: Forecasting
# Fit ARIMA model (you may need to tune the order parameters)
model = ARIMA(data['Temp'].dropna(), order=(5, 1, 0))  # Adjust parameters as needed
model_fit = model.fit()

# Generate forecast for the next 30 days
forecast = model_fit.forecast(steps=30)

# Prepare forecast dates
forecast_dates = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=30)

# Step 6: Visualization of forecast results
plt.figure(figsize=(12, 6))
plt.plot(data['Temp'], label='Historical Temperature', color='blue')
plt.plot(forecast_dates, forecast, label='Forecasted Temperature', color='orange')
plt.title('KFMSCIT024 Ayush Rane \n Temperature Forecast')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()





p10:

#prc 10
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

# Define dataset
data_dict = {
    'Date': pd.date_range(start='2021-01-01', periods=24, freq='M'),
    'Sales': [
        230, 220, 250, 260, 290, 350, 310, 320, 315, 380, 210, 350,  # Year 1
        245, 235, 270, 280, 310, 320, 330, 335, 325, 290, 280, 370   # Year 2
    ]
}
data = pd.DataFrame(data_dict)
data.set_index('Date', inplace=True)

# Plot sales data
plt.figure(figsize=(12, 6))
plt.plot(data['Sales'], label='Monthly Sales')
plt.title('Hitesh Bhanushali KSMSCIT005 \n Monthly Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()

# Decomposition
decomposition = seasonal_decompose(data['Sales'], model='additive', period=12)
decomposition.plot()
plt.show()

# Train-test split (80-20 split)
train_size = int(len(data) * 0.8)
train, test = data.iloc[:train_size], data.iloc[train_size:]
print('Train size:', len(train), 'Test size:', len(test))

print("Hitesh Bhanushali KSMSCIT005")
print("---------------------")

# Fit SARIMAX model
model = SARIMAX(train['Sales'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12),
                enforce_stationarity=False, enforce_invertibility=False)
model_fit = model.fit(disp=False)
print(model_fit.summary())

# Forecast
forecast = model_fit.get_forecast(steps=len(test))
forecast_series = forecast.predicted_mean
conf_int = forecast.conf_int()

# Plot forecast against actual values
plt.figure(figsize=(12, 6))
plt.plot(test.index, test['Sales'], label='Actual Sales', marker='o')
plt.plot(test.index, forecast_series, label='Forecasted Sales', color='red', marker='o')
plt.fill_between(forecast_series.index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='pink', alpha=0.3)
plt.title('Hitesh Bhanushali KSMSCIT005 \n  Monthly Sales Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()

print("Hitesh Bhanushali KSMSCIT005")
# Evaluate model
mse = mean_squared_error(test['Sales'], forecast_series)
print('Mean Squared Error (MSE):', mse)

# Final Model Fitting for future prediction
final_model = SARIMAX(data['Sales'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12),
                      enforce_stationarity=False, enforce_invertibility=False)
final_model_fit = final_model.fit()

# Future forecast (12 months ahead)
future_forecast = final_model_fit.get_forecast(steps=12)
future_index = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=12, freq='M')
future_forecast_series = pd.Series(future_forecast.predicted_mean, index=future_index)
future_conf_int = future_forecast.conf_int()

# Plot future forecast
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Sales'], label='Historical Sales')
plt.plot(future_forecast_series.index, future_forecast_series, label='Future Forecasted Sales', color='green', marker='o')
plt.fill_between(future_forecast_series.index, future_conf_int.iloc[:, 0], future_conf_int.iloc[:, 1], color='lightgreen', alpha=0.3)
plt.title('Hitesh Bhanushali KSMSCIT005 \n  Future Sales Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()





p11:

#least square method
import scipy.stats as stats
import numpy as np
print("Hitesh Bhanushali KSMSCIT005")

# Sample data (x and y values)
x = np.array([59,65,45,69,60,62,70,55,45,49])
y = np.array([76,70,55,65,55,64,80,69,54,61])

slope_yx, intercept_yx, r_value_yx, p_value_yx, std_err_yx = stats.linregress(y, x)
slope_xy, intercept_xy, r_value_xy, p_value_xy, std_err_xy = stats.linregress(x, y)
estimate_yx = slope_yx * 61 + intercept_yx
print("slope_yx:",slope_yx)
print("intercept_yx;",intercept_yx)
print("slope_xy:",slope_xy)
print("intercept_xy:",intercept_xy)
print("estimate_yx:",estimate_yx)
