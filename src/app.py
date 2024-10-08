import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from sqlalchemy import create_engine
import urllib.parse
from dotenv import load_dotenv
import os



from src.scripts.python.process_and_transform_data import split_sql_script
from src.etl import main as run_etl


# Ejecutar el proceso ETL al iniciar la aplicación
print("Iniciando el proceso ETL...")
run_etl()
print("Proceso ETL completado.")



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
path = os.path.join(".","src","scripts", "sql", sql_script_filename)

with open(path, 'r') as file:
    sql_script = file.read()

# Dividir el script en declaraciones individuales
sql_statements = split_sql_script(sql_script)

query_banca = sql_statements[0]
query_perfil_riesgo = sql_statements[1]
query_cliente = sql_statements[2]
query_aba_mensual = sql_statements[3]

# Ejecutar las consultas y cargar los datos en DataFrames
try:
    df_banca = pd.read_sql(query_banca, engine)
    df_perfil_riesgo = pd.read_sql(query_perfil_riesgo, engine)
    df_cliente = pd.read_sql(query_cliente, engine)
    df_aba_mensual = pd.read_sql(query_aba_mensual, engine)
except Exception as e:
    print(f"Error al ejecutar las consultas: {e}")

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Crear las gráficas
fig_banca = px.bar(df_banca, x='banca', y='porcentaje', color='macroactivo', title='Portafolio por porcentaje de Banca y Macroactivo')
fig_perfil_riesgo = px.bar(df_perfil_riesgo, x='perfil_riesgo', y='porcentaje', color='macroactivo', title='Portafolio por porcentaje de Perfil Riesgo y Macroactivo')


# Calcular la suma total de total_aba_macroactivo y total_aba por id_sistema_cliente
total_aba_macroactivo_sum_by_id = df_cliente.groupby('id_sistema_cliente')['total_aba_macroactivo'].sum()
total_aba_sum_by_id = df_cliente.groupby('id_sistema_cliente')['total_aba'].sum()

# Crear las gráficas pie chart para 'macroactivos' y 'activos'
fig_pie_macroactivos = px.pie(df_cliente, names=total_aba_macroactivo_sum_by_id.index,
                            values=total_aba_macroactivo_sum_by_id.values, title='Portafolio por Cliente y Macroactivos del total de portafolio')
# Ocultar los porcentajes menores al 5% en la gráfica de macroactivos
fig_pie_macroactivos.update_traces(textposition='inside', textinfo='percent+label', insidetextorientation='radial',
                                pull=[0.1 if p < 0.05 else 0 for p in total_aba_macroactivo_sum_by_id.values])

fig_pie_activos = px.pie(df_cliente, names=total_aba_sum_by_id.index,
                        values=total_aba_sum_by_id.values, title='Portafolio por Cliente y Activos del total de portafolio')
# Ocultar los porcentajes menores al 5% en la gráfica de activos
fig_pie_activos.update_traces(textposition='inside', textinfo='percent+label', insidetextorientation='radial',
                            pull=[0.1 if p < 0.05 else 0 for p in total_aba_sum_by_id.values])

# Crear la gráfica de línea
fig_line_chart_aba_mensual = px.line(df_aba_mensual, x='month_year', y='promedio_mensual_aba', title='Evolución del Promedio Mensual del ABA')

# Crear las gráficas pie chart
fig_pie_macroactivos_ma = px.pie(df_cliente, names='macroactivo',
                            values='total_aba_macroactivo', title='Macroactivos del total de portafolio')

# Crear las gráficas pie chart
fig_pie_activos_a = px.pie(df_cliente, names='activo',
                            values='total_aba', title='Activos del total de portafolio')
fig_pie_activos_a.update_traces(textinfo='none')  # Ocultar los porcentajes

# Configurar el layout de la aplicación con un arreglo 2x2
app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='stacked-column-chart-banca',
            figure=fig_banca
        ),
        dcc.Graph(
            id='stacked-column-chart-perfil-riesgo',
            figure=fig_perfil_riesgo
        )
    ], style={'display': 'flex', 'flex-direction': 'row'}),

    html.Div([
        dcc.Graph(
            id='pie-chart-macroactivos',
            figure=fig_pie_macroactivos
        ),
        dcc.Graph(
            id='pie-chart-activos',
            figure=fig_pie_activos
        )
    ], style={'display': 'flex', 'flex-direction': 'row'}),

    html.Div([
        dcc.Graph(
            id='pie-chart-macroactivos-ma',
            figure=fig_pie_macroactivos_ma
        ),
        dcc.Graph(
            id='pie-chart-activos-a',
            figure=fig_pie_activos_a
        )
    ], style={'display': 'flex', 'flex-direction': 'row'}),

    html.Div([
        dcc.Graph(
            id='line-chart-aba-mensual',
            figure=fig_line_chart_aba_mensual
        )
    ]),
])



if __name__ == '__main__':
    app.run_server(debug=False)    