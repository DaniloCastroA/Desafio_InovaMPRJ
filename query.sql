-- contratos com pagamento acima do valor contratado

SELECT
    c.id_contrato,
    c.data,
    c.valor AS valor_contrato,
    COALESCE(SUM(p.valor), 0) AS total_pago,
    COALESCE(SUM(p.valor), 0) - c.valor AS excedente  -- cálculo do excedente
FROM contrato c
LEFT JOIN empenho e ON e.id_contrato = c.id_contrato
LEFT JOIN pagamento p ON p.id_empenho = e.id_empenho
GROUP BY c.id_contrato, c.data, c.valor
HAVING COALESCE(SUM(p.valor), 0) > c.valor
ORDER BY excedente DESC
LIMIT 10;
