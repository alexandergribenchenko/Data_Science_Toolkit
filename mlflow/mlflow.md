# mlflow

# Links de interes
- [Documentación oficial](https://mlflow.org/docs/latest/index.html#)
- [Tutoriales y ejemplos](https://mlflow.org/docs/latest/tutorials-and-examples/index.html)

# Código


# Experimento wine
- Request unico dato
```python
{
  "dataframe_split": {
    "columns": [
      "fixed acidity",
      "volatile acidity",
      "citric acid",
      "residual sugar",
      "chlorides",
      "free sulfur dioxide",
      "total sulfur dioxide",
      "density",
      "pH",
      "sulphates",
      "alcohol"
    ],
    "data": [
      [
        7.4,
        0.7,
        0.0,
        1.9,
        0.076,
        11.0,
        34.0,
        0.9978,
        3.51,
        0.56,
        9.4
      ]
    ]
  }
}

```
- Response único dato:
```python
{
  "predictions": [
    5.343644383858527,
    5.517806023434062,
    5.406008491177671
  ]
}
```



- Request multiples datos (3 muestras)
```python
{
  "dataframe_split": {
    "columns": [
      "fixed acidity",
      "volatile acidity",
      "citric acid",
      "residual sugar",
      "chlorides",
      "free sulfur dioxide",
      "total sulfur dioxide",
      "density",
      "pH",
      "sulphates",
      "alcohol"
    ],
    "data": [
      [
        7.4,
        0.7,
        0.0,
        1.9,
        0.076,
        11.0,
        34.0,
        0.9978,
        3.51,
        0.56,
        9.4
      ],
      [
        6.7,
        0.8,
        0.12,
        2.0,
        0.064,
        11.0,
        22.0,
        0.9956,
        3.4,
        0.63,
        10.0
      ],
      [
        8.0,
        0.45,
        0.23,
        2.2,
        0.094,
        16.0,
        39.0,
        0.9972,
        3.29,
        0.54,
        9.5
      ]
    ]
  }
}
```
