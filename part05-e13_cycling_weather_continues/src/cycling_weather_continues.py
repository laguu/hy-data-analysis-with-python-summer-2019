#!/usr/bin/env python3
import pandas as pd
from sklearn import linear_model

#%%
wd = {
    'ma' : 'Mon',
    'ti' : 'Tue',
    'ke' : 'Wed',
    'to' : 'Thu',
    'pe' : 'Fri',
    'la' : 'Sat',
    'su' : 'Sun'
}
m = {
    'tammi': 1,
    'helmi': 2,
    'maalis': 3,
    'huhti': 4,
    'touko': 5,
    'kesä': 6,
    'heinä': 7,
    'elo': 8,
    'syys': 9,
    'loka': 10,
    'marras': 11,
    'joulu': 12
}
def days(s):
    return wd[s]

def months(s):
    return m[s]
    
def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def split_date_continues():
    df = pd.read_csv('./src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(axis=0, how='all')
    df = df.dropna(axis=1, how='all')
    df = pd.concat((df.drop(columns=['Päivämäärä']), split_date(df)), axis=1)
    
    return df

def cycling_weather():

    df = split_date_continues()
    df = df.groupby(['Year','Month','Day']).sum().reset_index()
    df2 = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    df2.iloc[:5,0:5]
    # parsee päivämäärät ja yhdistä
    res = pd.merge(df,df2,left_on=['Year','Month','Day'], right_on=['Year','m','d'])
    res = res.drop(columns=['m', 'd', 'Time', 'Time zone'])
    res = res.fillna(method='ffill')    


    return res    

#%%

def cycling_weather_continues(station):

    df = cycling_weather()
    df = df.groupby(['Year','Month','Day']).sum().reset_index()
    
    df = df[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)',station]]
    #df = df.fillna(method='ffill')
    #df = df.dropna()

    model = linear_model.LinearRegression(fit_intercept=True)
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    model.fit(X, y)
    

    return (tuple(model.coef_), model.score(X,y))




#%%    
def main():
    #%%
    st='Merikannontie'
    coef, score = cycling_weather_continues(st)
    
    #%%
    
    print(f"Measuring station: {st}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")
#%%
if __name__ == "__main__":
    main()
