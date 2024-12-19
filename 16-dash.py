import dash
from dash import dcc, html, Input, Output, State, dash_table
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
    html.Div(id='query-result'),
    
    # 新增按钮：获奖作品特征分析
    html.Button('获奖作品特征分析', id='analysis-button', n_clicks=0, style={'marginTop': '20px'}),
    html.Div(id='analysis-result'),  # 用于显示分析结果
    
    # 页面底部版权信息
    html.Footer([
        html.P("西北民族大学新闻传播学院《大数据与人工智能》课程作品", style={'fontSize': 12, 'textAlign': 'center', 'color': '#333'}),
        html.P("作者：XXX", style={'fontSize': 12, 'textAlign': 'center', 'color': '#333'})
    ], style={'backgroundColor': '#f0f0f0', 'padding': '10px', 'marginTop': '20px'})
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
    
    # 过滤掉名为 'Unnamed' 的列
    columns_to_display = [col for col in result.columns if not col.startswith('Unnamed')]
    
    # 使用 dash_table.DataTable 显示结果
    return html.Div([
        html.H5("查询结果:"),
        dash_table.DataTable(
            data=result[columns_to_display].to_dict('records'),  # 仅显示需要的列
            columns=[{'name': col, 'id': col} for col in columns_to_display],  # 定义表格列
            style_table={'overflowX': 'auto'},  # 自动水平滚动
            style_cell={'textAlign': 'left'},  # 单元格内容左对齐
            sort_action='native',  # 启用排序功能
            filter_action='native',  # 启用筛选功能
            page_action='native',  # 启用分页功能
            page_size=10  # 每页显示10行
        )
    ])

# 获奖作品特征分析
@app.callback(
    Output('analysis-result', 'children'),
    Input('analysis-button', 'n_clicks'),
    State('category-dropdown', 'value'),  # 获取当前选择的大类名称
    State('award-dropdown', 'value'))  # 获取当前选择的奖项
def analyze_award_features(n_clicks, category, award):
    if n_clicks == 0:
        return html.Div()
    
    # 根据当前查询条件筛选数据
    if category and award:
        filtered_df = df[(df['大类名称'] == category) & (df['奖项'] == award)]
    elif category:
        filtered_df = df[df['大类名称'] == category]
    elif award:
        filtered_df = df[df['奖项'] == award]
    else:
        filtered_df = df
    
    # 示例分析：统计获奖作品的奖项分布
    award_counts = filtered_df['奖项'].value_counts().reset_index()
    award_counts.columns = ['奖项', '数量']
    
    # 显示分析结果
    return html.Div([
        html.H5("获奖作品特征分析结果:"),
        dash_table.DataTable(
            data=award_counts.to_dict('records'),
            columns=[{'name': col, 'id': col} for col in award_counts.columns],
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
            sort_action='native',
            filter_action='native',
            page_action='native',
            page_size=10
        )
    ])

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)