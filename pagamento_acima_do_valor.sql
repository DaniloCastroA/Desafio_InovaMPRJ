
SELECT *
FROM (
    SELECT
        c.id_contrato,
        c.data,
        c.valor AS valor_contrato,
        COALESCE(e.valor, 0) AS total_pago,
        COALESCE(e.valor, 0) - c.valor AS excedente,
        ROW_NUMBER() OVER (ORDER BY COALESCE(e.valor, 0) - c.valor DESC) AS ranking
    FROM contrato c
    LEFT JOIN (
        SELECT id_contrato, SUM(p.valor) AS valor
        FROM empenho e
        LEFT JOIN pagamento p ON p.id_empenho = e.id_empenho
        GROUP BY id_contrato
    ) e ON e.id_contrato = c.id_contrato
    GROUP BY c.id_contrato, c.data, c.valor, e.valor
    HAVING COALESCE(e.valor, 0) > c.valor
) t
WHERE ranking <= 10;