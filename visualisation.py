import plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import requests

link = 'https://78703be3.ngrok.io/analytics'


external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app= dash.Dash(__name__, external_stylesheets=external_stylesheets)




colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


markdown_text_01='''
## Cyber Bullying
Cyberbullying or cyberharassment is a form of bullying or harassment using electronic means. Cyberbullying and cyberharassment are also known as online bullying. It has become increasingly common, especially among teenagers. Cyberbullying is when someone ,bully or harass others on the internet, particularly on social media sites. Harmful bullying behavior can include posting rumors, threats, sexual remarks, a victim's personal information, or pejorative labels (i.e. hate speech).Bullying or harassment can be identified by repeated behavior and an intent to harm.Victims may experience lower self-esteem, increased suicidal ideation, and a variety of negative emotional responses, including being scared, frustrated, angry, and depressed.
'''

markdown_text_02='''
## Cyber bullying laws in India
There is no specific legislation that provides for the specific cyberbullying laws in India however provisions such as Section 67 of the Information Technology Act deals with cyberbullying in a way. Section 67 of the act prescribes punishment for publishing or transmitting obscene material in electronic form for a term which may extend to five years and also with fine which may extend to ten lakh rupees.
Other than Section 67 of the IT Act following are the provisions of the cyberbullying laws in India:

Section 507  IPC -  The section states that if anyone receives criminal intimidation by way of an anonymous communication then the person giving threats shall be punished with imprisonment for up to two years. By virtue of word anonymous the offense of anti-bullying and cyberbullying is included in this section.

Section 66 E of IT Act - The section prescribes punishment for violation of privacy. The section states that any person who intentionally violates the privacy by transmitting, capturing or publishing private pictures of others shall be punished with up to three years imprisonment or fine up to three lakhs.
'''



app.layout=html.Div(
					[

# 					dcc.Markdown(children=markdown_text_01,style={
# 						'textAlign':'center',
# 						'color':colors['background']
# 						}),

# 					dcc.Markdown(children=markdown_text_02,style={
# 						'textAlign':'center',
# 						'color':colors['background']
# 						}),
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