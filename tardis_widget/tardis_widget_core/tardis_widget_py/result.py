import ipywidgets as widgets
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from traitlets import Unicode
from ipywidgets import Layout, Button, Box, VBox
from IPython.display import display
from IPython.core.pylabtools import print_figure
plt.ioff()

@widgets.register
class Result(widgets.DOMWidget):
    """
    Result Widget for tardis

    It has the following as methods:

    - Plots data into graph

    """
    _view_name = Unicode("ResultView").tag(sync=True)
    _model_name = Unicode("ResultModel").tag(sync=True)
    _view_module = Unicode("tardis_widget_core").tag(sync=True)
    _model_module = Unicode("tardis_widget_core").tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)


    def __init__(self, row, column):
        self.row = row
        self.column = column

    def _repr_png_(self):
        fig = plt.figure()
        plt.plot(self.row, self.column)
        data = print_figure(fig, 'png')
        plt.close()
        return data
