import pandas as pd
import numpy as np
from raw_data_prep import call
from datetime import datetime


def tok_val():
    df = pd.read_csv('top30.csv')
    df = df['Symbol']
    return(df)

def mv(coin,date_s,date_e,MA_VAL):
    date_s = datetime.strptime(date_s, "%Y-%m-%d")
    date_e = datetime.strptime(date_e, "%Y-%m-%d")

    date_s = (int(date_s.timestamp()))*1000
    date_e = (int(date_e.timestamp()))*1000

    lis = call(coin,date_s,date_e)
    li = [i[0:5] for i in lis]

    df = pd.DataFrame(li, columns=['Date', 'Open price', 'High price', 'Low price', 'Close price'])
    df['Date'] = df['Date'].apply(lambda x :(datetime.utcfromtimestamp(x / 1000.0)).date())
    df['Mov Avg'] = df['Close price'].rolling(window=MA_VAL).mean()
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    return(df)


def rsi(coin,date_s,date_e):
    date_s = datetime.strptime(date_s, "%Y-%m-%d")
    date_e = datetime.strptime(date_e, "%Y-%m-%d")

    date_s = (int(date_s.timestamp()))*1000
    date_e = (int(date_e.timestamp()))*1000

    lis = call(coin,date_s,date_e)
    li = [i[0:5] for i in lis]

    df = pd.DataFrame(li, columns=['Date', 'Open price', 'High price', 'Low price', 'Close price'])
    df['Date'] = df['Date'].apply(lambda x :(datetime.utcfromtimestamp(x / 1000.0)).date())
    df['Close price'] = df['Close price'].astype(float)
    df['change'] = df['Close price'] - df['Close price'].shift(1)
    df.dropna(subset=['change'],inplace=True)
    df['Gain'] = np.where(df['change']>0,df['change'],0)
    df['Loss'] = np.where(df['change']<0,(df['change']*(-1)),0)
    df['Avg Gain'] = df['Gain'].rolling(window=14).mean()
    df['Avg Loss'] = df['Loss'].rolling(window=14).mean()
    df['RS'] = df['Avg Gain']/df['Avg Loss']
    df['RSI'] = (100 - (100/(1+df['RS'])))
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    return(df)

    
