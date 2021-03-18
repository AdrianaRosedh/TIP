import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import requests
import json
from dash.dependencies import Input, Output

#GET KPI1
KPI1 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi1/incvol/"
r = requests.get(KPI1)
KPI1JSON = json.loads(r.text)

def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname='/kpi1/')
    
    dash_app.layout= html.Div(children=[
    html.H1(children='IBERIA DASHBOARD'),
    #KPI1
    dcc.Dropdown(
        id="month",
        options=[{"label": 'January 2018', "value":'201801'},
                 {"label": 'February 2018', "value":'201802'},
                 {"label": 'March 2018', "value":'201803'},
                 ],
        value="201801"
    ),
    dcc.Graph(
        id='kpi1',
        figure={
            'data': [],
            'layout': {
                'title': ''
            }
        }
    )
])
    #KPI1 DATA - total incidences
    incidences= {}
    for i in KPI1JSON["items"]:
        if i['month'] in incidences:
            incidences[i['month']].append(i['incidences_number'])
        else: 
            incidences[i['month']]= [i["incidences_number"]]
    
    @dash_app.callback(
    Output(component_id="kpi1",component_property="figure"),
    [Input(component_id="month", component_property="value")]
    )
    def update_KPI1(value):
        return {
            "data": [
            {'x': ["Alta", "Baja", "Media", "Critica"], 'y': incidences[value], 'type': 'bar', 'name': value},
      ],
      "layout": {
        "title": "Incidences per month"
      }
    } 

    return dash_app










if __name__ == '__main__':
    app.run_server(debug=True)
