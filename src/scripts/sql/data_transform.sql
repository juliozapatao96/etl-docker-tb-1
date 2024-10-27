-- Añadir nueva columna para fecha completa
ALTER TABLE public.temp_historico_aba_macroactivos ADD COLUMN ingestion_date DATE;

-- Actualizar nueva columna
UPDATE public.temp_historico_aba_macroactivos
SET ingestion_date = TO_DATE(CONCAT(ingestion_year, '-', ingestion_month, '-', ingestion_day), 'YYYY-MM-DD');