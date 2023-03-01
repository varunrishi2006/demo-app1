import dash
from dash import Dash, html, dcc, Input, Output, State, dash_table
import plotly.express as px
import pandas as pd
from pandas.api.types import CategoricalDtype
from datetime import datetime as dt, date
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Code for initial preprocessing of booking curve dataframe starts here
df_booking_curve = pd.read_excel('C:/Users/varun/PycharmProjects/Deploy_App_to_Web/PythonAnyWhere/demo-app1/Sample_Data.xlsx', sheet_name='View1')
df_booking_curve['Total Rev (Historical)'] = df_booking_curve['Total Rev (Historical)'].astype(int)
df_booking_curve['Avg Fare (Historical)'] = df_booking_curve['Avg Fare (Historical)'].astype(int)
df_booking_curve['Booked Historical'] = df_booking_curve['Booked Historical'].astype(int)

print(df_booking_curve.shape)

category_order = CategoricalDtype([
    '0-7',
    '8-15',
    '16-30',
    '31-60',
    '61-90',
    '91-120',
    '>120',
], ordered=True)

df_booking_curve.loc[df_booking_curve['NDO'].between(0, 7, 'both'), 'NDO Range'] = '0-7'
df_booking_curve.loc[df_booking_curve['NDO'].between(8, 15, 'both'), 'NDO Range'] = '8-15'
df_booking_curve.loc[df_booking_curve['NDO'].between(16, 30, 'both'), 'NDO Range'] = '16-30'
df_booking_curve.loc[df_booking_curve['NDO'].between(31, 60, 'both'), 'NDO Range'] = '31-60'
df_booking_curve.loc[df_booking_curve['NDO'].between(61, 90, 'both'), 'NDO Range'] = '61-90'
df_booking_curve.loc[df_booking_curve['NDO'].between(91, 120, 'both'), 'NDO Range'] = '91-120'
df_booking_curve.loc[df_booking_curve['NDO'].between(120, 365, 'both'), 'NDO Range'] = '>120'
# Code for initial preprocessing of booking curve dataframe ends here

df_forecast = pd.read_excel('C:/Users/varun/PycharmProjects/Deploy_App_to_Web/PythonAnyWhere/demo-app1/Sample_Data.xlsx', sheet_name='View2')

df_product = pd.read_excel('C:/Users/varun/PycharmProjects/Deploy_App_to_Web/PythonAnyWhere/demo-app1/Sample_Data.xlsx', sheet_name='View3')

df_product.rename(columns={'NDO Range':'NDO'},inplace=True)

df_product.loc[df_product['NDO'].between(0, 7, 'both'), 'NDO Range'] = '0-7'
df_product.loc[df_product['NDO'].between(8, 15, 'both'), 'NDO Range'] = '8-15'
df_product.loc[df_product['NDO'].between(16, 30, 'both'), 'NDO Range'] = '16-30'
df_product.loc[df_product['NDO'].between(31, 60, 'both'), 'NDO Range'] = '31-60'
df_product.loc[df_product['NDO'].between(61, 90, 'both'), 'NDO Range'] = '61-90'
df_product.loc[df_product['NDO'].between(91, 120, 'both'), 'NDO Range'] = '91-120'
df_product.loc[df_product['NDO'].between(120,365, 'both'), 'NDO Range'] = '>120'

df_product['NDO Range'] = df_product['NDO Range'].astype(category_order)

df_journey = pd.read_excel('C:/Users/varun/PycharmProjects/Deploy_App_to_Web/PythonAnyWhere/demo-app1/Sample_Data.xlsx', sheet_name='View4')

df_journey.rename(columns={'NDO Range':'NDO'}, inplace=True)

