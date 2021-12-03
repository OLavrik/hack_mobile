from altair import Chart, X, Y, Axis, Data, DataFormat
import pandas as pd
import numpy as np
from flask import render_template, url_for, flash, redirect, request, make_response, jsonify, abort
from web import app
from web.utils import utils, altair_plot, plotly_plot
import json
from .eda import EDA_VISUAL

# Loading raw data and clean it



#loading data
sample, describe, unique, numeric, nan_dict, summury_class = utils.load_data()


@app.route("/")
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





@app.route("/model", methods=['POST'])
def select_model():
    # total confirmed cases globally
    # take country input from user
    """
    select model
    """

    context = {}
    return render_template('country.html', context=context)
