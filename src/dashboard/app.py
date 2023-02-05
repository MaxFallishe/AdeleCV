import dash
import dash_bootstrap_components as dbc

from task.SegmentationTask import SegmentationTask


app = dash.Dash(
    __name__,
    update_title=None,
    external_stylesheets=[dbc.themes.FLATLY],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

srv = app.server

app.config.suppress_callback_exceptions = True

app.title = "AutoDL-CV"

_task = SegmentationTask()

