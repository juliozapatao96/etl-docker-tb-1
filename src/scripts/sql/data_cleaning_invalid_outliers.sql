-- Se crea por las pruebas realizadas. Para evitar eliminar el grupo EG de catalogo_banca
UPDATE public.temp_historico_aba_macroactivos
SET id_sistema_cliente = REPLACE(id_sistema_cliente, '1.00901E+11', '10088888888')
WHERE id_sistema_cliente  = '1.00901E+11';

-- valida los rangos adecuados en las fechas
DELETE FROM public.temp_historico_aba_macroactivos
WHERE ingestion_year < 2000 OR ingestion_year > 2050
	OR ingestion_month NOT BETWEEN 1 AND 12
	OR ingestion_day NOT BETWEEN 1 AND 31;
	
-- Elimina valores que tienen notación científica
DELETE FROM public.temp_historico_aba_macroactivos
WHERE  id_sistema_cliente SIMILAR TO '%([eE][-+]?[0-9]+)';

-- valida que estos campos de tipo texto no sean numéricos
DELETE FROM public.temp_historico_aba_macroactivos
WHERE macroactivo SIMILAR TO '([0-9]*)' 
	OR cod_banca SIMILAR TO '([0-9]*)';
	
-- valida que estos campos tipo numericos no sean de tipo texto
DELETE FROM public.temp_historico_aba_macroactivos
WHERE cod_activo NOT SIMILAR TO '([0-9]*)' 
	OR cod_perfil_riesgo NOT SIMILAR TO '([0-9]*)'; 
	
-- Se verifica que tiene la misma información que las columnas de ingestion (redundantes)

--ALTER TABLE public.temp_historico_aba_macroactivos
--DROP COLUMN year, 
--DROP COLUMN month;


-- valida que los valores que están en cod_activo
-- de la tabla historico concuerden con los códigos que existen en
-- la tabla catalogo_activos
DELETE FROM public.temp_historico_aba_macroactivos AS ham
WHERE ham.cod_activo::INTEGER NOT IN (
    SELECT cod_activo
    FROM public.catalogo_activos
);

-- de forma similar, se contruyen las siguientes
DELETE FROM public.temp_historico_aba_macroactivos AS ham
WHERE ham.cod_perfil_riesgo::INTEGER NOT IN (
    SELECT cod_perfil_riesgo
    FROM public.cat_perfil_riesgo
);

DELETE FROM public.temp_historico_aba_macroactivos AS ham
WHERE ham.cod_banca NOT IN (
    SELECT cod_banca 
    FROM public.catalogo_banca
);