df_journey.loc[df_journey['NDO'].between(0, 7, 'both'), 'NDO Range'] = '0-7'
df_journey.loc[df_journey['NDO'].between(8, 15, 'both'), 'NDO Range'] = '8-15'
df_journey.loc[df_journey['NDO'].between(16, 30, 'both'), 'NDO Range'] = '16-30'
df_journey.loc[df_journey['NDO'].between(31, 60, 'both'), 'NDO Range'] = '31-60'
df_journey.loc[df_journey['NDO'].between(61, 90, 'both'), 'NDO Range'] = '61-90'
df_journey.loc[df_journey['NDO'].between(91, 120, 'both'), 'NDO Range'] = '91-120'
df_journey.loc[df_journey['NDO'].between(120,365, 'both'), 'NDO Range'] = '>120'

df_journey['NDO Range'] = df_journey['NDO Range'].astype(category_order)

# card_total_users = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H5(f'Total No. of Users', className="card-title-1", style={'textAlign': 'centre'}),
#             html.H5(f'{total_users}', className="card-text-1", style={'textAlign': 'centre'})
#         ]),
#     ], style={'textAlign': 'center'}, color="rgb(211, 211, 211)"
# )
# card_total_users_mc = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H5(f'No. of Signed-up Users (User/Manual_Client)', className="card-title-2"),
#             html.H5(f'{total_users_mc}', className="card-text-2")
#         ]),
#     ], style={'textAlign': 'center'}, color="rgb(211, 211, 211)"
# )
# card_active_users = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H5(f'No. of users with at-least one valid integration', className="card-title-3"),
#             html.H5(f'{active_users}', className="card-text-3")
#         ]),
#     ], style={'textAlign': 'center'}, color="rgb(211, 211, 211)"
# )
# card_no_integration = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H5(f'No. of Users with no integration', className="card-title-4"),
#             html.H5(f'{user_no_integration}', className="card-text-4")
#         ]),
#     ], style={'textAlign': 'center'}, color="rgb(211, 211, 211)"
# )
# card_avg_integration_user = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H5(f'Avg. Integration per Active Users', className="card-title-5"),
#             html.H5(f'{avg_integration_per_user}', className="card-text-5")
#         ]),
#     ], style={'textAlign': 'center'}, color="rgb(211, 211, 211)"
# )
# card_total_processed_value = dbc.Card(
#     [
#         dbc.CardBody([
#             html.H5(f'Total Transaction Value', className="card-title-6"),
#             html.H5(f'{total_processed_value}', className="card-text-6")
#         ]),
#     ], style={'textAlign': 'center', 'textAuto' : '.6s'}, color="rgb(211, 211, 211)"
# )


style = {
    'writing-mode': 'vertical-lr',
    'white-space': 'nowrap'
}

