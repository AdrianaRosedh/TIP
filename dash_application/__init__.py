import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import requests

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname='/dash/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='example-graph',
            figure=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
        ),  
        
    )

    return dash_app

# KPI 1 Information

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
    dash_app1 = dash.Dash(server=flask_app, name="kpi1", url_base_pathname='/kpi1/')
    
    dash_app1.layout = html.Div(
        dcc.Graph(
            id='kpi1-graph',
            figure= px.bar(k1_df, x="Months", y="Number of incidents", color="Priority", barmode="group")
        ),  
        
    )

    return dash_app1

if __name__ == '__main__':
    app.run_server(debug=True)