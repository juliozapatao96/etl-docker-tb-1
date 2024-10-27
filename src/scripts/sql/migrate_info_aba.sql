-- 1. Insertar los datos de temp_historico_aba_macroactivos en historico_aba_macroactivos
INSERT INTO public.historico_aba_macroactivos (
    ingestion_year, 
    ingestion_month,  
    ingestion_day, 
    id_sistema_cliente, 
    macroactivo, 
    cod_activo,        
    aba, 
    cod_perfil_riesgo, 
    cod_banca, 
    year, 
    month,
    ingestion_date
)
SELECT 
    ingestion_year, 
    ingestion_month,
    ingestion_day, 
    id_sistema_cliente, 
    macroactivo, 
    cod_activo,
    aba, 
    cod_perfil_riesgo,
    cod_banca, 
    year, 
    month,
    ingestion_date
FROM public.temp_historico_aba_macroactivos;

-- 2. Eliminar la tabla temporal
DROP TABLE IF EXISTS public.temp_historico_aba_macroactivos;
