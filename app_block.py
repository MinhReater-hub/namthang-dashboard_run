from dash import Dash, html
import dash
import dash_bootstrap_components as dbc

from components.sidebar import sidebar

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.CYBORG],
    title="Nam Thắng Group Dashboard",
)

app.layout = html.Div(
    [
        sidebar,

        html.Div(
            dash.page_container,
            style={
                "marginLeft": "260px",
                "padding": "24px",
                "minHeight": "100vh",
                "backgroundColor": "#0f172a",
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=False)
