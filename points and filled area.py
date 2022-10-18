import plotly.graph_objects as go

fig = go.Figure(

    go.Scattermapbox(
        fill = "toself",
        lon = [77.1025,72.8777,88.3639, 80.2707],
        lat = [28.7041,19.0760,22.5726,13.0827],
        marker = {"size":100, "color":"red"}
        )
    )

fig.update_layout(mapbox_style = "stamen-terrain", showlegend = False)

fig.show()
