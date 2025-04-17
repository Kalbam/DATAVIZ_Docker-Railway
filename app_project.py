import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

server = app.server
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dashboard del Proyecto - Entregable #3"

# Lista de pestañas con contenido correspondiente
tabs = [
    dcc.Tab(label='1. Introducción', children=[
        html.H2('Introducción'),
        html.P('Bienvenidos al Dashboard del proyecto. Aquí se presenta una visión general de la problemática, el análisis realizado y los hallazgos encontrados.'),
        html.P('Objetivo general: Presentar los resultados del análisis aplicado a una base de datos específica mediante técnicas estadísticas y de machine learning.')
    ]),
    dcc.Tab(label='2. Contexto', children=[
        html.H2('Contexto'),
        html.P('Descripción breve del contexto del proyecto.'),
        html.Ul([
            html.Li('Fuente de los datos: [Nombre de la fuente]'),
            html.Li('Variables de interés: [listar variables]')
        ])
    ]),
    dcc.Tab(label='3. Planteamiento del Problema', children=[
        html.H2('Planteamiento del Problema'),
        html.P('Describe en pocas líneas la problemática abordada.'),
        html.P('Pregunta problema: ¿Cuál es la pregunta que intenta responder el análisis?')
    ]),
    dcc.Tab(label='4. Objetivos y Justificación', children=[
        html.H2('Objetivos y Justificación'),
        html.H4('Objetivo General'),
        html.Ul([html.Li('[Objetivo general del proyecto]')]),
        html.H4('Objetivos Específicos'),
        html.Ul([
            html.Li('Objetivo específico 1'),
            html.Li('Objetivo específico 2'),
            html.Li('Objetivo específico 3')
        ]),
        html.H4('Justificación'),
        html.P('Explicación breve sobre la importancia de abordar el problema planteado y los beneficios esperados.')
    ]),
    dcc.Tab(label='5. Marco Teórico', children=[
        html.H2('Marco Teórico'),
        html.P('Resumen de conceptos teóricos clave relacionados con el proyecto. Se pueden incluir referencias o citas.')
    ]),
    dcc.Tab(label='6. Metodología', children=[
        html.H2('Metodología'),
        html.H4('a. Definición del Problema a Resolver'),
        html.Ul([
            html.Li('Tipo de problema: clasificación / regresión / agrupamiento / series de tiempo'),
            html.Li('Variable objetivo o de interés: [Nombre de la variable]')
        ]),
        html.H4('b. Preparación de los Datos'),
        html.Ul([
            html.Li('Limpieza y transformación de datos'),
            html.Li('División del dataset en entrenamiento y prueba o validación cruzada')
        ]),
        html.H4('c. Selección del Modelo o Algoritmo'),
        html.Ul([
            html.Li('Modelo(s) seleccionados'),
            html.Li('Justificación de la elección'),
            html.Li('Ecuación o representación matemática si aplica')
        ]),
        html.H4('d. Entrenamiento y Evaluación del Modelo'),
        html.Ul([
            html.Li('Proceso de entrenamiento'),
            html.Li('Métricas de evaluación: RMSE, MAE, Accuracy, etc.'),
            html.Li('Validación utilizada')
        ])
    ]),
    dcc.Tab(label='7. Resultados y Análisis Final', children=[
        html.H2('Resultados y Análisis Final'),
        html.H4('a. Análisis Exploratorio de Datos (EDA)'),
        html.Ul([
            html.Li('Estadísticas descriptivas'),
            html.Li('Gráficos, distribuciones y correlaciones')
        ]),
        html.H4('b. Visualización de Resultados del Modelo'),
        html.Ul([
            html.Li('Gráficas de comparación: valores reales vs. predichos'),
            html.Li('Análisis de residuales')
        ]),
        html.H4('c. Limitaciones y Consideraciones Finales'),
        html.Ul([
            html.Li('Restricciones del análisis'),
            html.Li('Posibles mejoras futuras')
        ])
    ]),
    dcc.Tab(label='8. Conclusiones', children=[
        html.H2('Conclusiones'),
        html.Ul([
            html.Li('Principales hallazgos del proyecto'),
            html.Li('Relevancia de los resultados obtenidos'),
            html.Li('Aplicaciones futuras y recomendaciones')
        ])
    ])
]

# Layout del dashboard
app.layout = dbc.Container([
    html.H1("Dashboard del Proyecto - Entregable #3", className="text-center my-4"),
    dcc.Tabs(tabs)
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
