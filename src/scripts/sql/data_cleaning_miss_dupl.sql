-- Elimina los valores Faltantes
DELETE FROM public.historico_aba_macroactivos
WHERE id_sistema_cliente IS NULL OR id_sistema_cliente = 'NaN'  
	OR cod_activo IS NULL OR cod_activo = 'NaN' 
	OR cod_perfil_riesgo IS NULL OR cod_perfil_riesgo = 'NaN' 
	OR cod_banca IS NULL OR cod_banca = 'NaN'
	OR aba IS NULL OR aba = 'NaN'
	OR year IS NULL OR year = 'NaN'
	OR month IS NULL OR month = 'NaN'
	OR ingestion_month IS NULL OR ingestion_month = 'NaN'
	OR macroactivo IS NULL OR macroactivo = 'NaN';
	
-- Eliminar los valores duplicados
CREATE TEMP TABLE temp_historico_aba AS
SELECT DISTINCT ON (ingestion_year, ingestion_month, ingestion_day, 
    id_sistema_cliente, cod_activo, macroactivo, aba, 
	cod_perfil_riesgo, cod_banca, year, month) 
    *
FROM public.historico_aba_macroactivos;

TRUNCATE public.historico_aba_macroactivos;

INSERT INTO public.historico_aba_macroactivos
SELECT * FROM temp_historico_aba;

DROP TABLE temp_historico_aba;