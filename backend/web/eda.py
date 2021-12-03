import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly
import json


custom_colors = ["#A67BC5", "#BB1C8B", "#05A4C0", '#CCEBC5', "#D2A7D8", "#FFDAB9", '#FDDAEC', "#85CEDA", "#ADD8E6"]


class EDA_VISUAL:

    # import dash
    # import dash_table
    # import pandas as pd
    #
    # unique = pd.read_csv('data/aggregation/unique.csv')
    #
    # app = dash.Dash(__name__)
    #
    # app.layout = dash_table.DataTable(
    #     id='table',
    #     columns=[{"name": i, "id": i} for i in df.columns],
    #     data=df.to_dict('records'),
    # )
    #
    # if __name__ == '__main__':
    #     app.run_server(debug=True)

    def __init__(self, sample, describe, unique, numeric, nan_dict, summury_class):
        self.sample = sample
        self.describe = describe
        self.unique = unique
        self.numeric = numeric
        self.nan_dict = nan_dict
        self.summury_class = summury_class

    def _get_json_fig(self, fig):
        fig.update_xaxes(rangeslider_visible=True)
        fig.update_layout(width=1500, height=500)
        plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return plot_json

    def aggregation_class(self):
        fig = go.Figure(data=[go.Pie(labels=list(self.summury_class.keys()),
                                     values=list(self.summury_class.values()))])

        fig.update_traces(hoverinfo='label+percent', textinfo='value',
                          marker=dict(colors=custom_colors))
        return self._get_json_fig(fig)

    def aggreg_nun(self):
        fig = go.Figure(data=[go.Pie(labels=list(self.nan_dict.keys()),
                                     values=list(self.nan_dict.values()))])

        fig.update_traces(hoverinfo='label+percent', textinfo='value',
                          marker=dict(colors=custom_colors))

        return self._get_json_fig(fig)

    def aggreg_unique(self):
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(self.unique.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[self.unique.unique_values, self.unique.type, self.unique.pct_missing],
                       fill_color='lavender',
                       align='left'))
        ])
        return self._get_json_fig(fig)

    def hist_(self):
        self.numeric.hist(bins=50, figsize=(60, 30), color='orchid')