# app = Dash(external_stylesheets=[dbc.themes.MORPH])
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H4("Booking Insights",
            style={'font-weight': 'bold', "textAlign": "center", 'marginBottom': 20, 'marginTop': 25}),

    html.Br(),
    dbc.Row(
        [
            html.Div([
                html.Label('Select a Dimension :',
                           style={'font-weight': 'bold'}),
                dcc.RadioItems(id='data-radio-dimension',
                               options={
                                   'load': 'Booking Comparison',
                                   'revenue': 'Revenue Comparison',
                                   'fare': 'Fare Comparison'

                               },
                               value='load',
                               inputStyle={'margin-right': '10px'},
                               labelStyle={'display': 'inline-block', 'padding': '0.5rem 0.5rem'}
                               )
            ]
            )
        ]
    ),
    dbc.Row(
        [html.Div([
            dcc.Graph(id='fig-booking-curve')
        ], className='nine columns'),

            # html.Div([
            #     dbc.CardGroup(
            #         [card_total_users, card_total_users_mc, card_active_users, card_no_integration, card_avg_integration_user, card_total_processed_value])
            # ]),
            #
            # html.Br(),

            html.Div([
                dbc.Label('Historical Date Range', style={'font-weight': 'bold'}),
                dcc.DatePickerRange(
                    id='historical-date-picker-range',
                    start_date=date(2022, 4, 1),
                    end_date=date(2022, 6, 1),
                    initial_visible_month=date(2022, 5, 1),
                    min_date_allowed=date(2020, 1, 1),
                    max_date_allowed=date(2023, 2, 28),
                ),
                html.P(),
                dbc.Label('Current Date Range', style={'font-weight': 'bold'}),
                dcc.DatePickerRange(
                    id='current-date-picker-range',
                    start_date=date(2023, 3, 4),
                    end_date=date(2023, 3, 4),
                    initial_visible_month=date(2023, 3, 4),
                    min_date_allowed=date(2020, 1, 1),
                    max_date_allowed=date(2023, 12, 31),
                ),
                html.P(),
                dbc.Label('Market', style={'font-weight': 'bold'}),
                dcc.Dropdown(
                    options=['BLRDXB', 'DELDXB', 'BOMDXB'],
                    value='BLRDXB',
                    id='market-dropdown',
                    clearable=False,
                    searchable=True,
                    placeholder='Please select...',
                    style={'color': 'black', 'font-size': 15}),
                html.P(),
                dbc.Label('Sector', style={'font-weight': 'bold'}),
                dcc.Dropdown(
                    options=['BLRDXB', 'DXBBLR'],
                    value='BLRDXB',
                    id='sector-dropdown',
                    clearable=False,
                    searchable=True,
                    placeholder='Please select...',
                    style={'color': 'black', 'font-size': 15}),
                html.P(),
                dbc.Label('Flight No.', style={'font-weight': 'bold'}),
                dcc.Dropdown(
                    options=[1111, 2222, 3333, 4444],
                    value=1111,
                    id='flight-dropdown',
                    clearable=False,
                    searchable=True,
                    placeholder='Please select...',
                    style={'color': 'black', 'font-size': 15}),
            ],
                className='two columns'
            )]
    ),

    html.P(),
    html.Br(),

    html.P(),
    html.Br(),

    dbc.Row([
        html.Div([
            dcc.Graph(id='forecast-graph')
            ], className='nine columns')
    ]),
    html.P(),
    html.Br(),

    dbc.Row([
        html.Div([
            html.Label(['NDO Range :'], style={'font-weight': 'bold'}),
            dcc.Checklist(
                id='ndo_range_checklist',
                options=df_product['NDO Range'].unique(),
                value=df_product['NDO Range'].unique(),
                inline=True,
                inputStyle={'margin-right': '10px'},
                labelStyle={'padding': '0.5rem 0.5rem', 'border-radius': '1rem'}
            )
    ])]),
    #
    # html.P(),
    # html.Br(),
    #
    dbc.Row([
        html.Div([
            dcc.Graph(id='product-graph')
            ], className='nine columns')
    ]),

    html.P(),
    html.Br(),

    dbc.Row([
        html.Div([
            html.Label(['NDO Range :'], style={'font-weight': 'bold'}),
            dcc.Checklist(
                id='ndo_range_checklist_1',
                options=df_journey['NDO Range'].unique(),
                value=df_journey['NDO Range'].unique(),
                inline=True,
                inputStyle={'margin-right': '10px'},
                labelStyle={'padding': '0.5rem 0.5rem', 'border-radius': '1rem'}
            )
    ])]),
    #
    # html.P(),
    # html.Br(),
    #
    dbc.Row([
        html.Div([
            dcc.Graph(id='journey-graph')
            ], className='nine columns')
    ]),

    # html.Div([
    #     html.Label('Select a Dimension :',
    #                style={'font-weight': 'bold'}),
    #     dcc.RadioItems(id='data-radio-x',
    #                    options={
    #                        'source': 'Exchange',
    #                        'Coin': 'Coin (Top 50 by Transactions)'
    #                    },
    #                    value='source',
    #                    inputStyle={'margin-right': '10px'},
    #                    labelStyle={'padding': '0.5rem 0.5rem'}
    #                    )
    # ]),
    # html.P(),
    #
    # html.Div([
    #     html.Label('Select a Metric :',
    #                style={'font-weight': 'bold'}),
    #     dcc.RadioItems(id='data-radio-y',
    #                    options={
    #                        'unique_integrations': 'Integrations',
    #                        'total_trnxs': 'Total Transactions',
    #                    },
    #                    value='total_trnxs',
    #                    inputStyle={'margin-right': '10px'},
    #                    labelStyle={'padding': '0.5rem 0.5rem'}
    #                    )
    # ]),

    html.Br(),
    html.P()

])


