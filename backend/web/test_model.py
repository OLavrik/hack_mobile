import json

import pandas as pd
import plotly
import plotly.graph_objects as go
from prettytable import *
import plotly.express as px

current_model_name = None
model = None
custom_colors = ["#ff9999", "#ffb399", "#ffcc99", '#ffe699', "#ffff99", "#e6ff99", '#ccff99', "#b3ff99", "#99ff99",
                 "#99ffb3", "#99ffcc", "#99ffe6", "#99ffff", "#99e6ff", "#99ccff", "#99b3ff", "#9999ff", "#b399ff",
                 "#cc99ff", "#e699ff", "#ff99ff", "#ff99e6", "#ff99cc"]

test_sample = pd.read_csv('web/static/data/test_sample.csv')
test_post_sample = pd.read_csv('web/static/data/test_post_sample.csv')
test_sample_predict = pd.read_csv('web/static/data/test_sample_predict.csv')
df_plot = pd.read_csv('web/static/data/importence_features.csv')


def plot_I():
    fig = px.bar(x=df_plot.importances,
                 y=df_plot.features,
                 color=custom_colors,
                 title="Feature Importance",
                 labels={'x': 'importance', 'y': 'features'})

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(width=1500, height=500)
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_json
    # df_plot=pd.read_csv()
    # plt.style.use('ggplot')
    # plt.figure(figsize=[30, 17])
    # sns.barplot(x=df_plot.importances, y=df_plot.features)
    # plt.title('Importances of Features Plot')
    # plt.show()


def load_model(model_name):
    global current_model_name
    if current_model_name is None or model_name != model_name:
        if model_name == 'CatBoost':
            from catboost import CatBoost

            global model
            model = CatBoost()
            model.load_model(
                "web/static/catboostmodelname"
            )
        elif model_name == 'GradientBoosting':
            pass
        else:
            raise ValueError(f"Unknown model_name value: {model_name}")

        current_model_name = model_name

        return False

    return True


def run_model_on_test(cash):
    cash = True
    if cash:
        return result_df

    pass


def plot_predicts(df, title):
    df = df.fillna('NONE')
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df[col].values for col in df.columns],
                   fill_color='lavender',
                   align='left'))
    ])

    fig.update_layout(
        title=title
    )

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(width=1500, height=500)
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_json


def load_model_info(model_name):
    if model_name == 'CatBoost':
        table = PrettyTable(["class", "     precision", "     recall", "     f1-score", "     support"])
        table.add_row(["1", "     0.34", "0.01", "     0.02", "     77220"])
        table.add_row(["2", "     0.48", "     0.51", "     0.49", "     274437"])
        table.add_row(["3", "     0.70", "     0.62", "     0.66", "     2568770"])
        table.add_row(["4", "     0.65", "     0.52", "     0.58", "     1311034"])
        table.add_row(["5", "     0.75", "     0.89", "     0.81", "     3233511"])
        table.add_row(["accuracy", "     ", "     ", "     0.71", "     7464972"])
        table.add_row(["macro avg", "     0.58", "     0.51", "     0.51", "     7464972"])
        table.add_row(["weighted avg", "     0.70", "     0.71", "     0.70", "     7464972"])
        return table.get_html_string(attributes={"class": "     foo"})
    elif model_name == 'RandomForest':
        table = PrettyTable(["class", "     precision", "     recall", "     f1-score", "     support"])
        table.add_row(["1", "     0.23", "     0.05", "     0.08", "     77404"])
        table.add_row(["2", "     0.43", "     0.40", "     0.41", "     274655"])
        table.add_row(["3", "     0.63", "     0.64", "     0.64", "     2569908"])
        table.add_row(["4", "     0.60", "     0.46", "     0.52", "     1311775"])
        table.add_row(["5", "     0.75", "     0.83", "     0.79", "     3231230"])
        table.add_row(["accuracy", "     ", "     ", "     0.68", "     7464972"])
        table.add_row(["macro avg", "     0.53", "     0.47", "     0.49", "     7464972"])
        table.add_row(["weighted avg", "     0.70", "     0.71", "     0.70", "     7464972"])
        return table.get_html_string(attributes={"class": "     foo"})
    return None
