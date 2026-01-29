
SELECT
    c.id_contrato,
    f.nome AS fornecedor,
    c.valor AS valor_contrato,
    MIN(c.data) AS data_inicio,                          
    MAX(lnf.data_emissao) AS data_fim,                  
    (MAX(lnf.data_emissao) - MIN(c.data)) AS dias_execucao,
    c.valor / NULLIF((MAX(lnf.data_emissao) - MIN(c.data)), 0) AS valor_por_dia
FROM contrato c
JOIN fornecedor f ON f.id_fornecedor = c.id_fornecedor
LEFT JOIN empenho e ON e.id_contrato = c.id_contrato
LEFT JOIN liquidacao_nota_fiscal lnf ON lnf.id_empenho = e.id_empenho
GROUP BY c.id_contrato, f.nome, c.valor
HAVING COUNT(lnf.id_liquidacao_empenhonotafiscal) > 0
ORDER BY valor_por_dia DESC
LIMIT 10;
