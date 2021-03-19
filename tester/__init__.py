import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import requests
import json
from dash.dependencies import Input, Output

#SIMPLE VERSION 

k1_endpoint = "https://qovo4nsf3oonbax-db202103111252.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip_rose/kpi1/incvol/"
k1_r = requests.get(k1_endpoint)
k1_kpi_data = k1_r.json()["items"]


k1_months = []
k1_incidences_numbers = []
k1_priorities = []

for dict in k1_kpi_data:
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

if __name__ == '__main__':
    app.run_server(debug=True)