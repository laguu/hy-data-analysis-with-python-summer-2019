#%%
#!/usr/bin/env python3

import pandas as pd

#%%
def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d
#%%
def split_date_continues():
    #%%
    df=pd.read_csv('src/Helsingin_pyorailijamaarat.csv',sep=';')
    df=df.dropna(axis=0,how='all')
    df=df.dropna(axis=1,how='all')
    df=split_date(df)
    df
    
    
    
    return None
#%%
def main():
#%%
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())

#%%
if __name__ == "__main__":
    main()
