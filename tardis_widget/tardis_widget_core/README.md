tardis_widget_core
===============================

TARDIS widgets for jupyter notebooks

Installation
------------

To install use pip:

    $ pip install tardis_widget_py
    $ jupyter nbextension enable --py --sys-prefix tardis_widget_py


For a development installation (requires npm),

    $ git clone https://github.com/tardis-sn/tardis_widget_core.git
    $ cd tardis_widget_core
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix tardis_widget_py
    $ jupyter nbextension enable --py --sys-prefix tardis_widget_py
