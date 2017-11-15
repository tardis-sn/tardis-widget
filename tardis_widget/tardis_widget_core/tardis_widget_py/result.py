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

    
