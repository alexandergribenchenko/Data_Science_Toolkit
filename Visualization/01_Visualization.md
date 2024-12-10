# Visualization Resources

- [The Data Visualisation Catalogue](https://datavizcatalogue.com/)
- [The Python Graph Gallery](https://www.python-graph-gallery.com/)
- [Plotly](https://plotly.com/python/)


# Tipos de gráficos
- [Pareto chart kaggle plotly](https://www.kaggle.com/code/sc0v1n0/how-to-create-a-pareto-chart-using-plotly)




```python
df_plot = df[(df.airline_code.isin(['AV','LA']))&(df.rt=='BOGSCL')]
fig, ax =plt.subplots()
sns.stripplot(data=df_plot, x="flight_date", y="sum_asks", hue='airline_code', jitter=0.2, size=2.5)
fig.set_size_inches(15,6)
plt.xticks(rotation=90)
plt.show()
```

