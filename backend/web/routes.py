import pandas as pd
import numpy as np
from flask import render_template, url_for, flash, redirect, request, make_response, jsonify, abort
from web import app
from web.utils import utils, plotly_plot
import json
from .eda import EDA_VISUAL
from .test_model import plot_predicts, test_sample, test_sample_predict, test_post_sample, load_model_info, plot_I

# Loading raw data and clean it



#loading data
sample, describe, unique, numeric, nan_dict, summury_class = utils.load_data()


@app.route("/")
def index():
    return render_template('layout.html')

@app.route("/eda")
def plot_plotly_global():
    # total confirmed cases globally
    sample, describe, unique, numeric, nan_dict, summury_class = utils.load_data()
    eda = EDA_VISUAL(sample, describe, unique, numeric, nan_dict, summury_class)
    plot1 = eda.aggregation_class()
    plot2 = eda.aggreg_nun()
    plot3 = eda.aggreg_unique()

    context = {"plot1": plot1,
               "plot2": plot2,
               "plot3": plot3}
    return render_template('plotly.html', context=context)


@app.route("/appstore", methods=['POST'])
def plot_appstore():
    print(request.form)
    # total confirmed cases globally
    sample, describe, unique, numeric, nan_dict, summury_class = utils.load_data()
    eda = EDA_VISUAL(sample, describe, unique, numeric, nan_dict, summury_class)
    plot1 = eda.aggregation_class()

    context = {"plot1": plot1}
    return render_template('appstore.html', context=context)


@app.route("/model", methods=['POST'])
def select_model():
    # total confirmed cases globally
    # take country input from user

    # cash = load_model(request.form['model_name'])
    # res_df = run_model_on_test(cash)
    print('select_model')
    plot1 = plot_predicts(test_sample, 'Sample of test data')
    plot2 = plot_predicts(test_post_sample, 'Postprocessed sample of test data')
    plot3 = plot_predicts(test_sample_predict, 'Predicts on sample of test data')
    f_imp = plot_I()
    inf = load_model_info(request.form['model_name'])
    context = {'plot1': plot1, 'plot2': plot2, 'plot3': plot3, 'info': inf, 'f_imp': f_imp}
    return render_template('test_model.html', context=context)
