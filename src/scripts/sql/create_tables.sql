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

-- Pasos iniciales -1
ALTER TABLE public.historico_aba_macroactivos
ALTER COLUMN ingestion_month TYPE INTEGER
USING ingestion_month::INTEGER;

ALTER TABLE public.historico_aba_macroactivos
ALTER COLUMN cod_activo TYPE INTEGER
USING cod_activo::INTEGER;

ALTER TABLE public.historico_aba_macroactivos
ALTER COLUMN cod_perfil_riesgo TYPE INTEGER
USING cod_perfil_riesgo::INTEGER;


-- Añadir nueva columna para fecha completa
ALTER TABLE public.historico_aba_macroactivos ADD COLUMN ingestion_date DATE;

-- integridad referencial
ALTER TABLE public.historico_aba_macroactivos
ADD CONSTRAINT historico_aba_macroactivos_pkey PRIMARY KEY (id_sistema_cliente, ingestion_date, cod_activo), 
ADD CONSTRAINT ca_fkey FOREIGN KEY (cod_activo) REFERENCES catalogo_activos(cod_activo) ON DELETE CASCADE,
ADD CONSTRAINT cpr_fkey FOREIGN KEY (cod_perfil_riesgo) REFERENCES cat_perfil_riesgo(cod_perfil_riesgo) ON DELETE CASCADE,
ADD CONSTRAINT cb_fkey FOREIGN KEY (cod_banca) REFERENCES catalogo_banca(cod_banca) ON DELETE CASCADE;

-- PRIMARY KEY (id_sistema_cliente, ingestion_year, ingestion_month, ingestion_day, cod_activo, macroactivo, aba, cod_perfil_riesgo, cod_banca, year, month)