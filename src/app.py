import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output
from sqlalchemy import create_engine
import urllib.parse
from dotenv import load_dotenv
import os

from src.scripts.python.process_and_transform_data import split_sql_script
from src.etl import main as run_etl
from src.initialConfiguration import main as run_configuration

# Ejecutar el proceso ETL al iniciar la aplicación
print("Iniciando configuración...")
run_configuration()
print("Proceso de configuración completada.")

print("Iniciando la aplicación Dash...")        
# Cargar las variables de entorno
load_dotenv(dotenv_path='config/config.env')
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_PASSWORD = urllib.parse.quote(DB_PASSWORD)  # Codificar la contraseña

# Crear la cadena de conexión usando SQLAlchemy
db_url = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

sql_script_filename = "query_to_dash.sql"

# Leer el contenido del archivo SQL
path = os.path.join(".", "src", "scripts", "sql", sql_script_filename)

with open(path, 'r') as file:
    sql_script = file.read()

# Dividir el script en declaraciones individuales
sql_statements = split_sql_script(sql_script)

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación con el botón y las gráficas
app.layout = html.Div([
    html.Div(id='status-message', style={'margin-bottom': '20px'}, children=["Listo para iniciar el procesamiento de datos."]),  # Mensaje inicial
    html.Button('Procesar Datos', id='etl-button', n_clicks=0),
    html.Div(id='output-container'),
    html.Div([
        dcc.Graph(id='stacked-column-chart-banca'),
        dcc.Graph(id='stacked-column-chart-perfil-riesgo'),
    ], style={'display': 'flex', 'flex-direction': 'row'}),
    
    html.Div([
        dcc.Graph(id='pie-chart-macroactivos'),
        dcc.Graph(id='pie-chart-activos'),
    ], style={'display': 'flex', 'flex-direction': 'row'}),
    
    html.Div([
        dcc.Graph(id='pie-chart-macroactivos-ma'),
        dcc.Graph(id='pie-chart-activos-a'),
    ], style={'display': 'flex', 'flex-direction': 'row'}),
    
    html.Div([
        dcc.Graph(id='line-chart-aba-mensual')
    ]),
])


# Callback para ejecutar el proceso ETL y actualizar las gráficas
@app.callback(
    [Output('stacked-column-chart-banca', 'figure'),
     Output('stacked-column-chart-perfil-riesgo', 'figure'),
     Output('pie-chart-macroactivos', 'figure'),
     Output('pie-chart-activos', 'figure'),
     Output('pie-chart-macroactivos-ma', 'figure'),
     Output('pie-chart-activos-a', 'figure'),
     Output('line-chart-aba-mensual', 'figure'),
     Output('status-message', 'children')],  # Agregar Output para el mensaje de estado
    [Input('etl-button', 'n_clicks')]
)
def update_graphs(n_clicks) -> bool:
    if n_clicks > 0:
        # Ejecutar el proceso ETL al presionar el botón
        try:
            print("Ejecutando el proceso ETL...")
            etl_success = run_etl()  # Guardar el retorno de run_etl()
            print("Proceso ETL finalizado.")
        except Exception as e:
            print(f"Error al ejecutar el proceso ETL: {e}")
            status_message = "Error al ejecutar el proceso ETL. Por favor, inténtelo de nuevo."
            return dash.no_update + [status_message]  # Devolver solo el mensaje de error
        
        if etl_success:
            try:
                df_banca = pd.read_sql(sql_statements[0], engine)
                df_perfil_riesgo = pd.read_sql(sql_statements[1], engine)
                df_cliente = pd.read_sql(sql_statements[2], engine)
                df_aba_mensual = pd.read_sql(sql_statements[3], engine)
            except Exception as e:
                print(f"Error al ejecutar las consultas: {e}")
                status_message = "Error al cargar los datos. Por favor, inténtelo de nuevo."
                return dash.no_update + [status_message]  # Devolver solo el mensaje de error

            # Crear las gráficas nuevamente con los nuevos datos
            fig_banca = px.bar(df_banca, x='banca', y='porcentaje', color='macroactivo', title='Portafolio por porcentaje de Banca y Macroactivo')
            fig_perfil_riesgo = px.bar(df_perfil_riesgo, x='perfil_riesgo', y='porcentaje', color='macroactivo', title='Portafolio por porcentaje de Perfil Riesgo y Macroactivo')

            total_aba_macroactivo_sum_by_id = df_cliente.groupby('id_sistema_cliente')['total_aba_macroactivo'].sum()
            total_aba_sum_by_id = df_cliente.groupby('id_sistema_cliente')['total_aba'].sum()

            fig_pie_macroactivos = px.pie(df_cliente, names=total_aba_macroactivo_sum_by_id.index, values=total_aba_macroactivo_sum_by_id.values, title='Portafolio por Cliente y Macroactivos del total de portafolio')
            fig_pie_macroactivos.update_traces(textposition='inside', textinfo='percent+label', insidetextorientation='radial',
                                            pull=[0.1 if p < 0.05 else 0 for p in total_aba_macroactivo_sum_by_id.values])

            fig_pie_activos = px.pie(df_cliente, names=total_aba_sum_by_id.index, values=total_aba_sum_by_id.values, title='Portafolio por Cliente y Activos del total de portafolio')
            fig_pie_activos.update_traces(textposition='inside', textinfo='percent+label', insidetextorientation='radial',
                                        pull=[0.1 if p < 0.05 else 0 for p in total_aba_sum_by_id.values])

            fig_pie_macroactivos_ma = px.pie(df_cliente, names='macroactivo', values='total_aba_macroactivo', title='Macroactivos del total de portafolio')

            fig_pie_activos_a = px.pie(df_cliente, names='activo', values='total_aba', title='Activos del total de portafolio')
            fig_pie_activos_a.update_traces(textinfo='none')  # Ocultar los porcentajes

            fig_line_chart_aba_mensual = px.line(df_aba_mensual, x='month_year', y='promedio_mensual_aba', title='Evolución del Promedio Mensual del ABA')

            status_message = "El proceso fue ejecutado exitosamente."
            # Retornar las gráficas actualizadas y el mensaje de estado
            return [fig_banca, fig_perfil_riesgo, fig_pie_macroactivos, fig_pie_activos, fig_pie_macroactivos_ma, fig_pie_activos_a, fig_line_chart_aba_mensual, status_message]

        status_message = "No se encontraron archivos para procesar."
        return [dash.no_update] * 7 + [status_message]
        
       
    return [dash.no_update] * 7 + ["Listo para iniciar el procesamiento de datos."]  # No hacer nada si no se ha presionado el botón

if __name__ == '__main__':
    app.run_server(debug=False)