# -----------------------------------------------------------------------------------------------------------------------

@app.callback(
    Output('fig-booking-curve', 'figure'),
    Input('sector-dropdown', 'value'),
    Input('data-radio-dimension', 'value')
)
def updated_booking_curve(sector, dimension):
    y1 = ""
    y2 = ""
    name1 = ""
    name2 = ""
    df_curve = df_booking_curve[df_booking_curve['Sector'] == sector]
    if dimension == 'load':
        y1 = 'Booked Historical'
        y2 = 'Current'
        name1 = 'Flown Load'
        name2 = 'Booked Load'
    elif dimension == 'revenue':
        y1 = 'Total Rev (Historical)'
        y2 = 'Current Revenue'
        name1 = 'Historical Revenue'
        name2 = 'Current Revenue'
    else:
        y1 = 'Avg Fare (Historical)'
        y2 = 'Current Fare'
        name1 = 'Historical Avg. Fare'
        name2 = 'Current Avg. Fare'

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_curve['NDO'], y=df_curve[y1],
                             mode='lines', name=name1))
    fig.add_trace(go.Scatter(x=df_curve['NDO'], y=round(df_curve[y2]),
                             mode='lines', name=name2))
    fig.update_layout(title={'text': 'Booking Curve by NDO', 'font': {'size': 20}},
                      xaxis_title='NDO',
                      # yaxis_title='Booked/Flown Loads',
                      paper_bgcolor='rgba(0,0,0,0)')

    return fig


@app.callback(
    Output('forecast-graph', 'figure'),
    Input('sector-dropdown', 'value'),
)
def updated_forecast_effect(sector):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    # fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_forecast['NDO'], y=df_forecast['Forecast'],
                             mode='lines', name='Forecast'), secondary_y=False)
    fig.add_trace(go.Scatter(x=df_forecast['NDO'], y=df_forecast['Avg. Fare'],
                             mode='lines', name='Fare Trend'), secondary_y=True)
    # fig.add_trace(go.Scatter(x=df_forecast['NDO'], y=df_forecast['Forecasted RASK'],
    #                          mode='lines', name='RASK Trend'))
    fig.update_layout(title={'text': 'Forecast trend', 'font': {'size': 20}},
                      xaxis_title='NDO',
                      # yaxis_title='Booked/Flown Loads',
                      paper_bgcolor='rgba(0,0,0,0)')

    return fig

@app.callback(
    Output('product-graph', 'figure'),
    Input('sector-dropdown', 'value'),
    [Input('ndo_range_checklist', 'value')]
)
def update_product_graph(sector,ndo_range_list):
    df_product_1 = df_product[(df_product['Sector'] == sector) & (df_product['NDO Range'].isin(ndo_range_list))]
    df_grouped_product = df_product_1.groupby(['Product', 'Actual/Historical']).\
        agg({'Booked Seats': 'sum'}).reset_index()
    fig = px.bar(df_grouped_product, x='Product', y='Booked Seats', color='Actual/Historical', barmode='group')
    fig.update_layout(title='Booking Distribution by Product')

    return fig

