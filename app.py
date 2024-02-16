import streamlit as st
import pandas as pd
from data_prep import tok_val,mv,rsi
from datetime import datetime as dt, date, timedelta
from dateutil.relativedelta import relativedelta
from plot import mv_plot,rsi_plot

st.sidebar.image('pt_logo.jpg')
st.sidebar.title(':panda_face:💬 Off-Chain Metrics App')
# st.set_page_config(page_title='Off-Chain Metrics Dashboard', layout='wide', page_icon=":panda_face:")
info_slot = st.empty()
info_slot.text("Please enter the proper values to get the desired chart")
Metric = st.sidebar.selectbox('Select Metric',options=(None,'SMA','RSI'))

if Metric == 'SMA':
    coin = st.sidebar.selectbox('Select Coin',options= tok_val())
    granularity = st.sidebar.selectbox("Select the granularity",options=('3M','6M','1Y','Custom'))
    MA_VAL = st.sidebar.selectbox('Select required moving avergae value',options=[5, 8, 13, 21, 34, 55, 89, 144, 233])
    
    if granularity == 'Custom':
        date_s = str(st.sidebar.date_input("Select start date"))
        date_e = str(st.sidebar.date_input("Select end date"))

    else:
        if granularity == '3M':
            granularity = 3
        if granularity == '6M':
            granularity = 6
        if granularity == '1Y':
            granularity = 12

        date_s = str(date.today() - relativedelta(months=granularity) - relativedelta(days=MA_VAL))
        date_e = str(date.today())

    val= mv(coin,date_s,date_e,MA_VAL)
    res = mv_plot(val)
    # st.text(val)
    button =  st.sidebar.button('Click Here to Get the Plot for Off-Chain Metrics')
    if button:
        info_slot.empty()
        info_slot.title("Moving Average")
        st.text((coin))
        st.plotly_chart(res,use_container_width=True)


if Metric == 'RSI':
    coin = st.sidebar.selectbox('Select Coin',options= tok_val())
    granularity = st.sidebar.selectbox("Select the granularity",options=('3M','6M','1Y','Custom'))

    if granularity == 'Custom':
        date_s = str(st.sidebar.date_input("Select start date"))
        date_e = str(st.sidebar.date_input("Select end date"))

    else:
        if granularity == '3M':
            granularity = 3
        if granularity == '6M':
            granularity = 6
        if granularity == '1Y':
            granularity = 12

        date_s = str(date.today() - relativedelta(months=granularity)- relativedelta(days=14))
        date_e = str(date.today())
    
    val= rsi(coin,date_s,date_e)

    try:
        res = rsi_plot(val)
        button =  st.sidebar.button('Click Here to Get the Plot for Off-Chain Metrics')
        if button:
            info_slot.empty()
            info_slot.title("Relative Strength Index")
            st.text((coin))
            st.plotly_chart(res,use_container_width=True)
    except:
        st.text("Atleast 14 days interval is needed")

    


