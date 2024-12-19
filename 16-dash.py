import dash
from dash import dcc, html, Input, Output, State
import pandas as pd

# 读取CSV文件
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# 初始化Dash应用
app = dash.Dash(__name__)

# 加载数据文件
file_path = 'data\\2022计算机设计大赛国奖清理后-增加变量.csv'
df = load_data(file_path)

# 定义应用布局
app.layout = html.Div([
    html.H1("CSV查询工具", style={'textAlign': 'center', 'background': 'linear-gradient(-45deg, #fff566, #a8ffca, #ffad61, #ff857a, #fff, #ff5cc9, #6279ea, #66ffe6)', 'WebkitBackgroundClip': 'text', 'WebkitTextFillColor': 'transparent','background-size': '300%;'}),
    
    html.Div([
        html.Label("选择大类名称:"),
        dcc.Dropdown(id='category-dropdown'),
        html.Label("选择奖项:"),
        dcc.Dropdown(id='award-dropdown'),
        html.Button('查询', id='query-button', n_clicks=0)
    ]),
    html.Div(id='query-result')
])

# 更新下拉菜单选项
@app.callback(
    [Output('category-dropdown', 'options'),
     Output('award-dropdown', 'options')],
    Input('query-result', 'children'))
def update_dropdowns(children):
    categories = df['大类名称'].unique()
    awards = df['奖项'].unique()
    return [{'label': i, 'value': i} for i in categories], [{'label': i, 'value': i} for i in awards]

# 查询结果显示
@app.callback(
    Output('query-result', 'children'),
    Input('query-button', 'n_clicks'),
    State('category-dropdown', 'value'),
    State('award-dropdown', 'value'))
def update_query_result(n_clicks, category, award):
    if n_clicks == 0:
        return html.Div()
    if category and award:
        result = df[(df['大类名称'] == category) & (df['奖项'] == award)]
    elif category:
        result = df[df['大类名称'] == category]
    elif award:
        result = df[df['奖项'] == award]
    else:
        result = df
    return html.Div([
        html.H5("查询结果:"),
        html.Pre(result.to_string())
    ])

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)