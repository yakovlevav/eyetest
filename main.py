# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import math

in_ft = [70, 60, 50, 40, 30, 20, 15, 10, 7, 4]
conversion = 0.3048
in_m = list(map(lambda a: a*conversion, in_ft))
print(in_m)
font_size =  [152, 130, 108, 87, 65, 43, 33, 21, 15, 9]

# print(10/21)
# print(2.1336/15)
# print(1.2192/9)

#Calculation of the letter size
a = lambda d: 2*d*math.atan(5/2)
print(a(7))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.P(children='ABCDFG', style={
        'textAlign': 'center',
        'font-family':'сourier Bold', 
        'fontSize':'50pt',
        'color':'black'
        }),
    html.P(children='ABCDFG', style={
        'textAlign': 'center',
        # 'fontType':'Courier', 
        'fontSize':'50mm'
        }),
])

if __name__ == '__main__':
    app.run_server(debug=True)