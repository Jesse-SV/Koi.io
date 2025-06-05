from dash import Dash, dcc, html, Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

app = Dash(__name__, external_stylesheets=external_stylesheets)

def generate_table(dataframe, columns_to_show, max_rows=10):
    # Filtra o DataFrame para mostrar apenas as colunas selecionadas
    filtered_df = dataframe[columns_to_show]
    return html.Div([
        html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in filtered_df.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(filtered_df.iloc[i][col]) for col in filtered_df.columns
                ]) for i in range(min(len(filtered_df), max_rows))
            ])
        ])
    ])

def generate_filter_column(df):
    return html.Div([
        html.H3('Filtros'),
        dcc.Checklist(
            id='column-selector',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[:3]  # Colunas selecionadas por padrão
        )
    ], style={'float': 'left', 'width': '20%'})

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Painel de Controle', value='tab-1'),
        dcc.Tab(label='Relatório', value='tab-2'),
        dcc.Tab(label='Ranking de Produtos', value='tab-3'),
        dcc.Tab(label='Entrada e Saída de Estoque', value='tab-4'),
        dcc.Tab(label='Produtos', value='tab-5'),
        dcc.Tab(label='Funcionários', value='tab-6'),
    ]),
    html.Div(id='tabs-content'),
])

@app.callback(Output('tabs-content', 'children'), [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Painel de Controle'),
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Relatório'),
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Ranking de Produtos'),
            generate_filter_column(df),
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Entrada e Saída de Estoque'),
            generate_filter_column(df),
        ])
    elif tab == 'tab-5':
        return html.Div([
            html.H3('Produtos'),
            generate_filter_column(df),
        ])
    elif tab == 'tab-6':
        return generate_table(df, df.columns[:3])
    else:
        return html.Div([])

if __name__ == '__main__':
    app.run_server(debug=True)
