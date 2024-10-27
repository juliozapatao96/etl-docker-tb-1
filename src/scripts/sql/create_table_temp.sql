CREATE TABLE IF NOT EXISTS temp_historico_aba_macroactivos (
    ingestion_year INTEGER,
    ingestion_month NUMERIC,
    ingestion_day INTEGER,
    id_sistema_cliente VARCHAR(50),
    macroactivo VARCHAR(50),
    cod_activo VARCHAR(50),
    aba NUMERIC,
    cod_perfil_riesgo VARCHAR(50),
    cod_banca VARCHAR(10),
    year VARCHAR(50),
    month NUMERIC
);