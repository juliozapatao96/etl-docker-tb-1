-- Añadir nueva columna para fecha completa
ALTER TABLE public.historico_aba_macroactivos ADD COLUMN ingestion_date DATE;

-- Actualizar nueva columna
UPDATE public.historico_aba_macroactivos
SET ingestion_date = TO_DATE(CONCAT(ingestion_year, '-', ingestion_month, '-', ingestion_day), 'YYYY-MM-DD');

-- integridad referencial
ALTER TABLE public.historico_aba_macroactivos
ADD CONSTRAINT historico_aba_macroactivos_pkey PRIMARY KEY (id_sistema_cliente, ingestion_date, cod_activo), 
ADD CONSTRAINT ca_fkey FOREIGN KEY (cod_activo) REFERENCES catalogo_activos(cod_activo) ON DELETE CASCADE,
ADD CONSTRAINT cpr_fkey FOREIGN KEY (cod_perfil_riesgo) REFERENCES cat_perfil_riesgo(cod_perfil_riesgo) ON DELETE CASCADE,
ADD CONSTRAINT cb_fkey FOREIGN KEY (cod_banca) REFERENCES catalogo_banca(cod_banca) ON DELETE CASCADE;