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

#print(k1_months)
#print(k1_incidences_numbers)
#print(k1_priorities)

k1_df = pd.DataFrame({
    "Months": k1_months,
    "Number of incidents": k1_incidences_numbers,
    "Priority": k1_priorities
})

def create_kpi1(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi1", url_base_pathname='/kpi1/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi1-graph',
            figure= px.bar(k1_df, x="Months", y="Number of incidents", color="Priority", barmode="group")
        ),  
        
    )

    return dash_app

# #COMPLICATED
# def create_dash_application(flask_app):
#     dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname='/kpi1C/')
    
#     dash_app.layout= html.Div(children=[
#     html.H1(children='IBERIA DASHBOARD'),
#     #KPI1
#     dcc.Dropdown(
#         id="month",
#         options=[{"label": 'January 2018', "value":'201801'},
#                  {"label": 'February 2018', "value":'201802'},
#                  {"label": 'March 2018', "value":'201803'},
#                  ],
#         value="201801"
#     ),
#     dcc.Graph(
#         id='kpi1',
#         figure={
#             'data': [],
#             'layout': {
#                 'title': ''
#             }
#         }
#     )
# ])
#     #KPI1 DATA - total incidences
#     incidences= {}
#     for i in KPI1JSON["items"]:
#         if i['month'] in incidences:
#             incidences[i['month']].append(i['incidences_number'])
#         else: 
#             incidences[i['month']]= [i["incidences_number"]]
    
#     @dash_app.callback(
#     Output(component_id="kpi1",component_property="figure"),
#     [Input(component_id="month", component_property="value")]
#     )
#     def update_KPI1(value):
#         return {
#             "data": [
#             {'x': ["Baja", "Media", "Alta" "Critica"], 'y': incidences[value], 'type': 'bar', 'name': value},
#             ],
#       "layout": {
#         "title": "Incidences per month"
#       }
#     }

#     return dash_app

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

#KPI3
kpi3_months = []
kpi3_brbaja=[]
kpi3_brmedia=[]
kpi3_bralta=[]
kpi3_brcritica=[]
kpi3_mtbaja=[]
kpi3_mtmedia=[]
kpi3_mtalta=[]
kpi3_mtcritica=[]

for dict in KPI3JSON:
    kpi3_months.append(dict["month"])
    kpi3_brbaja.append(dict["brbaja"])
    kpi3_brmedia.append(dict["brmedia"])
    kpi3_bralta.append(dict["bralta"])
    kpi3_brcritica.append(dict["brcritica"])
    kpi3_mtbaja.append(dict["mtbaja"])
    kpi3_mtmedia.append(dict["mtmedia"])
    kpi3_mtalta.append(dict["mtalta"])
    kpi3_mtcritica.append(dict["mtcritica"])

kpi3_df = pd.DataFrame({
    "Months": kpi3_months,
    "brbaja": kpi3_brbaja,
    "brmedia": kpi3_brmedia,
    "bralta": kpi3_bralta,
    "brcritica":kpi3_brcritica,
    "mtbaja": kpi3_mtbaja,
    "mtmedia": kpi3_mtmedia,
    "mtalta": kpi3_mtalta,
    "mtcritica":kpi3_mtcritica,
})

def create_kpi3(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi3", url_base_pathname='/kpi3/')
    
    dash_app.layout = html.Div(children=[
        # BAJA
        html.Div([
            html.H1(children='Hello Dash'),

            html.Div(children='''
                Dash: A web application framework for Python.
            '''),

            dcc.Graph(
            id='kpi3-graph1',
            figure= px.bar(kpi3_df, x="Months", y=["brbaja", "mtbaja"], barmode="group")
            ),  
        ]),
        # MEDIA
        html.Div([
            html.H1(children='Hello Dash'),

            html.Div(children='''
                Dash: A web application framework for Python.
            '''),

            dcc.Graph(
            id='kpi3-graph2',
            figure= px.bar(kpi3_df, x="Months", y=["brmedia", "mtmedia"], barmode="group")
            ), 
        
        ]),
        # ALTA
        html.Div([
            html.H1(children='Hello Dash'),

            html.Div(children='''
                Dash: A web application framework for Python.
            '''),

            dcc.Graph(
            id='kpi3-graph3',
            figure= px.bar(kpi3_df, x="Months", y=["bralta", "mtalta"], barmode="group")
            ), 
        
        ]),
        # CRITICA
        html.Div([
            html.H1(children='Hello Dash'),

            html.Div(children='''
                Dash: A web application framework for Python.
            '''),

            dcc.Graph(
            id='kpi3-graph4',
            figure= px.bar(kpi3_df, x="Months", y=["brcritica", "mtcritica"], barmode="group")
            ), 
        
        ]),
        
    ])
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

#GET KPI4
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
