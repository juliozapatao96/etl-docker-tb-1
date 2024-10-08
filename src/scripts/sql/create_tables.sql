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
    cod_banca VARCHAR(10) PRIMARY KEY,
    banca VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS historico_aba_macroactivos (
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

-- PRIMARY KEY (id_sistema_cliente, ingestion_year, ingestion_month, ingestion_day, cod_activo, macroactivo, aba, cod_perfil_riesgo, cod_banca, year, month)