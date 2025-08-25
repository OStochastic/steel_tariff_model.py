import plotly.graph_objects as go
import numpy as np

Pw = 530.42
P_tariff = 543.15

Q1 = 81600.0
Q2 = 106324.8
Q3 = 83150.4
Q4 = 102562.5

if (Q3 - Q1) == 0:
    slope_S = 1e9
else:
    slope_S = (P_tariff - Pw) / (Q3 - Q1)
intercept_S = Pw - slope_S * Q1

if (Q4 - Q2) == 0:
    slope_D = -1e9
else:
    slope_D = (P_tariff - Pw) / (Q4 - Q2)
intercept_D = Pw - slope_D * Q2

fig = go.Figure()

q_axis_max = max(Q2, Q4) * 1.15
quantity_range_plot = np.linspace(0, q_axis_max, 500)
price_S_plot = intercept_S + slope_S * quantity_range_plot
price_D_plot = intercept_D + slope_D * quantity_range_plot

fig.add_trace(go.Scatter(
    x=quantity_range_plot, y=price_S_plot,
    mode='lines', name='Domestic Supply (S)',
    line=dict(color='darkorange', width=2)
))
fig.add_trace(go.Scatter(
    x=quantity_range_plot, y=price_D_plot,
    mode='lines', name='Domestic Demand (D)',
    line=dict(color='darkviolet', width=2)
))

fig.add_hline(y=Pw, line_dash="dash", line_color="green", name=f'World Price (Pw=${Pw:.0f})',
              annotation_text="World Price", annotation_position="bottom right")
fig.add_hline(y=P_tariff, line_dash="dash", line_color="red", name=f'Price with Tariff (Pt=${P_tariff:.0f})',
              annotation_text="Price with Tariff", annotation_position="bottom right")

quant_cs_after = np.linspace(0, Q4, 200)
price_d_cs_after = intercept_D + slope_D * quant_cs_after
fig.add_trace(go.Scatter(
    x=np.concatenate([quant_cs_after, quant_cs_after[::-1]]),
    y=np.concatenate([price_d_cs_after, np.full(len(quant_cs_after), P_tariff)]),
    fill='toself', fillcolor='rgba(128,0,128,0.3)', line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip", showlegend=True, name='Consumer Surplus'
))

quant_ps_after = np.linspace(0, Q3, 200)
price_s_ps_after = intercept_S + slope_S * quant_ps_after
fig.add_trace(go.Scatter(
    x=np.concatenate([quant_ps_after, quant_ps_after[::-1]]),
    y=np.concatenate([price_s_ps_after, np.full(len(quant_ps_after), P_tariff)]),
    fill='toself', fillcolor='rgba(255,165,0,0.3)', line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip", showlegend=True, name='Producer Surplus'
))

fig.add_trace(go.Scatter(x=[Q3, Q4, Q4, Q3, Q3], y=[Pw, Pw, P_tariff, P_tariff, Pw], fill="toself", fillcolor='rgba(144,238,144,0.6)', line=dict(color='black', width=1), name='c: Tariff Revenue'))
fig.add_trace(go.Scatter(x=[Q1, Q3, Q3, Q1], y=[Pw, Pw, P_tariff, Pw], fill="toself", fillcolor='rgba(255,255,0,0.6)', line=dict(color='black', width=1), name='b: DWL Production'))
fig.add_trace(go.Scatter(x=[Q4, Q2, Q4, Q4], y=[P_tariff, Pw, Pw, P_tariff], fill="toself", fillcolor='rgba(255,215,0,0.6)', line=dict(color='black', width=1), name='d: DWL Consumption'))

fig.update_layout(
    title='Partial Equilibrium Model: Effects of an Import Tariff on the US Steel Market',
    xaxis_title='Quantity (thousand metric tons)',
    yaxis_title='Price (USD/metric ton)',
    legend_title='Economic Areas',
    template='plotly_white'
)

fig.update_xaxes(range=[0, q_axis_max])
fig.update_yaxes(range=[0, intercept_D * 1.05])

file_name = "interactive_steel_tariff_graph.html"
fig.write_html(file_name)

print(f"Interactive graph has been saved as '{file_name}'")

