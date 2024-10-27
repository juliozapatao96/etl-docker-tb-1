WITH ultima_fecha AS (
    SELECT
        cod_banca,
        MAX(ingestion_date) AS ultima_fecha
    FROM
        historico_aba_macroactivos
    GROUP BY
        cod_banca
)

SELECT
    h.cod_banca,
    cb.banca,
    h.macroactivo,
    SUM(h.aba) AS total_aba,
    ROUND((SUM(h.aba) * 100.0 / SUM(SUM(h.aba)) OVER (PARTITION BY h.cod_banca))::NUMERIC, 2) AS porcentaje
FROM
    historico_aba_macroactivos h
JOIN
    ultima_fecha u ON h.cod_banca = u.cod_banca
JOIN
	catalogo_banca cb ON h.cod_banca = cb.cod_banca
WHERE
    h.ingestion_date = u.ultima_fecha
GROUP BY
    h.cod_banca, cb.banca, h.macroactivo;

-- q2
WITH ultima_fecha AS (
    SELECT
        cod_perfil_riesgo,
        MAX(ingestion_date) AS ultima_fecha
    FROM
        historico_aba_macroactivos
    GROUP BY
        cod_perfil_riesgo
)

SELECT
    h.cod_perfil_riesgo,
    cpr.perfil_riesgo,
    h.macroactivo,
    SUM(h.aba) AS total_aba,
    ROUND((SUM(h.aba) * 100.0 / SUM(SUM(h.aba)) OVER (PARTITION BY h.cod_perfil_riesgo))::NUMERIC,2) AS porcentaje
FROM
    historico_aba_macroactivos h
JOIN
    ultima_fecha u ON h.cod_perfil_riesgo = u.cod_perfil_riesgo
JOIN
	cat_perfil_riesgo cpr ON h.cod_perfil_riesgo = cpr.cod_perfil_riesgo 
WHERE
    h.ingestion_date = u.ultima_fecha
GROUP BY
    cpr.perfil_riesgo, h.cod_perfil_riesgo, h.macroactivo;


-- q3
WITH ultima_fecha AS (
    SELECT
        id_sistema_cliente,
        MAX(ingestion_date) AS ultima_fecha
    FROM
        historico_aba_macroactivos
    GROUP BY
        id_sistema_cliente
),
total_por_macroactivo AS (
    SELECT
        h.id_sistema_cliente,
        h.macroactivo,
        SUM(h.aba) AS total_aba_macroactivo
    FROM
        historico_aba_macroactivos h
    JOIN
        ultima_fecha u ON h.id_sistema_cliente = u.id_sistema_cliente
    WHERE
        h.ingestion_date = u.ultima_fecha
    GROUP BY
        h.id_sistema_cliente, h.macroactivo
)

SELECT
    h.id_sistema_cliente,
    h.macroactivo,
    a.activo,
	ROUND(SUM(h.aba), 0) AS total_aba,
	ROUND(total_macro.total_aba_macroactivo, 0) AS total_aba_macroactivo,
	ROUND(total_macro.total_aba_macroactivo * 100.0 / SUM(SUM(h.aba)) OVER (PARTITION BY h.id_sistema_cliente), 2) AS porcentaje_macroactivo,
	ROUND(SUM(h.aba) * 100.0 / SUM(SUM(h.aba)) OVER (PARTITION BY h.id_sistema_cliente), 2) AS porcentaje_activo
FROM
    historico_aba_macroactivos h
JOIN
    ultima_fecha u ON h.id_sistema_cliente = u.id_sistema_cliente
JOIN
    catalogo_activos a ON h.cod_activo = a.cod_activo
JOIN
    total_por_macroactivo total_macro ON h.id_sistema_cliente = total_macro.id_sistema_cliente AND h.macroactivo = total_macro.macroactivo
WHERE
    h.ingestion_date = u.ultima_fecha
GROUP BY
    h.id_sistema_cliente, h.macroactivo, a.activo, total_macro.total_aba_macroactivo
ORDER BY
    h.id_sistema_cliente, h.macroactivo, a.activo;

-- q4
WITH fecha_filtrada AS (
    SELECT
        ingestion_date,
        aba,
        DATE_TRUNC('month', ingestion_date) AS month_year
    FROM
        historico_aba_macroactivos
    WHERE
        ingestion_date BETWEEN '2023-01-01' AND '2024-12-31'
)
SELECT
    month_year,
    ROUND(AVG(aba),0) AS promedio_mensual_aba
FROM
    fecha_filtrada
GROUP BY
    month_year
ORDER BY
    month_year;

-- q5
SELECT
    ingestion_date,
    DATE_TRUNC('month', ingestion_date) AS month_year,
    aba
FROM
    historico_aba_macroactivos
ORDER BY
    month_year, ingestion_date;

