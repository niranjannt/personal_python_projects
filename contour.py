import plotly.graph_objects as go

x = [1,2,3,4,5]
y = [1,2,3,4]

z = [[12,13,45,45],
     [11,10,21,20],
     [11,20,23,30],
     [22,34,45,67],
     [40,60,78,40]]

figure = go.Figure(go.Contour(x = x, y = y, z = z))

figure.show()
