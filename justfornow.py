#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:53:11 2021

@author: damianmendelsohn
"""
import dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import requests
import json
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

#GET KPI1
KPI1 = "https://pienihkdkeeamjz-db202102121646.adb.us-ashburn-1.oraclecloudapps.com/ords/tip/kpi1/incvol/"
r = requests.get(KPI1)
KPI1JSON = json.loads(r.text)

#GET KPI2
KPI2 = "https://pienihkdkeeamjz-db202102121646.adb.us-ashburn-1.oraclecloudapps.com/ords/tip/kpi2/incsolved/"
r = requests.get(KPI2)
KPI2JSON = json.loads(r.text)

#GET KPI3
KPI3 = "https://pienihkdkeeamjz-db202102121646.adb.us-ashburn-1.oraclecloudapps.com/ords/tip/kpi3/sla/"
r = requests.get(KPI3)
KPI3JSON = json.loads(r.text)

#GET KPI4
KPI4 = "https://pienihkdkeeamjz-db202102121646.adb.us-ashburn-1.oraclecloudapps.com/ords/tip/kpi4/BACKL/"
r = requests.get(KPI4)
KPI4JSON = json.loads(r.text)

#Month Labels
monthslist=["January","February","March","April","May","June","July","August","September","October","November","December"]

#Incidents Solved Values
incidenceskpi2=[]
for i in KPI2JSON["items"]:
    incidenceskpi2.append(i['incident_code'])
incidenceskpi2 
    
app.layout = html.Div(children=[
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
                #{'x': priority, 'y': incidences, 'type': 'bar', 'name': 'bar1'}
            'layout': {
                'title': ''
            }
        }
    ),
     #KPI2
     dcc.Graph(
        id='kpi2',
        figure={
            'data': [{'x': monthslist,'y': incidenceskpi2, 'type': 'bar', 'name': 'bar2'}],
            'layout': {
                'title': "Incidences solved per month"
            }
        }
    ),
     #KPI4
    dcc.Dropdown(
        id="monthss",
        options=[{"label": 'January 2018', "value":'201801'},
                 {"label": 'February 2018', "value":'201802'},
                 {"label": 'March 2018', "value":'201803'},
                 ],
        value="201801"
    ),
     dcc.Graph(
        id='kpi4',
        figure={
            'data': [],
            'layout': {
                'title': ''
            }
        }
    ),
    
])

#KPI1 DATA - total incidences
incidences= {}
for i in KPI1JSON["items"]:
    if i['month'] in incidences:
        incidences[i['month']].append(i['incidences_number'])
    else: 
        incidences[i['month']]= [i["incidences_number"]]
      
#KPI2 DATA - solved per month
solved= {}
for i in KPI2JSON["items"]:
    if i['month'] in solved:
        solved[i['month']].append(i['incident_code'])
    else: 
        solved[i['month']]= [i["incident_code"]]

#KPI4 DATA - backlog
backlog= {}
for i in KPI4JSON["items"]:
    if i['month'] in backlog:
        backlog[i['month']].append(i['incident_code'])
    else: 
        backlog[i['month']]= [i["incident_code"]]

@app.callback(
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

#kpi2 para borrar
# @app.callback(
#   Output(component_id="kpi2",component_property="figure"),
#   [Input(component_id="months", component_property="value")]
# )
# def update_KPI2(value):
#     return {
#       "data": [
#         {'x': monthskpi2,'y': incidenceskpi2, 'type': 'bar', 'name': value},
#         #{'x': ["Incidences Solved"], 'y': solved[value], 'type': 'bar', 'name': value},
#       ],
#       "layout": {
#         "title": "Incidences solved per month"
#       }
#     }

@app.callback(
  Output(component_id="kpi4",component_property="figure"),
  [Input(component_id="monthss", component_property="value")]
)
def update_KPI4(value):
    return {
      "data": [
        {'x': ["Incidences in backlog"], 'y': backlog[value], 'type': 'bar', 'name': value},
      ],
      "layout": {
        "title": "Incidences in backlog"
      }
    }

#if __name__ == "__main__":
app.run_server(debug=True)


#months=[]
#for i in KPI1JJSON["items"]:
    #months.append(i['month']) 

#incidences=[]
#for i in KPI1JJSON["items"]:
#    incidences.append(i['incidences_number'])
    
#priority=[]
#for i in KPI1JJSON["items"]:
#    priority.append(i['priority'])
    