@app.callback(
    Output('journey-graph', 'figure'),
    Input('sector-dropdown', 'value'),
    [Input('ndo_range_checklist_1', 'value')]
)
def update_product_graph(sector,ndo_range_list):
    df_journey_1 = df_journey[(df_journey['Sector'] == sector) & (df_journey['NDO Range'].isin(ndo_range_list))]
    df_grouped_journey = df_journey_1.groupby(['Feeding Sector', 'Actual/Historical']).\
        agg({'Booked Seats': 'sum'}).reset_index()
    fig = px.bar(df_grouped_journey, x='Feeding Sector', y='Booked Seats', color='Actual/Historical', barmode='group')
    fig.update_layout(title='Booking Distribution by Journey')

    return fig


# def update_graph(start_date, end_date, user_roles):
#     print(df.head())
#     print(f'update_graph {start_date}')
#     print(f'update_graph {end_date}')
#     print(user_roles)
#     # print(s[years_chosen[1]])
#
#     # dff = df[(df['month-year'] >= s[years_chosen[0]]) & (df['month-year'] <= s[years_chosen[1]])]
#     dff = df[(df['month-year'] >= start_date) & (df['month-year'] <= end_date)]
#     dff = dff[dff['role'].isin(user_roles)]
#     print(dff.shape)
#     print((dff['user'].nunique()))
#     df_user_trnxs = dff.groupby('user').agg({'total_trnxs': 'sum'}). \
#         sort_values(by='total_trnxs', ascending=False).reset_index()
#     print(df_user_trnxs.shape)
#
#     df_user_trnxs['total_trnxs'] = df_user_trnxs['total_trnxs'].astype('float')
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(0, 25, 'both'), 'Trnx_Interval'] = '[0-25]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(25, 50, 'right'), 'Trnx_Interval'] = '(25-50]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(50, 100, 'right'), 'Trnx_Interval'] = '(50-100]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(100, 150, 'right'), 'Trnx_Interval'] = '(100-150]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(150, 200, 'right'), 'Trnx_Interval'] = '(150-200]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(200, 300, 'right'), 'Trnx_Interval'] = '(200-300]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(300, 400, 'right'), 'Trnx_Interval'] = '(300,400]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(400, 500, 'right'), 'Trnx_Interval'] = '(400,500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(500, 600, 'right'), 'Trnx_Interval'] = '(500,600]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(600, 700, 'right'), 'Trnx_Interval'] = '(600,700]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(700, 800, 'right'), 'Trnx_Interval'] = '(700,800]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(800, 900, 'right'), 'Trnx_Interval'] = '(800,900]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(900, 1000, 'right'), 'Trnx_Interval'] = '(900,10000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(1000, 1500, 'right'), 'Trnx_Interval'] = '(1000,1500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(1500, 2000, 'right'), 'Trnx_Interval'] = '(1500,2000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(2000, 2500, 'right'), 'Trnx_Interval'] = '(2000,2500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(2500, 3000, 'right'), 'Trnx_Interval'] = '(2500,3000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(3000, 3500, 'right'), 'Trnx_Interval'] = '(3000,3500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(3500, 4000, 'right'), 'Trnx_Interval'] = '(3500,4000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(4000, 4500, 'right'), 'Trnx_Interval'] = '(4000,4500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(4500, 5000, 'right'), 'Trnx_Interval'] = '(4500,5000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(5000, 5500, 'right'), 'Trnx_Interval'] = '(5000,5500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(5500, 6000, 'right'), 'Trnx_Interval'] = '(5500,6000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(6000, 6500, 'right'), 'Trnx_Interval'] = '(6000,6500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(6500, 7000, 'right'), 'Trnx_Interval'] = '(6500,7000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(7000, 7500, 'right'), 'Trnx_Interval'] = '(7000,7500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(7500, 8000, 'right'), 'Trnx_Interval'] = '(7500,80000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(8000, 8500, 'right'), 'Trnx_Interval'] = '(8000,8500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(8500, 9000, 'right'), 'Trnx_Interval'] = '(8500,9000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(9000, 9500, 'right'), 'Trnx_Interval'] = '(9000,9500]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(9500, 10000, 'right'), 'Trnx_Interval'] = '(9500,10000]'
#     df_user_trnxs.loc[df_user_trnxs['total_trnxs'].between(10000, 9999999, 'right'), 'Trnx_Interval'] = '(>10000]'
#
#     df_user_trnxs['Trnx_Interval'] = df_user_trnxs['Trnx_Interval'].astype(category_order)
#     print(df_user_trnxs.shape)
#
#     df_final = df_user_trnxs['Trnx_Interval'].value_counts().sort_index().reset_index(). \
#         rename(columns={'index': 'Transaction Range', 'Trnx_Interval': 'Total Users'})
#     print(df_final.shape)
#     print(df_final)
#
#     fig = px.bar(df_final, x='Transaction Range', y='Total Users', text_auto='s', template='ggplot2')
#     fig.update_traces(textfont_size=20, textangle=0, textposition="outside", cliponaxis=False)
#     fig.update_layout(title='No. of Users by Transaction Range', paper_bgcolor='rgba(0,0,0,0)')
#
#     return fig
#
#
# @app.callback(
#     Output('campaign-graph', 'figure'),
#     [Input('my-date-picker-range', 'start_date'),
#      Input('my-date-picker-range', 'end_date')],
#     [Input('user_checklist', 'value')]
# )
# def campaign_details(start_date, end_date, user_roles):
#     print(f'campaign_details {start_date}')
#     print(f'campaign_details {end_date}')
#     print(f'campaign_details {user_roles}')
#
#     # df_campaign_details_init = df_campaign_details[(df_campaign_details['month-year'] >= s[years_chosen[0]]) & (
#     #         df_campaign_details['month-year'] <= s[years_chosen[1]])]
#
#     df_campaign_details_init = df_campaign_details[(df_campaign_details['month-year'] >= start_date) & (
#             df_campaign_details['month-year'] <= end_date)]
#
#     df_campaign_details_init = df_campaign_details_init[df_campaign_details_init['calc_roles'].isin(user_roles)]
#
#     df_campaign_details_final = df_campaign_details_init['campaignCode'].value_counts().sort_values(
#         ascending=False).reset_index(). \
#         rename(columns={'index': 'Campaign Code', 'campaignCode': 'User Count'})
#
#     fig = px.bar(df_campaign_details_final, x='Campaign Code', y='User Count', text_auto='s', template='ggplot2')
#     fig.update_layout(title='No. of Users by Campaign Code', paper_bgcolor='rgba(0,0,0,0)')
#     fig.update_traces(textfont_size=20, textangle=0, textposition="outside", cliponaxis=False)
#
#     return fig
#
#
# @app.callback(
#     Output('integration-transaction', 'figure'),
#     Input('data-radio-x', 'value'),
#     Input('data-radio-y', 'value'),
#     [Input('user_checklist', 'value')],
#     [Input('my-date-picker-range', 'start_date'),
#      Input('my-date-picker-range', 'end_date')])
# def update_integration_trnxs(grouped_dimension, grouped_metric, user_role, start_date, end_date):
#     if grouped_dimension == 'source':
#         # df_user_intg_init = df_user_intg[(df_user_intg['month-year'] >= s[years_chosen[0]]) & (
#         #         df_user_intg['month-year'] <= s[years_chosen[1]])]
#         df_user_intg_init = df_user_intg[(df_user_intg['month-year'] >= start_date) & (
#                 df_user_intg['month-year'] <= end_date)]
#         df_user_intg_final = df_user_intg_init[df_user_intg_init['calc_roles'].isin(user_role)]
#
#         print(df_user_intg_final.shape)
#         print(df_user_intg_final.head())
#
#         if grouped_metric == 'total_trnxs':
#             df_source = df_user_intg_final.groupby(grouped_dimension)[grouped_metric].sum(). \
#                 sort_values(ascending=False).reset_index(). \
#                 rename(columns={'source': 'Exchange', 'total_trnxs': 'Total Transactions'})
#             fig = px.bar(df_source, x='Exchange', y='Total Transactions', text_auto='.2s', template='ggplot2')
#             fig.update_layout(title='Total Transactions by Exchange', paper_bgcolor='rgba(0,0,0,0)')
#
#         else:
#             df_source = df_user_intg_final.groupby(grouped_dimension)['walletId'].nunique(). \
#                 sort_values(ascending=False).reset_index(). \
#                 rename(columns={'source': 'Exchange', 'walletId': 'Unique Integrations'})
#             fig = px.bar(df_source, x='Exchange', y='Unique Integrations', text_auto='.2s', template='ggplot2')
#             fig.update_layout(title='Unique Integrations by Exchange', paper_bgcolor='rgba(0,0,0,0)')
#
#     else:
#         df_coin_wallet_intg_init = df_coin_wallet_intg[(df_coin_wallet_intg['month-year'] >= start_date) &
#                                                        (df_coin_wallet_intg['month-year'] <= end_date)]
#         df_coin_wallet_intg_final = df_coin_wallet_intg_init[df_coin_wallet_intg_init['calc_roles'].isin(user_role)]
#
#         print(df_coin_wallet_intg_final.shape)
#         print(df_coin_wallet_intg_final.head())
#
#         if grouped_metric == 'total_trnxs':
#             df_coin = df_coin_wallet_intg_final.groupby(grouped_dimension)[grouped_metric].sum(). \
#                 sort_values(ascending=False).reset_index(). \
#                 rename(columns={'total_trnxs': 'Total Transactions'})
#             fig = px.bar(df_coin, x='Coin', y='Total Transactions', text_auto='.2s', template='ggplot2')
#             fig.update_layout(title='Total Transactions by Coin', paper_bgcolor='rgba(0,0,0,0)')
#
#
#         else:
#             df_coin = df_coin_wallet_intg_final.groupby(grouped_dimension)['unique_integrations'].sum(). \
#                 sort_values(ascending=False).reset_index(). \
#                 rename(columns={'unique_integrations': 'Unique Integrations'})
#             fig = px.bar(df_coin, x='Coin', y='Unique Integrations', text_auto='.2s', template='ggplot2')
#             fig.update_layout(title='Unique Integrations by Coin', paper_bgcolor='rgba(0,0,0,0)')
#
#     return fig
#
#
# @app.callback(
#     Output('dd-output-container', 'figure'),
#     Input('demo-dropdown', 'value'),
#     Input('data-radio-z', 'value'),
#     [Input('my-date-picker-range', 'start_date'),
#      Input('my-date-picker-range', 'end_date')],
#     [Input('user_checklist', 'value')]
# )
# def update_output(selected_exchange, grouped_metric, start_date, end_date, user_role):
#     df_coin_wallet_intg_init = df_coin_wallet_intg[(df_coin_wallet_intg['month-year'] >= start_date) & (
#             df_coin_wallet_intg['month-year'] <= end_date)]
#     df_coin_wallet_intg_final = df_coin_wallet_intg_init[df_coin_wallet_intg_init['calc_roles'].isin(user_role)]
#
#     print(df_coin_wallet_intg_final.shape)
#     print(df_coin_wallet_intg_final.head())
#
#     df_coin = df_coin_wallet_intg_final[df_coin_wallet_intg_final['source'] == selected_exchange].groupby('Coin')[
#                   grouped_metric]. \
#                   sum().sort_values(ascending=False).reset_index()[:50]
#
#     df_coin.rename(columns={'unique_integrations': 'Unique Integrations',
#                             'Unique users': 'Unique Users',
#                             'total_trnxs': 'Total Transactions'}, inplace=True)
#     y_axis = df_coin.columns[1]
#     fig = px.bar(df_coin, x='Coin', y=y_axis, text_auto=".2s", template='ggplot2')
#     fig.update_layout(title=f'{y_axis} by Coin', paper_bgcolor='rgba(0,0,0,0)')
#
#     return fig


if __name__ == '__main__':
    app.run_server(debug=True)
