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
KPI1JSON = r.json()["items"]

#SIMPLE VERSION 

k1_months = []
k1_incidences_numbers = []
k1_priorities = []

for dict in KPI1JSON:
    k1_months.append(dict["month"])
    k1_incidences_numbers.append(dict["incidences_number"])
    k1_priorities.append(dict["priority"])

k1_df = pd.DataFrame({
    "Months": k1_months,
    "Number of incidents": k1_incidences_numbers,
    "Priority": k1_priorities
})

def create_kpi1(flask_app):
    dash_app = dash.Dash(server=flask_app, name="incidences", url_base_pathname='/kpi1/')       
    dash_app.layout = html.Div(children=[
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
            figure= px.bar(k1_df, x="Months", y="Number of incidents", color="Priority", barmode="group")
        )
    ])

    @dash_app.callback(
        Output(component_id="kpi1",component_property="figure"),
        [Input(component_id="month", component_property="value")]
    )
    def update_KPI1(value):
        return {
            "data": [
            {'x': ["Baja", "Media", "Alta", "Critica"], 'y': k1_month[value], 'type': 'bar', 'name': value},
            ],
            "layout": {
                "title": "Incidences per month"
            }
        }
        return dash_app


#GET KPI2
KPI2 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi1/incvol/"
r2 = requests.get(KPI2)
KPI2JSON = r2.json()["items"]

#KPI2
kpi2_months = []
kpi2_incidences_numbers = []

for dict in KPI2JSON:
    kpi2_months.append(dict["month"])
    kpi2_incidences_numbers.append(dict["incidences_number"])


kpi2_df = pd.DataFrame({
    "Months": kpi2_months,
    "Number of incidents": kpi2_incidences_numbers,
})

def create_kpi2(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi2", url_base_pathname='/kpi2/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi2-graph',
            figure= px.bar(kpi2_df, x="Months", y="Number of incidents", barmode="group")
        ),  
        
    )
    return dash_app

#GET KPI3
KPI3 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi3/sla/"
r3 = requests.get(KPI3)
KPI3JSON = r3.json()["items"]

#GET KPI3 Fancy Version

sla= {}
for i in KPI3JSON:
    if i['month'] in sla:
        sla[i['month']].append(i['brbaja'],i['mtbaja'],i['brmedia'],i['mtmedia'],i['bralta'],i['mtalta'],i['brcritica'],i['mtcritica'])
    else: 
        sla[i['month']]= [i["brbaja"],i['mtbaja'],i['brmedia'],i['mtmedia'],i['bralta'],i['mtalta'],i['brcritica'],i['mtcritica']]

def create_kpi3(flask_app):
    dash_app = dash.Dash(server=flask_app, name="SLA", url_base_pathname='/kpi3/')    
    
    dash_app.layout = html.Div(children=[
        #KPI3
        dcc.Dropdown(
            id="month",
            options=[{"label": 'January 2018', "value":'201801'},
                    {"label": 'February 2018', "value":'201802'},
                    {"label": 'March 2018', "value":'201803'}
                    ],
            value="201801"
        ),
        dcc.Graph(
            id='kpi3',
            figure={
                'data':[],           
            }
        )  
    ])
    @dash_app.callback(
    Output(component_id="kpi3",component_property="figure"),
    [Input(component_id="month", component_property="value")]
    )
    def update_KPI3(value):
        return {
            "data": [
            {'x': ['BR BAJA','MT BAJA','BR MEDIA','MT MEDIA','BR ALTA','MT ALTA','BT CRITICA','MT CRITICA'], 'y': sla[value], 'type': 'bar', 'name': value},
            
            ]
        }

        return dash_app

#GET KPI4
KPI4 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi4/BL/"
r4 = requests.get(KPI4)
KPI4JSON = r4.json()["items"]

#SIMPLE VERSION 

k4_months = []
k4_incidences_numbers = []

for dict in KPI4JSON:
    k4_months.append(dict["month"])
    k4_incidences_numbers.append(dict["incidences_number"])

#print(k4_months)
#print(k4_incidences_numbers)

k4_df = pd.DataFrame({
    "Months": k4_months,
    "Number of incidents": k4_incidences_numbers,
})

def create_kpi4(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi4", url_base_pathname='/kpi4/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi4-graph',
            figure= px.bar(k4_df, x="Months", y="Number of incidents", barmode="group")
        ),       
    )
    return dash_app

#GET KPI5
KPI5 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi5/av/"
r5 = requests.get(KPI5)
KPI5JSON = r5.json()["items"]

#SIMPLE VERSION 

k5_months = []
k5_unavailability_time = []
k5_availability_percentage = []
k5_service = []

for dict in KPI5JSON:
    k5_months.append(dict["month"])
    k5_unavailability_time.append(dict["unavailability_time"])
    k5_availability_percentage.append(dict["availability_percentage"])
    k5_service.append(dict["service"])

k5_df = pd.DataFrame({
    "Months": k5_months,
    "Number of Unavailability": k5_unavailability_time,
    "Percentage of Availability": k5_availability_percentage,
    "Service": k5_service,
})

def create_kpi5(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi5", url_base_pathname='/kpi5/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi5-graph',
            figure= px.bar(k5_df, x="Months", y="Number of Unavailability", color="Service", hover_name="Percentage of Availability", barmode="group")
        ),  
        
    )
    return dash_app

#GET KPI6
KPI6 = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi6/monav/"
r6 = requests.get(KPI6)
KPI6JSON = r6.json()["items"]

k6_month = []
k6_monthly_av = []
 
for dict in KPI6JSON:
    k6_month.append(dict["month"])
    k6_monthly_av.append(dict["monthly_av"])
    
k6_df = pd.DataFrame({
    "Months": k6_month,
    "Average": k6_monthly_av
    })
        
def create_kpi6(flask_app):
      dash_app = dash.Dash(server=flask_app, name="kpi6", url_base_pathname='/kpi6/')
      
      dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi6-graph',
            figure= px.bar(k6_df, x="Months", y="Average", barmode="group")
        ),  
        
    )
      return dash_app
