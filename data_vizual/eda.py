import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

custom_colors = ["#A67BC5", "#BB1C8B", "#05A4C0", '#CCEBC5', "#D2A7D8", "#FFDAB9", '#FDDAEC', "#85CEDA", "#ADD8E6"]


class EDA_VISUAL:
    sample = pd.read_csv('data/aggregation/sample.csv')
    describe = pd.read_csv('data/aggregation/describe.csv')
    unique = pd.read_csv('data/aggregation/unique.csv')
    numeric = pd.read_csv('data/aggregation/all_prepared_for_learn_prep1_del_bundle.csv')

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

    dataset_train_size = 44854516
    nan_dict = {
        "gamecategory": 16961331 / dataset_train_size,
        "subgamecategory": 16968425 / dataset_train_size,
        "bundle": 17284 / dataset_train_size,
        "shift": 3591150 / dataset_train_size,
        "oblast": 3455278 / dataset_train_size,
        "city": 4799992 / dataset_train_size,
        "os": 233 / dataset_train_size,
        "osv": 283 / dataset_train_size
    }

    summury_class = {
        "5": 17187506,
        "3": 14187054,
        "4": 11142080,
        "2": 1416245,
        "1": 921631,
    }

    def aggregation_class(self):
        fig = go.Figure(data=[go.Pie(labels=list(self.summury_class.keys()),
                                     values=list(self.summury_class.values()))])

        fig.update_traces(hoverinfo='label+percent', textinfo='value',
                          marker=dict(colors=custom_colors))
        fig.show()

    def aggreg_nun(self):
        fig = go.Figure(data=[go.Pie(labels=list(self.nan_dict.keys()),
                                     values=list(self.nan_dict.values()))])

        fig.update_traces(hoverinfo='label+percent', textinfo='value',
                          marker=dict(colors=custom_colors))
        fig.show()

    # def aggreg_nun(self):
    #     fig = go.Figure(data=[go.Pie(labels=list(self.nan_dict.keys()),
    #                                  values=list(self.nan_dict.values()))])
    #
    #     fig.update_traces(hoverinfo='label+percent', textinfo='value',
    #                       marker=dict(colors=custom_colors))
    #     fig.show()

    def hist_(self):
        self.numeric.hist(bins=50, figsize=(60, 30), color='orchid')
