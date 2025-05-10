import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load pre-processed data
df = pd.read_csv("aggregated_customer_data.csv")  # Or your combined dataset

# Create 3D PCA figure
fig = px.scatter_3d(
    df,
    x='PC1', y='PC2', z='PC3',
    color='Cluster',
    symbol='Label',
    title='PCA Clustering: Aggregated vs Raw',
    opacity=0.7
)

# Dash app
app = dash.Dash(__name__)
app.title = "PCA KMeans Dashboard"

app.layout = html.Div([
    html.H1("📊 PCA + KMeans Customer Segmentation"),
    dcc.Graph(figure=fig),
    html.P("Explore PCA clusters for both raw and aggregated datasets."),
])

if __name__ == "__main__":
    app.run_server(debug=True)
