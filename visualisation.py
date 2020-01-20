import plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import requests

link = 'ADD HERE API LINK OF DATABASE THAT RETURNS JSON VALUES'


# Here I have taken sample from my project that returned values like city names, site name, person name, age , gender etc.
#So here, visualizations are for the data as mentioned above

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app= dash.Dash(__name__, external_stylesheets=external_stylesheets)




colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout=html.Div(
					[
						
					html.H1(children="!!!Visualisations!!!",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),
					html.Div(
						dcc.Graph( 
						       id='place_vs_their_count'
						      )
						),
					html.Div(
						dcc.Graph( 
						       id='site_vs_count'
						      )
						),
                    html.Div(
                        dcc.Graph(
                            id='Gender vs Count'
                            )
                        ),
					dcc.Interval(
            		id='interval-component',
            		interval=1*10000, 
            		n_intervals=0
       				 )
					]
					)

@app.callback(Output('place_vs_their_count', 'figure'),
              [Input('interval-component', 'n_intervals')])

def update_event(n):
    data = requests.get(link)
    ans = data.json()
    
    nik = ans['details']
    
    df = pd.DataFrame(nik)
    
    data={
	'x_data':[],
	'y_data':[]
	}
    
    seq=[var for var in df['location'].unique()]
    
    def match(temp):
        cnt=0
        for var in df['location']:
            if var==temp:
                cnt=cnt+1
        return cnt
    
    y=list(map(match,seq))
    
    for k in seq:
        data['x_data'].append(k)
        
    for j in y:
        data['y_data'].append(j)
        
        
    fig=make_subplots(rows=1,cols=1)
    
    fig.append_trace({
		'x':data['x_data'],
		'y':data['y_data'],
		'type':'scatter',
        'mode':'lines+markers'
		},1,1)
    
    return fig




@app.callback(Output('site_vs_count', 'figure'),
              [Input('interval-component', 'n_intervals')])

def update_event(n):
    data2 = requests.get(link)
    ans2 = data2.json()
    
    nik2 = ans2['details']
    
    df2 = pd.DataFrame(nik2)
    
    data={
	'x_data':[],
	'y_data':[]
	}
    
    
    seq=[var for var in df2['site'].unique()]
    
    
    def match(temp):
        cnt=0
        for var in df2['site']:
            if var==temp:
                cnt=cnt+1
        return cnt
    
    y=list(map(match,seq))
    
    for k in seq:
        data['x_data'].append(k)
        
    for j in y:
        data['y_data'].append(j)
        
        
    fig=make_subplots(rows=1,cols=1)
    
    fig.append_trace({
		'x':data['x_data'],
		'y':data['y_data'],
		'type':'bar'
		},1,1)
    
    return fig



@app.callback(Output('Gender vs Count', 'figure'),
              [Input('interval-component', 'n_intervals')])

def update_event(n):
    data3 = requests.get(link)
    ans3 = data3.json()
    
    nik3 = ans3['details']
    
    df3 = pd.DataFrame(nik3)
    
    data={
	'x_data':[],
	'y_data':[]
	}
    
    seq=[var for var in df3['gender'].unique()]
    
    def match(temp):
        cnt=0
        for var in df3['gender']:
            if var==temp:
                cnt=cnt+1
        return cnt
    
    
    y=list(map(match,seq))
    
    for k in seq:
        data['x_data'].append(k)
        
    for j in y:
        data['y_data'].append(j)
        
    fig=make_subplots(rows=1,cols=1)
    
    fig.append_trace({
		'x':data['x_data'],
		'y':data['y_data'],
		'type':'bar'
		},1,1)
    
    return fig



if __name__ == '__main__':
    app.run_server(debug=False)
