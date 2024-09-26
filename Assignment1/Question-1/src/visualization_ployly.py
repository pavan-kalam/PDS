import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Load the cleaned data
df = pd.read_csv('data_clean/frailty_data_clean.csv')

# Sort the dataframe by age for proper curve plotting
df = df.sort_values(by='Age')

# Create smoothed curves for each Frailty status
frailty_0 = df[df['Frailty'] == 0]
frailty_1 = df[df['Frailty'] == 1]

# Generate scatter points for the curve
fig = go.Figure()

# Add curve for Frailty == 0 (No)
fig.add_trace(go.Scatter(
    x=frailty_0['Age'],
    y=frailty_0['Grip strength'],
    mode='lines+markers',
    name='Frailty = No',
    line=dict(color='blue'),
    marker=dict(color='blue', size=8),
))

# Add curve for Frailty == 1 (Yes)
fig.add_trace(go.Scatter(
    x=frailty_1['Age'],
    y=frailty_1['Grip strength'],
    mode='lines+markers',
    name='Frailty = Yes',
    line=dict(color='red'),
    marker=dict(color='red', size=8),
))

# Update layout for better aesthetics
fig.update_layout(
    title='Grip Strength vs Age with Frailty (Curve)',
    xaxis_title='Age (years)',
    yaxis_title='Grip Strength (kg)',
    legend_title='Frailty Status',
    height=600,
    width=800,
)

# Save the plot as an HTML file
fig.write_html('result/grip_strength_curve_plotly1.html')

# Show the plot
fig.show()
