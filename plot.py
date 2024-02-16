import plotly.graph_objects as go
from plotly.subplots import make_subplots


def mv_plot(df):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df['Date'],
                open=df['Open price'],
                high=df['High price'],
                low=df['Low price'],
                close=df['Close price'],
                name='Price'))
    
    
    fig.add_trace(go.Scatter(x=df['Date'],y=df['Mov Avg'],mode='lines',name='Moving Average'))
    
    fig.update_layout(
        plot_bgcolor='white',
        xaxis_title="Date",
        yaxis_title="Price"
    )

    return(fig)

def rsi_plot(df):
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.0001)

    fig.add_trace(go.Candlestick(x=df['Date'],
                open=df['Open price'],
                high=df['High price'],
                low=df['Low price'],
                close=df['Close price'],
                name='Price'), row=1, col=1)


    fig.add_trace(go.Scatter(x=df['Date'], y=df['RSI'], mode='lines', name='Relative Strength Index'),row=3,col=1)

    fig.add_shape(
        dict(type='line', y0=30, y1=30, x0=min(df['Date']), x1=max(df['Date']), line=dict(dash='dot', color='red')),
        row=3, col=1
    )
    fig.add_shape(
        dict(type='line', y0=70, y1=70, x0=min(df['Date']), x1=max(df['Date']), line=dict(dash='dot', color='green')),
        row=3, col=1
    )

    fig.update_layout(
        autosize=False,
        width=1000,
        height=700,
        xaxis_rangeslider_visible=True,
        plot_bgcolor='white',
        yaxis_title="Price",
        xaxis_title = "Date",
        legend=dict(
            x=1.2, 
            y=1.0
        )
        
    )

    return fig
