from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc


def table_models(df):
    cols = [
            {"name": i, "id": i, "hideable": True, "selectable": True, 'editable': i == 'name'}
            for i in df.columns
        ]

    return dbc.Container(
        [
            html.Div(
                id='hidden-div-table',
                style={'display': 'none'}
            ),
            html.Div(
                id='hidden-div-table2',
                style={'display': 'none'}
            ),
            html.Hr(),
            dbc.DropdownMenu(
                label="Menu",
                id='table-menu',
                children=[
                    dbc.DropdownMenuItem("Export weights", id='export-weights'),
                    dbc.DropdownMenuItem("Convert weights", id='convert-weights'),
                ],
                style={"margin-bottom": "1%"}
            ),
            dcc.Download(id="download-weights"),
            html.Div(
                [
                    dash_table.DataTable(
                        id='stats-models-table',
                        columns=cols,
                        data=df.to_dict('records'),
                        # editable=True,
                        filter_action="native",
                        sort_action="native",
                        sort_mode="multi",
                        row_selectable="multi",
                        row_deletable=True,
                        page_action="native",
                        page_current=0,
                        page_size=10,
                        css=[
                            {'selector': 'table', 'rule': 'table-layout: fixed'},
                        ],
                        style_cell={
                            'width': '{}%'.format(len(df.columns)),
                            'textOverflow': 'ellipsis',
                            'overflow': 'hidden'
                        },
                        export_format='csv',
                    ),
                ],
                # className='table'
            )
        ]
    )
