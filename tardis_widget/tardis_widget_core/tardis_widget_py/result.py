import ipywidgets as widgets
import pandas as pd
from traitlets import Unicode
from ipywidgets import Layout, Button, Box, VBox
from IPython.display import display

@widgets.register
class Result(widgets.DOMWidget):
    """
    Result Widget for tardis

    It has the following as methods for now:

    - Model Parameters

    - Tabulated Results

    - Visualized Results

    """
    _view_name = Unicode("ResultView").tag(sync=True)
    _model_name = Unicode("ResultModel").tag(sync=True)
    _view_module = Unicode("tardis_widget_core").tag(sync=True)
    _model_module = Unicode("tardis_widget_core").tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)


    def model_parameters(self):
        pass


    def tabulated_results(self, input_a, input_b):
        a = range(input_a)
        b = range(input_b)
        df = pd.DataFrame()
        df['Rad. temp'] = a # change to read values for Rad. temp column
        df['Ws'] = b # change to read values for Ws column
        df.index = range(1, len(df)+1)
        df.index.names = ['Shell']
        return df


    def visualized_results(self):
        pass
