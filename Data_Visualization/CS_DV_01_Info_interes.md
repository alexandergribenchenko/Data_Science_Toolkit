# Enlaces de interes

- [Mejor pagina de graficación](https://www.python-graph-gallery.com/)

- [Evitar overplotting](https://www.python-graph-gallery.com/134-how-to-avoid-overplotting-with-python)



df_plot = df[(df.airline_code.isin(['AV','LA']))&(df.rt=='BOGSCL')]
fig, ax =plt.subplots()
sns.stripplot(data=df_plot, x="flight_date", y="sum_asks", hue='airline_code', jitter=0.2, size=2.5)
fig.set_size_inches(15,6)
plt.xticks(rotation=90)
plt.show()
