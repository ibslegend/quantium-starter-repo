import dash
from dash import dcc, html
import pandas as pd

# Load data
df = pd.read_csv(
    r"C:\Users\ibsle\Documents\quantium-starter-repo\data\sales.txt",
    header=None,
    names=["sales", "date", "region"]
)

# Convert types
df["sales"] = df["sales"].astype(float)
df["date"] = pd.to_datetime(df["date"])

# 🔥 IMPORTANT: aggregate data
df = df.groupby(["date", "region"], as_index=False)["sales"].sum()

# Sort after grouping
df = df.sort_values("date")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Over Time by Region"),

    dcc.Graph(
        figure={
            "data": [
                {
                    "x": df[df["region"] == region]["date"],
                    "y": df[df["region"] == region]["sales"],
                    "type": "line",
                    "name": region
                }
                for region in df["region"].unique()
            ],
            "layout": {
                "title": "Regional Sales Trend",
                "xaxis": {"title": "Date"},
                "yaxis": {"title": "Sales"}
            }
        }
    )
])

if __name__ == "__main__":
    app.run(debug=True)