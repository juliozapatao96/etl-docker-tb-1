-- Crear las tablas
CREATE TABLE IF NOT EXISTS cat_perfil_riesgo (
    cod_perfil_riesgo INTEGER PRIMARY KEY,
    perfil_riesgo VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS catalogo_activos (
    cod_activo INTEGER PRIMARY KEY,
    activo VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS catalogo_banca (
    cod_banca VARCHAR(5) PRIMARY KEY,
    banca VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS historico_aba_macroactivos (
    ingestion_year INTEGER,
    ingestion_month INTEGER,
    ingestion_day INTEGER,
    id_sistema_cliente VARCHAR(50),
    macroactivo VARCHAR(100),
    cod_activo INTEGER,
    aba NUMERIC,
    cod_perfil_riesgo INTEGER,
    cod_banca VARCHAR(5),
    year INTEGER,
    month INTEGER
);