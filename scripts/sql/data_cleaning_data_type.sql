ALTER TABLE public.historico_aba_macroactivos
ALTER COLUMN ingestion_month TYPE INTEGER
USING ingestion_month::INTEGER;

ALTER TABLE public.historico_aba_macroactivos
ALTER COLUMN cod_activo TYPE INTEGER
USING cod_activo::INTEGER;

ALTER TABLE public.historico_aba_macroactivos
ALTER COLUMN cod_perfil_riesgo TYPE INTEGER
USING cod_perfil_riesgo::INTEGER;