
SELECT
    p.id_pagamento,
    p.id_empenho,
    e.id_contrato,
    c.id_fornecedor,
    f.nome AS fornecedor,
    p.valor
FROM pagamento p
INNER JOIN empenho e 
       ON e.id_empenho = p.id_empenho
INNER JOIN contrato c
       ON c.id_contrato = e.id_contrato
INNER JOIN fornecedor f
       ON f.id_fornecedor = c.id_fornecedor
WHERE NOT EXISTS (
    SELECT 1 FROM liquidacao_nota_fiscal lnf 
    WHERE lnf.id_empenho = p.id_empenho
);